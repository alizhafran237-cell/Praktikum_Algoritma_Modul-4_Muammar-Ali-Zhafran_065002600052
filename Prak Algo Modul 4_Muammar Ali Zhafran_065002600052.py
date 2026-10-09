for i in range(7, 1, -1):
    print(str(i) * i)
    
bulan = int(input("Masukkan bulan (1-12): "))
tahun = int(input("Masukkan tahun: "))

while bulan < 1 or bulan > 12:
    bulan = int(input("Bulan tidak valid, masukkan bulan (1-12): "))

if bulan == 2:
    if tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0):
        hari = 29
    else:
        hari = 28
elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
    hari = 30
else:
    hari = 31

print("Jumlah hari:", hari)