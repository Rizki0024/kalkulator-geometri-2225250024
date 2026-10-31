# Program utama Kalkulator Geometri

from analisis import (
    hitung_persegi,
    hitung_persegi_panjang,
    hitung_segitiga,
    hitung_lingkaran
)

from data_io import (
    tampilkan_menu,
    input_angka_positif,
    tampilkan_hasil
)

from utilitas import (
    tampilkan_judul,
    validasi_segitiga
)


# Fungsi utama program
def main():
    tampilkan_judul()

    while True:
        tampilkan_menu()

        pilihan = input("Masukkan pilihan (0-4): ")

        if pilihan == "1":
            sisi = input_angka_positif(
                "Masukkan panjang sisi: "
            )

            luas, keliling = hitung_persegi(sisi)

        elif pilihan == "2":
            panjang = input_angka_positif(
                "Masukkan panjang: "
            )

            lebar = input_angka_positif(
                "Masukkan lebar: "
            )

            luas, keliling = hitung_persegi_panjang(
                panjang, lebar
            )

        elif pilihan == "3":
            while True:
                a = input_angka_positif(
                    "Masukkan panjang sisi a: "
                )

                b = input_angka_positif(
                    "Masukkan panjang sisi b: "
                )

                c = input_angka_positif(
                    "Masukkan panjang sisi c: "
                )

                if validasi_segitiga(a, b, c):
                    break

                print(
                    "Sisi tersebut tidak dapat membentuk segitiga!"
                )
                print("Silakan masukkan ketiga sisi kembali.")

            luas, keliling = hitung_segitiga(a, b, c)

        elif pilihan == "4":
            jari_jari = input_angka_positif(
                "Masukkan jari-jari lingkaran: "
            )

            luas, keliling = hitung_lingkaran(jari_jari)

        elif pilihan == "0":
            print("\nProgram selesai.")
            break

        else:
            print("Pilihan tidak valid. Pilih angka 0 sampai 4.")
            continue

        tampilkan_hasil(luas, keliling)


# Menjalankan program utama
if __name__ == "__main__":
    main()