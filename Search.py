from bs4 import BeautifulSoup #untuk melakukan webscrapping
import requests, lxml #Untuk melakukan permintaan http
class Search:
    def cari_pertanyaan(keyword):
        # 1 Cari Pertanyaan ke google search
        headers = {
            'User-agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
        }

        params = {
            'q': keyword,  # Masukkan pertanyaan disini
            'gl': 'id',  # country to search from
            'hl': 'id',  # language
        }

        html = requests.get('https://www.google.com/search', headers=headers, params=params)
        soup = BeautifulSoup(html.text, "lxml")
        return soup

    def get_hasil(soup):
        url_source = []
        for result in soup.select('.tF2Cxc'):
            link = result.select_one('.yuRUbf a')['href']
            if link not in url_source:
                url_source.append(link)
        return url_source
        # mengirim kumpulan link web yang berhubungan

