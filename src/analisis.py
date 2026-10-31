

import math

# Nilai pi yang digunakan dalam perhitungan lingkaran
PI = 3.14


# Fungsi untuk menghitung luas dan keliling persegi
def hitung_persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi

    return luas, keliling


# Fungsi untuk menghitung luas dan keliling persegi panjang
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    return luas, keliling


# Fungsi untuk menghitung luas dan keliling segitiga
def hitung_segitiga(a, b, c):
    keliling = a + b + c
    s = keliling / 2

    # Menghitung luas menggunakan rumus Heron
    luas = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return luas, keliling


# Fungsi untuk menghitung luas dan keliling lingkaran
def hitung_lingkaran(jari_jari):
    luas = PI * jari_jari * jari_jari
    keliling = 2 * PI * jari_jari

    return luas, keliling
