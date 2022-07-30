from tkinter import *
from Main_process import Main_process

root = Tk()
root.title("Pencarian Jawaban Untuk Pertanyaan Kapan")
root.config()

def perintah():
    # print pertanyaan
    print('pertanyaan : ' + data.get())

    keyword = data.get()
    jawaban = Main_process.do_main_process(keyword)

    # print jawaban
    print('Jawaban yang ditemukan : ' + jawaban)

    print('-------------------------------------------------------')

    answer.config(text="" + jawaban)
    data.delete(0, END)
    return jawaban

def tutup():
   root.quit()

labelPertanyaan = Label( root,
                         text="Masukkan Pertanyaan",
                         font="Helvetica 9",
                         # fg='white',
                         # background="#1D5C63"
                         )
labelPertanyaan.grid(row=1, column=0, pady=5, sticky=W)

data = Entry(font="Normal 13", width=33)
data.grid(row=1, column=1, pady=5, sticky=W)

buttonCari = Button(text="Cari",
                font="Normal 9",
                activebackground="#417D7A",
                width=13,
                command=perintah)
buttonCari.grid(row=1, column=2, pady=5)

labelJawaban = Label( root,
                      text="Jawaban yang Ditemukan",
                      font="Helvetica 9",
                      # fg='white',
                      # background="#1D5C63"
              )
labelJawaban.grid(row=2, column=0, sticky=W)

answer = Label(width=62,
               height=6,
               font="Normal 11",
               # fg='white',
               background="white",
               # background="#1D5C63",
               justify='left',
               borderwidth=1,
               relief='raised'

               )
answer.grid(row=3,
            column=0,
            columnspan=3,
            sticky=W,
            padx=3,
            pady=5
            )

buttonTutup = Button(text="Tutup",
                font="Normal 9",
                activebackground="#1D5C63",
                width=80,
                command=tutup)
buttonTutup.grid(row=4, column=0,columnspan=3, pady=5)

root.mainloop()