# Test Case Kalkulator Geometri

Pengujian dirancang untuk memastikan program dapat menghitung luas dan keliling dengan benar serta menangani input yang tidak valid.

| Kode | Jenis | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Persegi, sisi 5 | Luas 25, keliling 20 |
| TC02 | Normal | Persegi panjang, 6 dan 4 | Luas 24, keliling 20 |
| TC03 | Normal | Segitiga, 3, 4, 5 | Luas 6, keliling 12 |
| TC04 | Normal | Lingkaran, jari-jari 7 | Luas 153,86, keliling 43,96 |
| TC05 | Boundary | Persegi, sisi 0 | Input ditolak |
| TC06 | Invalid | Lingkaran, jari-jari -5 | Input ditolak |
| TC07 | Invalid | Segitiga, sisi 1, 2, 3 | Input ditolak |
| TC08 | Invalid | Ukuran dimasukkan berupa huruf | Program menampilkan pesan kesalahan |

## Keterangan

- Normal: menguji input yang benar.
- Boundary: menguji nilai pada batas yang tidak diperbolehkan.
- Invalid: menguji input yang tidak sesuai.

## Status Pengujian

Seluruh test case di atas masih berupa rancangan pengujian, hasil aktual akan dicatat setelah program selesai dibuat dan dijalankan.

**Pertemuan 15**
# TEST CASE KALKULATOR GEOMETRI

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan seluruh fitur Kalkulator Geometri berjalan sesuai dengan fungsi yang telah dibuat.

## 2. Daftar Pengujian

| No. | Fitur | Input | Hasil yang Diharapkan | Status |
|---|---|---|---|---|
| 1 | Persegi | Sisi = 5 | Luas = 25, Keliling = 20 | Berhasil |
| 2 | Persegi Panjang | Panjang = 6, Lebar = 4 | Luas = 24, Keliling = 20 | Berhasil |
| 3 | Segitiga | Sisi = 3, 4, 5 | Luas = 6, Keliling = 12 | Berhasil |
| 4 | Lingkaran | Jari-jari = 7 | Luas = 153.86, Keliling = 43.96 | Berhasil |
| 5 | Validasi angka negatif | -7 | Program menolak angka | Berhasil |
| 6 | Validasi input huruf | abc | Program menolak input | Berhasil |
| 7 | Validasi segitiga | Sisi = 2, 3, 8 | Program menolak sisi tidak valid | Berhasil |
| 8 | Keluar program | Pilihan = 0 | Program berhenti | Berhasil |

## 3. Kesimpulan Pengujian

Berdasarkan pengujian yang telah dilakukan, seluruh fitur Kalkulator Geometri dapat berjalan sesuai dengan hasil yang diharapkan.

Program mampu menghitung luas dan keliling bangun datar, menerima input pengguna, melakukan validasi input, serta menangani pilihan keluar dari program.

Dengan demikian, program Kalkulator Geometri telah memenuhi pengujian fungsional dasar.