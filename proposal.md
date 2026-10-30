# PROPOSAL PROYEK INDIVIDU PERTEMUAN 14
# KALKULATOR GEOMETRI

## Identitas

- **Nama:** Rizki Ramadan
- **NIM:** 2225250024
- **Kelas:** 3F
- **Program Studi:** Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman

## 1. Latar Belakang

Dalam pembelajaran matematika, materi geometri khususnya bangun datar sering melibatkan perhitungan luas dan keliling. Setiap bangun datar memiliki rumus yang berbeda sehingga terkadang pengguna harus mengingat dan menghitungnya secara manual.

Berdasarkan hal tersebut, saya merancang program Kalkulator Geometri sederhana menggunakan bahasa pemrograman Python. Program ini dibuat untuk membantu pengguna menghitung luas dan keliling beberapa bangun datar melalui pilihan menu yang tersedia.

## 2. Pengguna dan Tujuan Program

**Pengguna:**

Siswa atau mahasiswa yang sedang mempelajari materi geometri, khususnya bangun datar.

**Tujuan program:**

1. Membantu pengguna menghitung luas dan keliling bangun datar.
2. Mempermudah proses perhitungan menggunakan program sederhana.
3. Mengurangi kesalahan dalam perhitungan manual.
4. Menerapkan materi algoritma dan pemrograman Python dalam permasalahan matematika.

## 3. Ruang Lingkup Proyek

Program ini dibatasi pada perhitungan empat jenis bangun datar, yaitu:

1. Persegi.
2. Persegi panjang.
3. Segitiga.
4. Lingkaran.

Fitur yang akan dibuat meliputi:

1. Menampilkan menu pilihan bangun datar.
2. Menerima input ukuran dari pengguna.
3. Menghitung luas dan keliling bangun datar.
4. Memeriksa validitas nilai yang dimasukkan.
5. Menampilkan hasil perhitungan.
6. Memberikan pilihan untuk menghitung kembali atau keluar dari program.

Program dijalankan melalui terminal atau console menggunakan Python. Proyek ini tidak mencakup pembuatan GUI, website, maupun penggunaan database.

## 4. Kebutuhan Program

### A. Kebutuhan Fungsional

1. Program dapat menampilkan pilihan bangun datar.
2. Program dapat menerima ukuran sesuai bangun datar yang dipilih.
3. Program dapat menghitung luas dan keliling persegi, persegi panjang, segitiga, dan lingkaran.
4. Program dapat memeriksa input agar tidak menerima ukuran nol atau negatif.
5. Program dapat memeriksa syarat panjang sisi segitiga.
6. Program dapat menampilkan hasil perhitungan.
7. Program dapat mengulang proses perhitungan sesuai pilihan pengguna.

### B. Kebutuhan Nonfungsional

1. Program dapat dijalankan melalui terminal menggunakan Python.
2. Tampilan program dibuat sederhana dan mudah dipahami.
3. Nama variabel dan fungsi disesuaikan dengan kegunaannya.
4. Program memberikan pesan kesalahan apabila input tidak valid.
5. Program dapat diuji menggunakan beberapa test case.

## 5. IPO (Input, Process, Output)

| Input | Process | Output |
|---|---|---|
| Pilihan bangun datar | Memeriksa pilihan pengguna | Nama bangun datar |
| Panjang sisi persegi | Menghitung luas dan keliling | Luas dan keliling persegi |
| Panjang dan lebar | Menghitung luas dan keliling | Luas dan keliling persegi panjang |
| Tiga sisi segitiga | Memeriksa syarat segitiga dan menghitung menggunakan rumus Heron | Luas dan keliling segitiga |
| Jari-jari lingkaran | Menghitung luas dan keliling menggunakan π | Luas dan keliling lingkaran |
| Pilihan untuk menghitung kembali | Memeriksa pilihan pengguna | Program mengulang atau berhenti |

## 6. Algoritma dan Pseudocode

### A. Algoritma

1. Mulai program.
2. Tampilkan judul dan menu kalkulator geometri.
3. Pengguna memilih jenis bangun datar.
4. Program meminta ukuran sesuai bangun datar yang dipilih.
5. Program memeriksa apakah input valid.
6. Jika input valid, program menghitung luas dan keliling.
7. Jika input tidak valid, program menampilkan pesan kesalahan.
8. Program menampilkan hasil perhitungan.
9. Program menanyakan apakah pengguna ingin menghitung kembali.
10. Jika pengguna memilih ya, program kembali ke menu.
11. Jika pengguna memilih tidak, program selesai.

### B. Pseudocode

```text
MULAI

ULANGI
    Tampilkan judul program
    Tampilkan menu bangun datar
    Baca pilihan pengguna

    JIKA pilihan = 1
        Baca sisi persegi
        Periksa validitas sisi
        Hitung luas dan keliling persegi

    JIKA pilihan = 2
        Baca panjang dan lebar
        Periksa validitas ukuran
        Hitung luas dan keliling persegi panjang

    JIKA pilihan = 3
        Baca sisi A, sisi B, dan sisi C
        Periksa validitas sisi
        Periksa syarat segitiga
        Hitung keliling dan luas menggunakan rumus Heron

    JIKA pilihan = 4
        Baca jari-jari lingkaran
        Periksa validitas jari-jari
        Hitung luas dan keliling lingkaran

    Tampilkan hasil perhitungan atau pesan kesalahan
    Tanyakan apakah ingin menghitung kembali

SAMPAI pengguna memilih keluar

SELESAI
```

