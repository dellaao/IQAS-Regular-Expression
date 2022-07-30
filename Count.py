from collections import Counter
#untuk menghitung data

class Count:

    # dengan jumlah kata
    # def Count(kumpulan):
    #     return Counter(kumpulan).most_common(1)[-1]

    # using most_commont method
    def most_frequent(kumpulan):
        occurence_count = Counter(kumpulan)
        return occurence_count.most_common(1)[0][0]

    # hanya 5 buah
    def most_frequent_lima(kumpulan):
        occurence_count = Counter(kumpulan)
        return occurence_count.most_common(5)