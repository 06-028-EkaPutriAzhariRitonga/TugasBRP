def segitiga_sama_sisi(tinggi):
    for i in range(1, tinggi + 1):
        # Menampilkan spasi
        print(' ' * (tinggi - i), end='')
        # Menampilkan bintang
        print('*' * (2 * i - 1))

# Meminta pengguna untuk memasukkan tinggi segitiga
try:
    tinggi = int(input("Input tinggi segitiga: "))
    if tinggi > 0:
        segitiga_sama_sisi(tinggi)
    else:
        print("Tinggi harus berupa bilangan bulat positif.")
except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat.")