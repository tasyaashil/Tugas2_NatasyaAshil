## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
`{%csrf_token%}` pada elemen form memiliki kegunaan untuk membandingkan kedua token yang ditemukan pada user maupun request. Pada sisi user, dilakukannya validasi dari request, jika request cocok dengan form, maka akan merespon OK, jika tidak cocok maka request akan ditolak.

Apabila tidak ada potongan kode `{%csrf_token %}`, elemen form akan rentan terjadinya route link yang diakses oleh orang lain. Selain itu, berbagai teknik yang dilakukan penyerang yaitu dapat menggunakan data yang dibuat untuk memanipulasi dokumen HTML dan menangkap bagian dari isinya.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Ya bisa, dapat membuat elemen form secara manual tanpa menggunakan generator seperti `form.as_table`. Caranya ialah dengan menggunakan `csrf_token`. 

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Alur datanya 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Pertama membuat aplikasi baru bernama todolist dengan menjalankan perintah
   ```shell
    python manage.py startapp todolist
   ```
   Setelah itu pada settings.py folder project_django menambahkan aplikasi todolist pada INSTALLLED_APPS, serta membuat fungsi show_todolist pada views.py folder todolist lalu menambahkan path pada urls.py folder project_django.
2. Membuat class bernama Tasktodolist pada models.py folder todolst untuk membuat field user, data, title, dan description.
3. 