from datetime import*
def diffDate(x):
    tgl = x.split("-")
    dateList = []
    for i in tgl:
        dateList.append(int(i))
    ystrdy = date(dateList[0], dateList[1], dateList[2])
    tdy = datetime.date(datetime.now())
    a = ystrdy - tdy
    b = a.days
    return b
try:
    tanggal = input("Masukkan tanggal yang di inginkan dengan format (yyyy-mm-dd): ")
    hasil = diffDate(tanggal)
    print("Selisih tanggal {0} dengan hari ini adalah {1} hari,".format(tanggal, hasil))
except ValueError:
    print("Masukkan tanggal dengan format yang valid")
