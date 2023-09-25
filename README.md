<details>
<summary>Tugas 3</summary>

# Tugas 3 PBP

## Apa perbedaan antara form POST dan form GET dalam Django?

Dalam framework web Django, metode GET dan POST digunakan dalam form untuk mengirim data dari klien ke server.

GET: Metode ini biasanya digunakan untuk mengambil data dari server. Dalam konteks form, GET menyertakan semua data formulir sebagai parameter dalam URL. Ini mempermudah pembagian link tetapi juga membatasi jumlah data yang bisa dikirim (karena batasan panjang URL). GET juga kurang aman karena semua data terlihat di URL dan bisa disimpan dalam log browser atau server.

POST: Metode ini digunakan untuk mengirimkan data yang tidak harus ditampilkan dalam URL, seperti kata sandi atau informasi pribadi lainnya. Data dikirim dalam badan permintaan, tidak dalam URL. Ini lebih aman dan bisa menampung lebih banyak data.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
HTML, atau HyperText Markup Language, adalah bahasa markup yang fokus pada tampilan informasi, terutama untuk tujuan web. Sementara itu, JSON, singkatan dari JavaScript Object Notation, adalah sebuah format data berdasarkan JavaScript yang menyajikan data dalam pasangan kunci dan nilai. JSON efisien untuk penyimpanan dan transfer data tetapi kurang mudah dibaca oleh manusia jika dibandingkan dengan XML. Di sisi lain, XML, atau Extensible Markup Language, adalah bahasa markup yang mempermudah proses penyimpanan dan transmisi data antara server. Dibandingkan dengan JSON, XML lebih mudah dibaca oleh manusia tetapi kurang efisien dalam pertukaran data.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON (JavaScript Object Notation) sering digunakan dalam aplikasi web modern untuk berbagai alasan:
* Kecepatan: JSON ringan dan memungkinkan pertukaran data yang cepat antara klien dan server.
* Struktur Data: JSON mendukung tipe data seperti array dan objek bersarang, yang memungkinkannya untuk merepresentasikan data yang kompleks.
* Kompatibilitas: Hampir semua bahasa pemrograman modern memiliki library untuk mem-parsing dan menghasilkan JSON.
* Readability: Meskipun lebih sulit dibaca dibandingkan XML, JSON relatif mudah dibaca dan ditulis oleh manusia jika dibandingkan dengan format data biner.
* Native JavaScript Support: Karena JSON adalah bagian dari JavaScript, ia dapat di-parse dan digenerate dengan mudah di sisi klien tanpa memerlukan library tambahan.
* Standardisasi: JSON adalah sebuah standar yang diakui secara luas untuk pertukaran data, yang membuatnya menjadi pilihan yang baik untuk integrasi antar sistem yang berbeda.
Karena alasan-alasan ini, JSON telah menjadi salah satu format paling populer untuk pertukaran data dalam pengembangan web modern.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
1. Mengimplementasikan skeleton sebagai kerangka Views dengan menambahkan folder templates dalam root folder dan membuat base.html di dalamnya, menambahkan beberapa potongan kode pada settings.py, mengubah kode berkas main.html dengan menambahkan `{% extends 'base.html' %}`
2. Membuat form input data dan tampilan pada HTML. Membuat berkas forms.py yang mempunyai fields name, amount, description. Menambahkan fungsi create_product, show_main. Menambahkan path url path`('create-product', create_product, name='create_product’)`, lalu membuat berkas html baru create_product.html
3. Menjadikan data dalam bentuk XML dan JSON dengan membuat fungsi dan menambahkan path url dalam urlpatterns. 
4. menjadikan data berdasarkan ID dalam bentuk XML, JSON. Menambahkan function `show_xml_by_id` dan `show_json_by_id` di views.py dan menambahkan urlpatterns pada urls.py. 

## Postman
### HTML
<img width="1392" alt="Screenshot 2023-09-18 at 12 07 31 PM" src="https://github.com/michelleangelicas/TugasPBP/assets/124910033/8c10e269-bfd9-4e06-a84e-b6f04b10c914">

### XML
<img width="1392" alt="Screenshot 2023-09-18 at 12 06 32 PM" src="https://github.com/michelleangelicas/TugasPBP/assets/124910033/31fee51b-4488-4ad4-845b-7060725d6c88">

