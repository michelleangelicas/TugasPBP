# Tugas 2 PBP

Link hasil deploy aplikasi : https://tugas-pbp.adaptable.app/

## Step by Step implementasi

### Membuat sebuah proyek Django baru & membuat aplikasi dengan nama main pada proyek tersebut.
Buka terminal Linux dan navigasi ke direktori TugasPBP, kemudian aktifkan virtual environment yang telah dibuat sebelumnya dengan menjalankan perintah `source env/bin/activate`.

Setelah environment aktif, jalankan perintah `python manage.py startapp main` untuk membuat aplikasi baru dengan nama "main". Ini akan menghasilkan direktori baru yang berisi semua file dan struktur yang diperlukan untuk aplikasi. Selanjutnya, kita perlu mendaftarkan aplikasi ini ke dalam proyek. Buka file `settings.py` yang berada dalam direktori proyek "inventaris", cari variabel `INSTALLED_APPS` dan tambahkan `'main'` ke dalam daftar aplikasi yang sudah terdaftar. Dengan demikian, aplikasi "main" sekarang sudah terdaftarkan dan siap untuk dikembangkan lebih lanjut.

### Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib
Aplikasi ini memanfaatkan model `Product` yang memiliki field seperti `name`, `amount`, dan `description`. Saya juga telah membuat sebuah template HTML dasar, "main.html", yang akan digunakan untuk menampilkan data dari model ini.

Langkah pertama adalah menambahkan definisi model ke dalam `models.py` di direktori aplikasi "main". Saya telah mendefinisikan kelas `Product` yang mewarisi dari `models.Model`, dan menambahkan field yang sesuai.

Setelah itu, saya menjalankan perintah `python manage.py makemigrations` untuk membuat migrasi model. Migrasi ini adalah sebuah skrip yang Django gunakan untuk menerapkan perubahan pada database. Selanjutnya, saya menerapkan migrasi ini dengan perintah `python manage.py migrate`, yang akan memperbarui struktur database sesuai dengan model yang telah saya definisikan.

Template "main.html" saya saat ini menampilkan data statis, tetapi setelah saya melalui tutorial lebih lanjut, template ini akan diisi dengan data dinamis dari model `Product`.

### Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
Saya telah membuat sebuah view bernama `show_main`. View ini mendefinisikan data dalam bentuk dictionary dan me-render template "main.html" dengan data tersebut. Saya menggunakan fungsi `render` dari modul `django.shortcuts` untuk menggabungkan data dari view dengan template HTML. Saya juga menambahkan data seperti name, amount, dan description. Ini memungkinkan saya untuk membuat tampilan web yang dinamis, di mana data dari view ditampilkan dalam template HTML.

### Melakukan routing pada proyek agar dapat menjalankan aplikasi main & membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
Saya telah mengonfigurasi routing URL melalui dua berkas `urls.py`—satu di tingkat aplikasi (`main`) dan satu lagi di tingkat proyek (`TugasPBP`). Di tingkat aplikasi, saya mendefinisikan URL dengan memanfaatkan fungsi `show_main` dari modul `main.views` dan mengaturnya sebagai tampilan utama. Di tingkat proyek, saya memanfaatkan fungsi `include` dari `django.urls` untuk mengintegrasikan URL aplikasi `main` ke dalam proyek. Akhirnya, saya menjalankan server dan mengakses halaman melalui peramban dengan alamat "http://localhost:8000/main/". Ini menunjukkan implementasi sukses dari routing URL di Django, memungkinkan tampilan yang saya buat di aplikasi `main` untuk diakses dan ditampilkan pada peramban web.

### Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Tahap deployment dilakukan dengan menghubungkan app Adaptable dengan repository yang terdapat pada github. Saya menyesuaikan versi Python dengan spesifikasi aplikasi. Lalu, memsaukkan perintah `python manage.py migrate && gunicorn TugasPBP.wsgi`. Lalu, saya mencentang bagian `HTTP Listener on PORT` dan meng-klik `Deploy App`.


## Request-Response Django Lifecycle

<img width="617" alt="Screenshot 2023-09-12 at 2 09 26 PM" src="https://github.com/michelleangelicas/TugasPBP/assets/124910033/66a3c3cf-34b3-4146-8d6b-2afeb2aa6639">

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

