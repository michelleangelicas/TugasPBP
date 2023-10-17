## Link app : [http://michelle-angelica21-tugas.pbp.cs.ui.ac.id/](http://michelle-angelica21-tugas.pbp.cs.ui.ac.id/main/login/)

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
1. Menambahkan View Fungsi.
Tambahkan fungsi di views.py untuk menghandle peningkatan jumlah (increase_amount), pengurangan jumlah (decrease_amount), dan penghapusan produk (delete_product).
2. Meng-update URL Patterns.
Tambahkan URL baru di urls.py yang mengarah ke fungsi-fungsi baru yang telah dibuat.
3. Meng-update Template.
Tambahkan tautan atau tombol di template HTML (main.html) yang mengarah ke URL baru untuk memanggil fungsi yang sesuai.

</details>


<details>
<summary>Tugas 5</summary>

# Tugas 5 PBP

## Manfaat dari Setiap Element Selector
* Type Selector:
    Manfaat: Digunakan untuk memilih dan mengatur gaya untuk semua elemen HTML dari jenis yang sama.
    Waktu yang Tepat: Ketika ingin menerapkan gaya yang sama ke semua elemen dengan tipe tertentu pada halaman web.
* Class Selector:
    Manfaat: Digunakan untuk memilih dan mengatur gaya untuk elemen HTML yang memiliki atribut class tertentu.
    Waktu yang Tepat: Ketika beberapa elemen pada halaman web memerlukan gaya yang sama, atau ketika menggunakan framework CSS seperti Bootstrap.
* ID Selector:
    Manfaat: Digunakan untuk memilih dan mengatur gaya untuk elemen HTML yang memiliki atribut id tertentu.
    Waktu yang Tepat: Ketika perlu mengatur gaya untuk elemen yang unik dalam dokumen.
* Attribute Selector:
    Manfaat: Digunakan untuk memilih elemen berdasarkan keberadaan atau nilai dari atributnya.
    Waktu yang Tepat: Ketika perlu memilih elemen berdasarkan atributnya, seperti memilih input berdasarkan tipe inputnya.
* Descendant Selector:
    Manfaat: Digunakan untuk memilih elemen yang merupakan keturunan dari elemen lain.
    Waktu yang Tepat: Ketika perlu mengatur gaya pada elemen yang berada di dalam elemen lain, seperti mengatur gaya pada paragraf di dalam div.
* Pseudo-class Selector:
    Manfaat: Digunakan untuk mengatur gaya pada elemen dalam keadaan tertentu, seperti :hover, :focus, dll.
    Waktu yang Tepat: Ketika perlu mengatur gaya berdasarkan keadaan elemen seperti ketika mouse berada di atas elemen atau ketika elemen mendapatkan fokus.

## HTML5 Tag

a. `<header>`:
Digunakan untuk memuat elemen header seperti judul, logo, navigasi, dll.

b. `<nav>`:
Digunakan untuk menandai blok navigasi, biasanya berisi menu atau daftar link.

c. `<main>`:
Digunakan untuk menampung konten utama dari halaman web, dan biasanya hanya ada satu per halaman.

d. `<article>`:
Digunakan untuk menandai konten independen seperti postingan blog atau artikel berita.

e. `<section>`:
Digunakan untuk mengelompokkan konten dan biasanya memiliki heading terkait.

f. `<aside>`:
Digunakan untuk menampung konten yang berhubungan tetapi terpisah dari konten utama, seperti sidebar.

g. `<footer>`:
Digunakan untuk menampung elemen footer seperti informasi hak cipta, link, dll.

h. `<figure>` dan `<figcaption>`:
`<figure>` digunakan untuk melampirkan gambar, diagram, dll, dan `<figcaption>` digunakan untuk memberikan keterangan untuk elemen `<figure>`.

i. `<mark>`:
Digunakan untuk menandai atau menyoroti teks.

j. `<progress>`:
Digunakan untuk menampilkan bar kemajuan.

k. `<output>`:
Digunakan untuk menampilkan hasil dari sebuah perhitungan atau aksi pengguna.

l. `<canvas>`:
Digunakan untuk menggambar grafik, membuat game, atau memanipulasi gambar dengan JavaScript.

m. `<video>` dan `<audio>`:
`<video>` digunakan untuk menambahkan video, dan `<audio>` digunakan untuk menambahkan audio.

n. `<time>`:
Digunakan untuk merepresentasikan waktu atau tanggal.

## Perbedaan antara Margin dan Padding

### Margin

Margin adalah properti CSS yang digunakan untuk menciptakan ruang sekitar elemen, di luar batas tepi (border) yang ada.
Margin tidak memiliki warna dan selalu transparan.
Margin bisa digunakan untuk membuat jarak antara dua elemen.

### Padding

Padding adalah properti CSS yang digunakan untuk menciptakan ruang sekitar konten elemen, di dalam batas tepi (border) yang ada.
Padding dapat memiliki warna, yaitu warna dari elemen tersebut.
Padding digunakan untuk membuat jarak antara konten dan batas tepi (border) elemen tersebut.


