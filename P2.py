from datetime import*
import os
if(os.path.exists("Data Pinjam.txt")):
   fileMode = "a"
else:
    fileMode = "w"
file = open("Data Pinjam.txt", fileMode)
while True:
    kode = input("Masukkan Kode Member : ")
    nama = input("Masukkan Nama Member : ")
    judul = input("Masukkan Judul Buku  : ")
    tglpnjm = datetime.date(datetime.now())
    tglkmbl = tglpnjm + timedelta(days = 7)
    file.write(kode + "|" + nama + "|" + judul + "|" + str(tglpnjm) + "|" + str(tglkmbl) + "\n")    
    tambah = input("\nMau lagi (y/n) : ")
    ("\n")
    if tambah == "y":
        True
    elif tambah == "n":
        break
    else:
        print("Input tidak valid")
        break
file.close()
