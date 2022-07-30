from bs4 import BeautifulSoup #untuk melakukan webscrapping
import requests, lxml #Untuk melakukan permintaan http
import re
from datetime import date, timedelta, datetime

class Preprocessing:
    def yesterday(frmt='%d %B %y', string=True):
        yesterday = datetime.now() - timedelta(1)
        if string:
            return yesterday.strftime(frmt)
        return yesterday

    def clean_tag_html(html):
        # Exception Handling
        # jika tidak dapat crawling akan dilewati
        try:
            r = requests.get(html, stream=True)
            soup = BeautifulSoup(r.text, "lxml")

            # buang script dan style
            for script in soup(["script", "style"]):
                script.extract()  # rip it out

            # filtering
            # get text
            text = soup.get_text()
            # text = re.sub("(?:[a-zA-Z'-]+[^a-zA-Z'-]+){0,4}WIB", '', text)
            # menghapus keterangan waktu yang mengganggu
            text = re.sub("(?:[a-zA-Z'-]+[^a-zA-Z'-]+){0,4}WIB", '', text)

            today = date.today()
            date_today = today.strftime("%d %B %Y")

            yesterday = datetime.now() - timedelta(days=1)
            date_yesterday = yesterday.strftime('%d %B %Y')

            month_dict = {"January": "Januari", "February": "Februari", "March": "Maret", "May": "Mei", "June": "Juni",
                          "July": "Juli",
                          "August": "Agustus", "December": "Desember"}

            for key, value in month_dict.items():
                date_today = date_today.replace(key, value)
                date_yesterday = date_yesterday.replace(key, value)
            text = text.replace(date_today, "")
            text = text.replace(date_yesterday, "")

            # print(text)
            # kumpulan teks dari link

            # tokenization
            # break into lines and remove leading and trailing space on each
            # pecah menjadi garis dan hapus spasi awal dan akhir pada masing-masing
            lines = (line.strip() for line in text.splitlines())
            # break multi-headlines into a line each
            # memecah multi-judul menjadi satu baris masing-masing
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            text = '\n'.join(chunk for chunk in chunks if chunk)
            return text

        except requests.exceptions.HTTPError as err:
            return ""

        except requests.exceptions.InvalidSchema as err:
            return ""

        except requests.exceptions.ConnectionError as errc:
            return ""

