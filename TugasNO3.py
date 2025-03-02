nama = str(input("Masukkan nama: "))
nim = str(input("Masukkan NIM: "))
res = str(input("Masukkan resolusi tahun ini: "))

with open('readme.txt', 'w') as y:
    y.write(f"Nama: {nama}\n")
    y.write(f"NIM: {nim}\n")
    y.write(f"Resolusi: {res}\n")

for i in range(jumlah_siswa):
    nama_siswa = input(f"Masukkan nama siswa ke-{i + 1}: ")
    nilai = int(input(f"Masukkan nilai {nama_siswa}: "))
    inputan[nama_siswa] = nilai

print(inputan)