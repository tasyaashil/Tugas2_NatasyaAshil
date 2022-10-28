## Link Heroku
https://natasya-tugas3.herokuapp.com/todolist/

## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
1. Inline CSS: Inline merupakan metode yang digunakan menggunakan atribut `style` pada tag `HTML`.
- Kelebihannya ialah mudah diimplementasikan jika hanya ingin merubah tag HTML tertentu.
- Kekurangannya ialah tidak efektif ketika merubah tag HTML dalam jumlah yang besar/banyak.

2. Internal CSS: Internal merupakan metode yang menggunakan atribut `style` di dalam `<head>` HTML.
- Kelebihannya ialah mudah diimplementasikan pada file HTML langsung tidak perlu membuat file CSS terpisah.
- Kekurangannya ialah tidak efisien untuk dipakai pada banyak file.

3. External CSS: External merupakan metode yang menggunakan tag `<link>` untuk menghubungkan file CSS yang terpisah.
- Kelebihannya ialah tampilan lebih rapih dan bisa digunakan untuk banyak file.
- Kekurangannya tidak efisien jika dipakai dalam skala kecil.

## Jelaskan tag HTML5 yang kamu ketahui.
1. `<button>`= mendefinisikan document tombol.
2. `<body>` = mendefinisikan elemen utama.
3. `<col>` = mendefinisikan kolom tabel.
4. `<div>` = mendefinisikan bagian tertentu dalam document.
5. `<h1>, <h2>, ... <h6>` = mendefinisikan header.
6. `<nav>` = mendefinisikan navigasi link.
7. `<style>` = mendefinisikan style untuk css.

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Tag Selector = menggunakan `tag` HTML sebagai selectornya.
2. ID Selector = menggunakan `id` pada HTML dan diimplementasikan dengan tanda `#`,
3. Class Selector = menggunakan `class` pada HTML dan diimplementasikan dengan tanda `.`.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Menggunakan implementasi external CSS dengan membuat folder `static` yang berisikan file `.css`. Membuat style pada halaman login, register, todolist, dan add_todolist. Menghubungkan file CSS dengan HTML dengan menggunakan `{% load static %}
`<link rel="stylesheet" href="{% static 'css/namafile.css' %}">` pada file HTML.
2. Mengubah bentuk tabel pada file `todolist.html` menjadi bentuk card. 
3. Menjalankan `python manage.py runserver`.
4. Melakukan git add, commit, dan push untuk perubahan yang dilakukan.