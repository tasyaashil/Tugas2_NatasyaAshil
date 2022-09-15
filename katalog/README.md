Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtual environment digunakan untuk tidak bertabrakan dengan versi lain yang terdapat di komputer, aplikasi web berbasis django dapat digunakan tanpa menggunakan virtual environment. Namun venv ini memiliki fungsi supaya terisolasi dan tidak tercampur package nya terorganisir.


Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
views.py
Pada bagian views.py dilakukannya pengambilan semua data yang terdapat di database. Kemudian menambahkan variabel baru seperti nama mahasiswa, NPM, dan item. Serta terdapat juga item data yang dapat dimunculkan datanya pada halaman HTML.

urls.py
Pada bagian urls.py dilakukannya routing pada katalog sehingga HTML dapat ditampilkan oleh browser.

katalog.html
Pada bagian katalog.html, saya menggunakan for loop dan mengambil data-data yang terdapat di database dengan menyimpan kedalam item data.

deploy
Pada tahap deploy, diperlukan aplikasi heroku dengan menuliskan HEROKU_APP_NAME dan HEROKU_API_KEY pada github actions secret untuk menghubungkan dengan repsitori github
