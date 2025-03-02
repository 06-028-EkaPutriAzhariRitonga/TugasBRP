n = int(input("Input Jumlah Siswa: "))
inputan = {}

for i in range(n):
    nama = str(input(f"Masukkan nama siswa ke-{i + 1}: "))
    nilai = int(input(f"Masukkan nilai {nama}: "))
    inputan[nama] = nilai

print(inputan)