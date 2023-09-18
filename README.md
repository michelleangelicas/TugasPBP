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
1. Mengimplementasikan skeleton sebagai kerangka Views dengan menambahkan folder templates dalam root folder dan membuat base.html di dalamnya, menambahkan beberapa potongan kode pada settings.py, mengubah kode berkas main.html dengan menambahkan {% extends 'base.html' %}
2. Membuat form input data dan tampilan pada HTML. Membuat berkas forms.py yang mempunyai fields name, amount, description. Menambahkan fungsi create_product, show_main. Menambahkan path url path('create-product', create_product, name='create_product’), lalu membuat berkas html baru create_product.html
3. Menjadikan data dalam bentuk XML dan JSON dengan membuat fungsi dan menambahkan path url dalam urlpatterns. 
4. menjadikan data berdasarkan ID dalam bentuk XML, JSON. Menambahkan function show_xml_by_id dan show_json_by_id di views.py dan menambahkan urlpatterns pada urls.py. 