## Perbedaan antara Framework CSS Tailwind dan Bootstrap
### Tailwind CSS

Tailwind adalah framework CSS yang berfungsi sebagai utility-first CSS framework.
Dalam Tailwind, kelas-kelas kecil dan tunggal digunakan secara komprehensif untuk membangun desain.
Tailwind memberikan kontrol yang lebih granular terhadap desain, memungkinkan pengembang membuat desain yang unik dan kustom.
Biasanya memerlukan konfigurasi lebih pada awal pengembangan.
Lebih fleksibel dan memungkinkan lebih banyak variasi desain.

### Bootstrap

Bootstrap adalah framework CSS yang mengandung pre-designed components.
Bootstrap menyediakan komponen-komponen yang sudah distilasi desainnya, seperti kartu, navigasi, modal, dll.
Lebih cepat untuk prototyping atau membangun aplikasi dengan desain standar.
Mungkin lebih mudah untuk pemula karena banyaknya dokumentasi dan komunitas yang mendukung.
Memungkinkan pengembangan yang lebih cepat untuk proyek-proyek yang tidak memerlukan desain kustom.

### Kapan Menggunakan Bootstrap daripada Tailwind, dan Sebaliknya?

### Menggunakan Bootstrap

Ketika Anda membutuhkan prototyping yang cepat dan efisien.
Ketika Anda membutuhkan komponen yang sudah jadi dan mendesain ulang tidak perlu.
Ketika Anda membutuhkan dokumentasi yang luas dan komunitas yang besar untuk dukungan.
Bagus untuk proyek-proyek yang lebih kecil atau jika Anda baru memulai dengan pengembangan front-end.

### Menggunakan Tailwind CSS

Ketika Anda membutuhkan kontrol yang lebih granular atas desain dan styling.
Ketika Anda menginginkan desain yang benar-benar kustom dan unik.
Ketika Anda menyukai pendekatan utility-first dan ingin menghindari penggunaan CSS kustom.
Bagus untuk proyek-proyek yang lebih besar dan tim yang membutuhkan kontrol lebih atas desain.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
- Menambahkan bootstrap CSS dan JS
- Menambahkan navbar

### Menambahkan tombol edit
- Menambahkan fungsi `edit_product` dan berkas html `edit_product.html` untuk tombol edit pada product
- Menambahkan tombol `edit_product` pada `main.html` agar terlihat tombol edit pada setiap product

### Membuat fungsi hapus
- Membuat fungsi baru `delete_product` pada `views.py`
- Menambahkan tombol `delete_product` pada `main.html`

### Desain
- Mendesain tampilan website dengan menambahkan style pada `main.html`


</details>


<details>
<summary>Tugas 6</summary>

# Tugas 6

## Penerapan Asynchronous Programming pada AJAX

AJAX (Asynchronous JavaScript and XML) adalah teknik yang digunakan dalam pengembangan web untuk mengirim dan menerima data dari server secara asinkron tanpa harus memuat ulang seluruh halaman web. Penerapan asynchronous programming pada AJAX adalah inti dari fungsionalitas ini. Dalam konteks AJAX:

- Asynchronous Programming: Ketika melakukan permintaan AJAX, menggunakan JavaScript untuk membuat permintaan ke server secara asinkron. Ini berarti bahwa permintaan tersebut tidak akan memblokir eksekusi kode JavaScript lainnya. Alih-alih menunggu server merespons, kode JavaScript dapat melanjutkan menjalankan tugas lain. Saat respons dari server tiba, kita dapat meresponsnya dengan mengaitkan fungsi callback yang akan dijalankan. Ini memungkinkan aplikasi web untuk tetap responsif dan tidak menghentikan pengguna dari berinteraksi dengan halaman web selama permintaan AJAX sedang berlangsung.

## Perbandingan Fetch API dengan jQuery untuk AJAX

1. **Fetch API**:
   - **Kelebihan**:
     - Terintegrasi dalam JavaScript modern, tidak perlu mengimpor library eksternal.
     - Memiliki dukungan asli untuk Promise, yang membuatnya lebih mudah digunakan dengan asynchronous programming.
     - Lebih ringan dan modular, sehingga memungkinkan memilih bagian yang ingin digunakan.
     - Mendukung format data selain XML, seperti JSON, yang umum digunakan dalam pertukaran data.

   - **Kekurangan**:
     - Memerlukan penanganan khusus untuk menangani respons HTTP yang berbeda (seperti penanganan error HTTP).

