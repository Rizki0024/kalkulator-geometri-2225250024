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