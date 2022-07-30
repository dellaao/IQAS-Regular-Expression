import numpy as np

from Search import Search
from Preprocessing import Preprocessing
from Regex import Regex
from Count import Count
from collections import Counter
import csv

class Main_process:
    def do_main_process(keyword):
        soup = Search.cari_pertanyaan(keyword)

        # 2 Get url dari hasil google search
        url_source = Search.get_hasil(soup)

        # 3 Hapus tag HTML dari link yang dihasilkan
        kumpulan_tanggal = []
        kumpulan_tanggal_bulan = []
        kumpulan_bulan = []
        kumpulan_bulan_tahun = []
        kumpulan_tahun = []
        kumpulan_tanggal_bulan_tahun = []

        for a in url_source:
            text = Preprocessing.clean_tag_html(a)
            # preprocessinglagi

            # 4 dan 5 Identifikasi jawaban dan kumpul seluruh jawaban
            # --------------------------------------------------------
            # 4 cari tanggal bulan tahun regex (tanggal)
            regex = r"([\d]{1,2})"
            cari = Regex.cari_regex(regex, text)

            # 5 Kumpul semua jawaban
            for b in cari:
                kumpulan_tanggal.append(b)

            # --------------------------------------------------------

            # 4 cari tanggal bulan tahun regex (tanggal bulan)
            regex = r"[\d]{1,2} [ADFJMNOS]\w*"
            cari = Regex.cari_regex(regex, text)

            # 5 Kumpul semua jawaban
            for b in cari:
                kumpulan_tanggal_bulan.append(b)

            # --------------------------------------------------------

            # 4 cari tanggal bulan tahun regex (bulan)
            regex = r"\s(Januari|Agustus|Febuari|Maret|April|Mei|Juni|Juli|Agustus|September|Oktober|November|Desember)"
            cari = Regex.cari_regex(regex, text)

            # 5 Kumpul semua jawaban
            for b in cari:
                kumpulan_bulan.append(b)

            # --------------------------------------------------------

            # 4 cari tanggal bulan tahun regex (bulan tahun)
            regex = r"[ADFJMNOS]\w* [\d]{4}"
            cari = Regex.cari_regex(regex, text)

            # 5 Kumpul semua jawaban
            for b in cari:
                kumpulan_bulan_tahun.append(b)

            # --------------------------------------------------------

            # 4 cari tanggal bulan tahun regex (tahun)
            regex = r"(?:(?:18|19|20|21)[0-9]{2})"
            cari = Regex.cari_regex(regex, text)

            # 5 Kumpul semua jawaban
            for b in cari:
                kumpulan_tahun.append(b)
            # --------------------------------------------------------

            # 4 cari tanggal bulan tahun regex (tanggal bulan tahun)
            # regex = r"[\d]{1,2} [ADFJMNOS]\w* [\d]{4}"
            regex = r"[\d]{1,2} (?:Januari|januari|Febuari|febuari|Maret|maret|April|april|Mei|mei|Juni|juni|Juli|juli|Agustus|agustus|September|september|Oktober|oktober|November|november|Desember|desember) [\d]{4}"
            cari = Regex.cari_regex(regex, text)

            # 5 Kumpul semua jawaban
            for b in cari:
                kumpulan_tanggal_bulan_tahun.append(b)


        # print(cari)

        # print('batas cari -----------------------------------------------')

        # print(kumpulan_tanggal_bulan_tahun)


        # print('batas ----------------------------------------------')

        jawaban_seluruh = kumpulan_tanggal_bulan_tahun
        if jawaban_seluruh == "":
            jawaban_seluruh = kumpulan_tanggal_bulan
            if jawaban_seluruh == "":
                jawaban_seluruh = kumpulan_bulan_tahun
                if jawaban_seluruh == "":
                    jawaban_seluruh = kumpulan_bulan
                    if jawaban_seluruh == "":
                        jawaban_seluruh = kumpulan_tanggal

        # batasi hanya 5 jawaban teratas
        jawaban_pertanyaan_lima = (Count.most_frequent_lima(kumpulan_tanggal_bulan_tahun))
        if jawaban_pertanyaan_lima =="":
            jawaban_pertanyaan_lima = (Count.most_frequent_lima(kumpulan_tanggal_bulan))
            if jawaban_pertanyaan_lima == "":
                jawaban_pertanyaan_lima = (Count.most_frequent_lima(kumpulan_bulan_tahun))
                if jawaban_pertanyaan_lima == "":
                    jawaban_pertanyaan_lima = (Count.most_frequent_lima(kumpulan_bulan))
                    if jawaban_pertanyaan_lima == "":
                        jawaban_pertanyaan_lima = (Count.most_frequent_lima(kumpulan_tanggal))

        # top_answer = Counter(kumpulan_tanggal_bulan_tahun).most_common(5)
        # for tanggal, jumlah in jawaban_pertanyaan_lima:
        #     # print("{tanggal} ({jumlah})".format(tanggal = tanggal, jumlah = jumlah))
        #     print("{tanggal}".format(tanggal=tanggal))
        # print(jawaban_pertanyaan_lima)
        # --------------------------------------------------------

        # open the file in the write mode
        f = open('top_answer.csv', 'w')
        x = open('text.csv', 'w')

        # create the csv writer
        # writer = csv.writer(f, delimiter=";")

        # write a row to the csv file
        # seluruh dokumen tanpa filter: writer.writerow(kumpulan_tanggal_bulan_tahun)
        # sebaris tanpa enter

        # pakai jumlah
        for tanggal, jumlah in jawaban_pertanyaan_lima:
            f.write(str(tanggal))
            f.write('; ')

        for tanggal in jawaban_seluruh:
            x.write(str(tanggal))
            x.write('; ')

        # tidak pakai jumlah
        # for tanggal, jumlah in top_answer:
        #     f.write(str(tanggal))
        #     f.write('\n')

        # close the file
        f.close()

        # --------------------------------------------------------

        # 6 & 7 (Menghitung kata terbanyak & Ambil ranking teratas)
        # print(Count.Count(kumpulan_tanggal))
        # print(Count.Count(kumpulan_tanggal_bulan))
        # print(Count.Count(kumpulan_tahun))
        # print(Count.Count(kumpulan_bulan))
        # print(Count.Count(kumpulan_bulan_tahun))
        # print(Count.Count(kumpulan_tanggal_bulan_tahun))

    # --------------------------------------------------------

        # --------------------------------------------------------

        # 8 (Gabungan semuanya)
        # print(kumpulan_tanggal)
        # print(kumpulan_tanggal_bulan)
        # print(kumpulan_tahun)
        # print(kumpulan_bulan)
        # print(kumpulan_bulan_tahun)
        # print(kumpulan_tanggal_bulan_tahun)

        # jawaban_pertanyaan = str(Count.Count(kumpulan_tanggal_bulan_tahun))

        #hanya tampilkan tanggal bulan tahun
        # jawaban_pertanyaan = str(Count.Count(kumpulan_tanggal)) + "\n" + str(Count.Count(kumpulan_tanggal_bulan)) + "\n" + str(Count.Count(kumpulan_tahun)) + "\n" + str(Count.Count(kumpulan_bulan)) + "\n" + str(Count.Count(kumpulan_bulan_tahun)) + "\n" + str(Count.Count(kumpulan_tanggal_bulan_tahun))

        jawaban_pertanyaan = str(Count.most_frequent(kumpulan_tanggal_bulan_tahun))
        if jawaban_pertanyaan =="":
            jawaban_pertanyaan = str(Count.most_frequent(kumpulan_tanggal_bulan))
            if jawaban_pertanyaan == "":
                jawaban_pertanyaan = str(Count.most_frequent(kumpulan_bulan_tahun))
                if jawaban_pertanyaan == "":
                    jawaban_pertanyaan = str(Count.most_frequent(kumpulan_bulan))
                    if jawaban_pertanyaan == "":
                        jawaban_pertanyaan = str(Count.most_frequent(kumpulan_tanggal))



        return (jawaban_pertanyaan)






