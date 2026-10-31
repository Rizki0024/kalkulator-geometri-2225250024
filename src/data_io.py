# Modul untuk menangani input dan output Kalkulator Geometri

from utilitas import validasi_angka_positif


# Fungsi untuk menampilkan menu pilihan
def tampilkan_menu():
    print("\nPilih bangun datar:")
    print("1. Persegi")
    print("2. Persegi panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("0. Keluar")


# Fungsi untuk menerima input angka positif
def input_angka_positif(pesan):
    while True:
        try:
            nilai = float(input(pesan))

            if validasi_angka_positif(nilai):
                return nilai

            print("Angka harus lebih besar dari nol!")

        except ValueError:
            print("Input tidak valid. Masukkan angka!")


# Fungsi untuk menampilkan hasil perhitungan
def tampilkan_hasil(luas, keliling):
    print("\n" + "-" * 30)
    print("HASIL PERHITUNGAN".center(30))
    print("-" * 30)
    print(f"Luas     : {luas:.2f}")
    print(f"Keliling : {keliling:.2f}")
    print("-" * 30)