2. **jQuery**:
   - **Kelebihan**:
     - Menyediakan antarmuka yang lebih sederhana dan konsisten untuk AJAX, yang memungkinkan pemrogram lebih mudah mengirim permintaan dan menangani respons.
     - Dapat menangani respons HTTP yang berbeda dengan lebih baik secara otomatis.
     - Memiliki dukungan lintas-browser yang kuat, sehingga tidak perlu khawatir tentang perbedaan implementasi browser.

   - **Kekurangan**:
     - Berukuran lebih besar dibandingkan dengan Fetch API karena termasuk banyak fitur lain selain AJAX.
     - Bergantung pada library eksternal tambahan (meskipun di masa lalu, ini lebih penting daripada saat ini).

**Pendapat**:

Pilihan antara Fetch API dan jQuery untuk AJAX sebagian besar tergantung pada kebutuhan proyek dan preferensi sebagai pengembang. Fetch API adalah pilihan yang baik jika ingin menjaga aplikasi tetap ringan, menggunakan fitur terbaru JavaScript, dan memiliki kendali yang lebih besar atas bagaimana cara menangani permintaan dan respons. Ini lebih modern dan disarankan untuk proyek-proyek baru atau yang telah menggunakan ekosistem JavaScript modern.

Di sisi lain, jQuery masih merupakan pilihan yang kuat jika ingin kesederhanaan dalam pengembangan, kompatibilitas lintas-browser yang baik, dan alat yang lebih kaya dalam satu paket. Ini cocok untuk proyek-proyek yang lebih lama yang masih menggunakan jQuery atau jika merasa lebih nyaman dengan antarmuka yang disediakan oleh jQuery.

## **Perbedaan antara Asynchronous Programming dengan Synchronous Programming**:

   - **Synchronous Programming (Sync)**: Pada pemrograman sinkron, tugas-tugas dieksekusi secara berurutan satu per satu. Setiap tugas harus menunggu tugas sebelumnya selesai sebelum dapat dijalankan. Ini berarti bahwa jika tugas pertama memakan waktu lama, maka semua tugas berikutnya harus menunggu.
   
   - **Asynchronous Programming (Async)**: Pada pemrograman asinkron, tugas-tugas dapat dieksekusi secara independen tanpa harus menunggu satu sama lain. Ini memungkinkan tugas-tugas yang memakan waktu lama untuk dieksekusi di latar belakang sementara tugas lain dapat dilanjutkan. Asynchronous programming sering digunakan untuk mengatasi operasi I/O yang memakan waktu seperti mengambil data dari server, operasi jaringan, atau input/output file.

## **Paradigma Event-Driven Programming**:

   Paradigma event-driven programming adalah pendekatan dalam pemrograman di mana program merespons peristiwa (events) yang terjadi, seperti input pengguna, perubahan status, atau tindakan lain yang dapat memicu respons. Ini berarti program tidak selalu berjalan secara berurutan, tetapi dapat menunggu peristiwa yang akan datang dan meresponsnya.

   Dalam tugas, pengguna merespons berbagai peristiwa, seperti mengklik tombol "Tambah Produk" atau mengklik tombol "Hapus" pada item produk. Ketika pengguna melakukan tindakan ini, JavaScript merespons peristiwa tersebut dengan mengirimkan permintaan AJAX ke server atau menampilkan modul tambahan seperti modal "Tambah Produk". Dengan demikian, paradigma event-driven programming digunakan untuk mengatasi peristiwa pengguna dan meresponsnya secara dinamis, yang memungkinkan interaksi yang lebih baik dengan aplikasi web  tanpa harus memuat ulang seluruh halaman.

## Cara saya mengimplementasikan checklist di atas secara step-by-step 
* AJAX GET untuk Mengambil Data Item: Untuk membuatnya bekerja, pastikan memiliki view di Django yang melayani URL {% url 'main:get_product_json' %} dan mengembalikan data produk dalam format JSON.
* Modal untuk Penambahan Item dengan AJAX POST: Ketika tombol "Add Product" di dalam modal diklik (button_add), fungsi addProduct dipanggil, yang akan melakukan AJAX POST ke {% url 'main:add_product_ajax' %}.
* Membuat Fungsi View untuk Menambahkan Item: Buat fungsi view di Django yang menerima POST request ke URL /create-ajax/. Fungsi view ini harus mengambil data dari request, validasi, dan menambahkannya ke database. Setelah berhasil, kembalikan respons positif (misalnya, status 201 atau JSON yang mengindikasikan sukses). Jika ada kesalahan, kembalikan pesan kesalahan yang relevan.
* Menyambungkan Form ke Path /create-ajax/: harus memastikan bahwa form di dalam modal mengarah ke {% url 'main:add_product_ajax' %} untuk submit. Ini sudah dilakukan di fungsi addProduct.
* Refresh Asinkronus: Setelah AJAX POST sukses (dalam fungsi addProduct), memanggil fungsi refreshProducts untuk memperbarui daftar produk di halaman tanpa perlu me-refresh seluruh halaman.
* Melakukan Perintah collectstatic:
    * menambahkan STATIC_ROOT di settings.py . Ini adalah lokasi di mana Django akan menempatkan semua file statis saat menjalankan collectstatic. STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
</details>
