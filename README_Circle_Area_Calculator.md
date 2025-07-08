# Circle Area Calculator in Python

Program ini digunakan untuk menghitung luas lingkaran berdasarkan nilai jari-jari yang diberikan oleh pengguna. Pengguna juga dapat memilih nilai konstanta π (pi) yang digunakan dalam perhitungan.

## Bahasa dan Versi Python
Program ditulis menggunakan bahasa Python, dan dapat dijalankan minimal pada versi Python 3.x.

## Cara Penggunaan

### Input yang Dibutuhkan
- Pilihan nilai π (pi):
  - A untuk 3.14
  - B untuk 22/7
- Nilai jari-jari (`r`) lingkaran dalam bentuk bilangan desimal atau bulat

### Output yang Dihasilkan
- Luas lingkaran yang dihitung dengan rumus `pi * r * r`
- Hasil akan dibulatkan ke dua angka di belakang koma

### Contoh Output Program
```
Pilih pi
A.3.14
B.22/7
Masukan Pilihan: A
Masukan Jari-Jari: 7
Jadi Hasilnya Adalah 153.86 
```

## Penjelasan Fungsi Utama
Program ini menggunakan fungsi utama bernama `luas_lingkaran`, yang menerima dua parameter:
- `pi`: nilai konstanta π (pi)
- `r`: jari-jari lingkaran

Fungsi ini mengembalikan hasil perkalian `pi * r * r` sebagai luas lingkaran.

```python
def luas_lingkaran(pi:float, r:float) -> float :
    return pi * r * r
```

## Author
Goodwill Hakim  
[LinkedIn - Goodwill Hakim](https://www.linkedin.com/in/goodwill-hakim-438b88371)