### JSON
<img width="1392" alt="Screenshot 2023-09-18 at 12 07 19 PM" src="https://github.com/michelleangelicas/TugasPBP/assets/124910033/bd8c26e5-7975-43d3-801b-f424b4719962">

### XML by id
<img width="1392" alt="Screenshot 2023-09-18 at 12 08 05 PM" src="https://github.com/michelleangelicas/TugasPBP/assets/124910033/cfa257a5-15c4-4283-ace7-bfd278fd6cec">

### JSON by id
<img width="1392" alt="Screenshot 2023-09-18 at 12 08 16 PM" src="https://github.com/michelleangelicas/TugasPBP/assets/124910033/6e063e35-bbf8-4be5-8dcd-cb13c725a080">

</details>

<details>
<summary>Tugas 4</summary>

# Tugas 4

## Django UserCreationForm
UserCreationForm adalah sebuah form bawaan Django yang digunakan untuk membuat pengguna baru. Form ini sudah termasuk validasi data masukan dan umumnya digunakan bersama dengan `django.contrib.auth.views`, yang menyediakan view untuk proses registrasi pengguna.

### Kelebihan
* Penggunaan yang Mudah: Ini adalah form yang sudah dibuat oleh Django, sehingga pengembang tidak perlu membuat form dari awal.
* Validasi Terintegrasi: Form ini sudah memiliki validasi terintegrasi, sehingga mengurangi risiko error.
* Pengembangan Cepat: Menggunakan komponen bawaan Django seperti UserCreationForm memungkinkan pengembangan aplikasi secara lebih cepat.
* Keamanan: Form ini mengimplementasikan praktik keamanan terbaik, yang melindungi dari serangan umum seperti SQL Injection.

### Kekurangan
* Kustomisasi Terbatas: Karena UserCreationForm adalah form bawaan, mengkustomisasinya bisa lebih sulit dibandingkan dengan membuat form sendiri.
* Kurang Fleksibel: Tidak cocok untuk skenario penggunaan yang membutuhkan logika atau validasi yang lebih kompleks.


## Autentikasi vs Otorisasi di Django
Autentikasi: Proses verifikasi identitas pengguna. Dalam konteks Django, autentikasi sering kali dilakukan dengan memeriksa kombinasi username dan password pengguna, dan framework ini menyediakan back-end autentikasi yang dapat dikustomisasi sesuai kebutuhan.

Otorisasi: Setelah autentikasi berhasil, otorisasi adalah proses pemberian hak akses atau izin kepada pengguna untuk mengakses sumber daya tertentu. Django menyediakan sistem perizinan yang dapat dikustomisasi untuk membatasi akses ke objek dan tipe objek tertentu dalam sistem.

### Mengapa Keduanya Penting?
* Keamanan dan Perlindungan Data: Autentikasi dan otorisasi adalah elemen kunci dalam melindungi data dan sumber daya dari akses yang tidak sah. Autentikasi memastikan bahwa pengguna adalah siapa yang mereka klaim, sedangkan otorisasi memastikan bahwa pengguna hanya dapat mengakses sumber daya yang diizinkan.
* Pemenuhan Kebijakan dan Persyaratan: Banyak aplikasi web perlu mematuhi kebijakan keamanan tertentu atau memenuhi persyaratan hukum tertentu mengenai perlindungan data dan privasi pengguna.
* Manajemen Akses: Sistem yang memiliki pengguna dengan berbagai tingkatan akses, seperti admin, staff, dan pengguna biasa, memerlukan pengelolaan hak akses yang baik untuk memastikan operasional yang lancar dan menghindari penyalahgunaan hak akses.

## Cookies dalam Konteks Aplikasi Web
Cookies adalah potongan data kecil yang disimpan oleh browser web di sisi klien. Cookies digunakan oleh aplikasi web untuk menyimpan informasi tentang pengguna, seperti preferensi pengguna, data sesi, atau lainnya. Dengan menggunakan cookies, aplikasi web dapat "mengingat" pengguna dan menyediakan pengalaman yang lebih kustomisasi dan responsif.

