import re

#untuk identifikasi jawaban pakai findall
class Regex:
    def cari_regex(regex, text):
        cari = re.findall(regex, text)
        # print(cari)
        return cari