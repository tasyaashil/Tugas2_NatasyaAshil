## Link Heroku
https://natasya-tugas3.herokuapp.com/todolist/

## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
`{%csrf_token%}` pada elemen form memiliki kegunaan untuk membandingkan kedua token yang ditemukan pada user maupun request. Pada sisi user, dilakukannya validasi dari request, jika request cocok dengan form, maka akan merespon OK, jika tidak cocok maka request akan ditolak.

Apabila tidak ada potongan kode `{%csrf_token %}`, elemen form akan rentan terjadinya route link yang diakses oleh orang lain. Selain itu, berbagai teknik yang dilakukan penyerang yaitu dapat menggunakan data yang dibuat untuk memanipulasi dokumen HTML dan menangkap bagian dari isinya.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Jawabannya adalah ya bisa, dapat membuat elemen form secara manual tanpa menggunakan generator seperti `form.as_table`. Caranya ialah dengan menggunakan type, input, dan value untuk menyesuaikan dengan sesuai keinginan.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Alur datanya user akan mengisi data pada form kemudian data yang diisi akan dicek apakah valid atau tidak. Jika valid data tersebut akan berinteraksi dengan `views.py` dan `models.py`, lalu akan tersimpan pada database. Kemudian data yang tersimpan akan memunculkan pada halaman html.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Pertama membuat aplikasi baru bernama `todolist` dengan menjalankan perintah
   ```shell
    python manage.py startapp todolist
   ```
   Setelah itu pada `settings.py` folder `project_django` menambahkan aplikasi `todolist` pada `INSTALLLED_APPS`, serta membuat fungsi `show_todolist` pada `views.py` folder `todolist` lalu menambahkan path pada `urls.py` folder `project_django`.
2. Membuat class bernama `Tasktodolist` pada `models.py` folder `todolist` untuk membuat field `user, data, title, dan description` beserta atribut sesuai dengan ketentuan soal.
3. Menambahkan `@login_required(login_url='/todolist/login/'), fungsi register, login_user, logout_user, add_todolist.` 
4. Me-return `todolist.html` pada fungsi `show_todolist`, me-return `register.html` pada fungsi `register`, me-return `login.html` pada fungsi `login_user`, me-return `add_todolist.html` pada fungsi `add_todolist`.
5. Membuat isi html dengan kesesuaian fungsi seperti halnya data login, registrasi, todolist, tombol, dan lainnya.
6. Melakukan routing dan kemudian menjalankan `python manage.py makemigrations` dan `python manage.py migrate` lalu terakhir `python manage.py runserver`.
6. Melakukan git add, commit, dan push untuk persiapan deploy.
7. Memasukkan app_name dan api_key pada github untuk menghubungkan heroku.