# Modul utilitas untuk Kalkulator Geometri


# Fungsi untuk menampilkan judul program
def tampilkan_judul():
    print("=" * 40)
    print("KALKULATOR GEOMETRI".center(40))
    print("=" * 40)


# Fungsi untuk memvalidasi angka positif
def validasi_angka_positif(nilai):
    return nilai > 0


# Fungsi untuk memvalidasi panjang sisi segitiga
def validasi_segitiga(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False

    return (
        a + b > c
        and a + c > b
        and b + c > a
    )