## 7. Struktur Program dan Modularisasi

Program akan dibagi menjadi beberapa fungsi agar setiap bagian memiliki tugas masing-masing dan lebih mudah diperiksa apabila terjadi kesalahan.

| Nama Fungsi | Kegunaan |
|---|---|
| `tampilkan_judul()` | Menampilkan judul program |
| `tampilkan_menu()` | Menampilkan pilihan bangun datar |
| `validasi_angka()` | Memeriksa input angka |
| `hitung_persegi()` | Menghitung luas dan keliling persegi |
| `hitung_persegi_panjang()` | Menghitung luas dan keliling persegi panjang |
| `hitung_segitiga()` | Menghitung luas dan keliling segitiga |
| `hitung_lingkaran()` | Menghitung luas dan keliling lingkaran |
| `main()` | Mengatur jalannya program |

### Rencana Struktur Folder

```text
kalkulator-geometri-2225250024/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── data/
│   └── nilai_contoh.txt
│
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
│
├── tests/
│   └── test_case.md
│
└── output/
    └── .gitkeep
```

## 8. Struktur Data

Struktur data yang direncanakan dalam program ini adalah:

1. **String**, digunakan untuk menyimpan pilihan dan nama bangun datar.
2. **Float**, digunakan untuk menyimpan ukuran bangun datar dan hasil perhitungan.
3. **Dictionary**, digunakan untuk menyimpan hasil perhitungan berupa nama bangun datar, luas, dan keliling.
4. **List**, digunakan untuk menyimpan pilihan menu bangun datar.

Contoh penggunaan dictionary:

```python
hasil = {
    "bangun_datar": "Persegi",
    "luas": 25,
    "keliling": 20
}
```

Struktur data tersebut dipilih karena sesuai dengan kebutuhan program yang sederhana dan tidak membutuhkan penyimpanan data yang kompleks.

## 9. Test Case

Pengujian dilakukan menggunakan tiga kategori, yaitu normal, boundary, dan invalid.

| Kode | Jenis Pengujian | Input | Hasil yang Diharapkan |
|---|---|---|---|
| TC01 | Normal | Persegi, sisi 5 | Luas = 25 dan keliling = 20 |
| TC02 | Normal | Persegi panjang, panjang 6 dan lebar 4 | Luas = 24 dan keliling = 20 |
| TC03 | Normal | Segitiga, sisi 3, 4, dan 5 | Luas = 6 dan keliling = 12 |
| TC04 | Normal | Lingkaran, jari-jari 7 | Luas = 153,86 dan keliling = 43,96 |
| TC05 | Boundary | Persegi, sisi 0 | Input ditolak karena ukuran harus lebih dari 0 |
| TC06 | Invalid | Lingkaran, jari-jari -5 | Input ditolak karena jari-jari tidak valid |
| TC07 | Invalid | Segitiga, sisi 1, 2, dan 3 | Input ditolak karena tidak memenuhi syarat segitiga |
| TC08 | Invalid | Ukuran bangun datar dimasukkan berupa huruf | Program menampilkan pesan kesalahan |

Keterangan: Perhitungan lingkaran menggunakan nilai π = 3,14.

## 10. Pembagian Tugas

Proyek ini dikerjakan secara individu sehingga seluruh proses pengerjaan dilakukan oleh satu orang.

| Nama | Tugas dan Tanggung Jawab |
|---|---|
| Rizki Ramadan | Menentukan ide proyek, menyusun rancangan, membuat algoritma, menulis kode program, melakukan pengujian, memperbaiki kesalahan, membuat dokumentasi, dan mengelola repository GitHub. |

## 11. Jadwal Pengerjaan

| Waktu | Kegiatan |
|---|---|
| Pertemuan 14 | Menentukan masalah, menyusun proposal, membuat IPO, pseudocode, struktur program, dan test case |
| Setelah Pertemuan 14 | Membuat struktur folder dan mulai menulis kode program |
| Pertemuan 15 | Melanjutkan program, melakukan pengujian, memperbaiki kesalahan, dan melengkapi dokumentasi |
| Pertemuan 16 | Menyesuaikan dengan arahan dosen apabila terdapat kegiatan presentasi atau evaluasi lanjutan |

## 12. GitHub Repository

Repository GitHub direncanakan menggunakan nama:

`kalkulator-geometri-2225250024`

Repository ini digunakan untuk menyimpan seluruh file proyek, mulai dari proposal, kode program, test case, hingga dokumentasi. Setiap perubahan akan dicatat menggunakan commit dengan pesan yang sesuai dengan pekerjaan yang dilakukan.

Contoh commit:

```bash
git add README.md proposal.md tests/
git commit -m "docs: menambahkan rancangan proposal dan test case proyek"
git push
```

**Link Repository:**  
(Diisi setelah repository GitHub dibuat)

## 13. Kesimpulan

Proyek Kalkulator Geometri merupakan program sederhana berbasis Python yang dirancang untuk membantu menghitung luas dan keliling beberapa bangun datar. Program ini memiliki empat pilihan bangun datar dengan fitur validasi input dan pengulangan perhitungan.

Dengan ruang lingkup yang telah ditentukan, proyek ini diharapkan dapat diselesaikan secara individu sesuai waktu yang tersedia. Rancangan ini akan menjadi pedoman dalam proses pembuatan, pengujian, dan dokumentasi program pada pertemuan berikutnya.