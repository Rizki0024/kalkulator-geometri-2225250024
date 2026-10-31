# Kalkulator Geometri

## Deskripsi Proyek

Kalkulator Geometri merupakan program sederhana menggunakan bahasa Python yang dirancang untuk menghitung luas dan keliling beberapa bangun datar melalui terminal atau console.

## Identitas

- Nama: Rizki Ramadan
- NIM: 2225250024
- Kelas: 3F
- Program Studi: Pendidikan Matematika

## Fitur Program

1. Menghitung luas dan keliling persegi.
2. Menghitung luas dan keliling persegi panjang.
3. Menghitung luas dan keliling segitiga.
4. Menghitung luas dan keliling lingkaran.
5. Melakukan validasi input pengguna.
6. Memberikan pilihan untuk melakukan perhitungan kembali.

## Teknologi

- Bahasa pemrograman: Python.
- Editor: Visual Studio Code.
- Version control: Git dan GitHub.

## Struktur Folder

```text
kalkulator-geometri-2225250024/
├── README.md
├── proposal.md
├── .gitignore
├── data/
├── src/
├── tests/
└── output/
```

## Cara Menjalankan

Program direncanakan dijalankan melalui terminal menggunakan Python.

```bash
python src/main.py
```

## Status Proyek

Saat ini proyek berada pada tahap perancangan. Implementasi dan pengujian program akan dilakukan pada tahap berikutnya.


**Pertemuan 15**
# KALKULATOR GEOMETRI

**Nama:** Rizki Ramadan  
**NIM:** 2225250024  
**Program Studi:** Pendidikan Matematika  
**Kelas:** 3F  
**Mata Kuliah:** Algoritma dan Pemrograman

## Deskripsi Program

Kalkulator Geometri merupakan program berbasis Python yang digunakan untuk menghitung luas dan keliling beberapa bangun datar.

Program menyediakan empat pilihan bangun datar, yaitu:
1. Persegi
2. Persegi panjang
3. Segitiga
4. Lingkaran

Program menggunakan pendekatan modular dengan memisahkan fungsi perhitungan, input dan output, utilitas, serta program utama ke dalam beberapa file Python.

## Fitur Program

- Menghitung luas dan keliling persegi.
- Menghitung luas dan keliling persegi panjang.
- Menghitung luas dan keliling segitiga menggunakan rumus Heron.
- Menghitung luas dan keliling lingkaran.
- Memvalidasi input angka positif.
- Memvalidasi panjang sisi segitiga.
- Menangani input yang bukan angka.
- Menyediakan pilihan untuk keluar dari program.

## Struktur Folder

```text
kalkulator-geometri-2225250024/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
└── output/
    └── .gitkeep
```

## Teknologi yang Digunakan

- Bahasa pemrograman Python.
- Modul `math` dari Python Standard Library.
- Visual Studio Code.
- Git dan GitHub.

## Cara Menjalankan Program

1. Pastikan Python sudah terpasang.
2. Buka folder proyek melalui Visual Studio Code.
3. Buka terminal pada folder utama proyek.
4. Jalankan perintah:

```bash
python src/main.py
```

5. Pilih bangun datar yang ingin dihitung.
6. Masukkan nilai sesuai permintaan program.
7. Program akan menampilkan hasil luas dan keliling.

## Pembagian Modul

| File | Fungsi |
|---|---|
| `main.py` | Mengatur alur utama program dan menu |
| `analisis.py` | Menyediakan fungsi perhitungan geometri |
| `data_io.py` | Mengelola input dan output pengguna |
| `utilitas.py` | Menyediakan fungsi validasi dan judul |

## Pengujian

Pengujian dilakukan terhadap perhitungan empat bangun datar, validasi input, validasi segitiga, serta pilihan keluar program.

Rincian pengujian terdapat pada file `tests/test_case.md`.

## Rumus yang Digunakan

- Persegi: luas = sisi × sisi; keliling = 4 × sisi.
- Persegi panjang: luas = panjang × lebar; keliling = 2 × (panjang + lebar).
- Segitiga: luas menggunakan rumus Heron; keliling = a + b + c.
- Lingkaran: luas = 3,14 × r × r; keliling = 2 × 3,14 × r.

## Kesimpulan

Program Kalkulator Geometri dibuat untuk menerapkan konsep algoritma, fungsi, modularisasi program, input-output, dan validasi data menggunakan Python.