### Django menggunakan cookies untuk mengelola data sesi pengguna
Secara default, Django menggunakan mekanisme cookie berbasis sesi untuk menyimpan ID sesi pengguna. Data sesi itu sendiri disimpan di sisi server. Dengan cara ini, informasi pengguna, seperti data autentikasi, disimpan dengan aman di server, sementara browser hanya menyimpan ID sesi yang unik dan aman. Django mengatur ini secara otomatis dan memungkinkan pengembang untuk memilih penyimpanan sesi yang berbeda jika dibutuhkan.


## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web memiliki potensi risiko, dan tidak sepenuhnya aman secara default. Sebagai developer, ada beberapa langkah yang harus diambil untuk memastikan bahwa cookies seaman mungkin.

### Risiko Potensial
* Intersepsi Cookie: Cookies yang ditransmisikan melalui HTTP (tanpa enkripsi) dapat diintersep dan dibaca oleh pihak ketiga. Penggunaan HTTPS dapat mencegah risiko ini.

* Cross-Site Scripting (XSS): Cookies dapat diakses melalui skrip JavaScript. Jika sebuah situs rentan terhadap serangan XSS, cookies dapat dicuri oleh attacker.

* Cross-Site Request Forgery (CSRF): Cookies otomatis dikirim dengan setiap permintaan ke domain yang mengatur cookie, sehingga dapat digunakan untuk melancarkan serangan CSRF.

* Overwriting Cookies: Cookie dari subdomain dapat menimpa cookie dari domain utama, yang dapat dimanfaatkan untuk serangan.

* Theft and Replay Attacks: Jika cookies dicuri, mereka dapat digunakan untuk mengimpersonasi pengguna yang sah.

### Pengamanan Cookies
* HTTPS dan Secure Attribute: Selalu gunakan HTTPS dan atur Secure attribute pada cookies untuk menghindari intersepsi oleh man-in-the-middle.

* HttpOnly Attribute: Atur attribute HttpOnly pada cookies untuk mencegah akses melalui JavaScript dan mengurangi risiko serangan XSS.

* SameSite Attribute: Gunakan SameSite attribute untuk mencegah cookies dikirimkan dalam permintaan cross-site, yang membantu melindungi terhadap serangan CSRF.

* Domain dan Path Attributes: Tentukan domain dan path cookies secara eksplisit untuk menghindari overwriting dan pengiriman yang tidak diinginkan.

* Masa Berlaku yang Terbatas: Beri cookies masa berlaku yang terbatas untuk mengurangi jangka waktu dimana cookies yang dicuri dapat digunakan.


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

### Membuat fungsi dan form registrasi. 
Pertama, menambahkan fungsi register dengan parameter request. Lalu, membuat berkas register.html dan menambahkan path url ke urlpatterns. 

### Membuat fungsi login
menambahkan fungsi login_user dengan parameter request. Lalu, menambahkan berkas login.html dengan template yang tersedia. Lalu, menambahkan path url ke urlpatterns.

### Membuat fungsi logout
menambahkan fungsi logout_user dan menmbahkan button logout. Lalu, menambahkan path url ke urlpatterns. 

### Merestriksi akses halaman main
menambahkan kode `@login_required(login_url='/login’)`

### Menggunakan data dari cookies
mengganti kode di bawah blok `if user is not none` untuk melihat kapan terakhir kali pengguna melakukan login. Lalu, menambahkan 'last_login' untuk isi context pada fungsi show_main. Lalu, mengubah fungsi logout_user dengan `response.delete_cookie('last_login’)`. Lalu, menambahkan potongan kode di main.html untuk menampilkan data last login.

### Menghubungkan Model Product dengan User
Menambahkan kode ForeignKey. Lalu, mengubah kode pada fungsi create_product pada views.py, dan mengubah fungsi show_main sehingga product menyesuaikan usernya. 

### Menambahkan fungsionalitas menambah dan mengurangi jumlah serta menghapus produk
1. Menambahkan View Fungsi
Tambahkan fungsi di views.py untuk menghandle peningkatan jumlah (increase_amount), pengurangan jumlah (decrease_amount), dan penghapusan produk (delete_product).
2. Meng-update URL Patterns
Tambahkan URL baru di urls.py yang mengarah ke fungsi-fungsi baru yang telah dibuat.
3. Meng-update Template
Tambahkan tautan atau tombol di template HTML (main.html) yang mengarah ke URL baru untuk memanggil fungsi yang sesuai.

</details>