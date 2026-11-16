#Perulangan

jumlah = int(input("jumlah mahasiswa : "))
total = 0
for i in range(1, jumlah+ 1):
    nilai = int(input(f"masukkan nilai mahasiswa {i} : "))
    total += nilai
if nilai >= 75:
    print("keterangan : lulus")
else:
    print("keterangan : tidak lulus")

rata_rata = total / jumlah
print("nilai rata-rata :", rata_rata)
