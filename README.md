# Tugas 2 PBP

Link hasil deploy aplikasi : https://tugas-pbp.adaptable.app/

## Step by Step implementasi

## Request-Response Django Lifecycle

<img width="567" alt="Screenshot 2023-09-08 at 10 08 20 PM" src="https://github.com/michelleangelicas/TugasPBP/assets/124910033/9225c6db-cccd-4eaa-880d-067c1921ed76">

Ketika seorang user atau klien mengakses server melalui URL atau form, Django akan membandingkan URL yang diminta dengan URL yang telah ditentukan dalam file urls.py. 
Setiap URL akan dihubungkan ke fungsi khusus dalam file views.py, yang akan memicu fungsi view. 
Fungsi view ini akan berinteraksi dengan database melalui objek dalam models.py. 
Setelah itu, fungsi view akan menghasilkan respons dalam bentuk HTML yang akan dirender oleh user atau klien melalui template.


## Alasan Menggunakan Lingkungan Virtual di Django

Virtual environment adalah area terisolasi yang digunakan untuk menyimpan library dan dependencies. Karena setiap proyek membutuhkan packages Python pihak ketiga yang berbeda, memiliki semua package di satu environment bisa menimbulkan konflik. Oleh karena itu, saat memulai proyek baru, penting untuk membuat virtual environment yang baru untuk proyek tersebut dengan dependencies dan versi yang spesifik untuk sebuah proyek.


## Membuat Proyek Django Tanpa Lingkungan Virtual

Sebenarnya, membangun proyek Django tanpa virtual environment adalah hal yang mungkin. Tujuan dari virtual environment adalah untuk memisahkan dan mengatur dependencies dan versi yang dibutuhkan oleh tiap proyek, agar tidak mengganggu proyek atau sistem lain. Jika aplikasi yang akan dikembangkan sederhana dan hanya untuk keperluan pribadi dalam jangka waktu yang singkat, virtual environment mungkin tidak terlalu dibutuhkan.


## Definisi MVC, MVT, MVVM dan perbedaan dari ketiganya

### MVC (Model-View-Controller)

Komponen:
* Model: Berhubungan dengan semua data, logika bisnis, dan aturan dari aplikasi.
* View: Bertanggung jawab atas tampilan, yaitu apa yang dilihat oleh pengguna.
* Controller: Bertindak sebagai perantara antara Model dan View. Mengendalikan aliran data dan logika.

Cara Bekerja:
1. Pengguna berinteraksi dengan View.
2. Controller memproses interaksi tersebut.
3. Controller meminta update dari Model, jika diperlukan.
4. Model memperbarui View.
5. Pengguna melihat perubahan pada View.

Contoh Penggunaan:
Aplikasi web dengan framework seperti Ruby on Rails, Django (juga mendukung MVT), dan ASP.NET MVC.


### MVT (Model-View-Template)

Komponen:
* Model: Sama seperti dalam MVC, berhubungan dengan data dan logika bisnis.
* View: Bertindak lebih seperti Controller dalam MVC. Mengendalikan logika yang menentukan apa yang harus ditampilkan.
* Template: Ini adalah apa yang dilihat pengguna (mirip dengan View dalam MVC).

Cara Bekerja:
1. Pengguna berinteraksi dengan Template.
2. View memproses interaksi tersebut.
3. View meminta update dari Model, jika diperlukan.
4. Model memperbarui Template.
5. Pengguna melihat perubahan pada Template.

Contoh Penggunaan:
Framework Django di Python.


### MVVM (Model-View-ViewModel)

Komponen:
* Model: Mirip dengan Model dalam MVC dan MVT.
* View: Bertanggung jawab atas tampilan, tetapi tidak mengetahui logika bisnis dan data apa yang akan ditampilkan.
* ViewModel: Bertindak sebagai perantara. Ia memiliki referensi ke Model dan View tetapi memungkinkan keduanya tetap terpisah.

Cara Bekerja:
1. View menghubungkan ke ViewModel, biasanya melalui data binding.
2. ViewModel meminta update dari Model.
3. Model memberikan data yang diperlukan ke ViewModel.
4. ViewModel memperbarui View melalui data binding.
5. Pengguna melihat perubahan pada View.

Contoh Penggunaan:
Aplikasi berbasis XAML seperti WPF, Xamarin, atau aplikasi Angular dan React dengan logika bisnis yang kompleks.


### Perbedaan Utama
* Aliran Kontrol: MVC dan MVT biasanya digunakan pada aplikasi yang aliran kontrolnya diatur oleh server (server-side), sedangkan MVVM sering digunakan di aplikasi klien (client-side) dengan data-binding dua arah.
* Kompleksitas: MVVM biasanya lebih kompleks dibandingkan MVC dan MVT tetapi memudahkan dalam hal testing dan pemisahan tugas.
* Penerapan: MVC dan MVT sering ditemukan di aplikasi web. MVVM lebih sering digunakan pada aplikasi desktop atau mobile, meskipun juga dapat digunakan pada aplikasi web modern.
* Fokus: MVC dan MVT biasanya lebih fokus pada tampilan dan logika bisnis yang ada di server, sedangkan MVVM memungkinkan Anda untuk memisahkan UI dan logika bisnis dengan lebih efektif, terutama di sisi klien.


