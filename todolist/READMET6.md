## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
1. Asynchronous programming = merupakan proses yang memungkinkan untuk berjalan sekaligus tanpa menunggu antrian.
2. Synchronous programming = merupakan proses yang harus menyelesaikan suatu task terlebih dahulu baru dapat melanjutkan ke task berikutnya.

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
- Paradigma Event-Driven merupakan paradigma dimana setiap entitas mengirimkan pesan ke entitas lain melalui sebuah perantara. 
- Contoh penerapan di tugas ini ialah onclick

## Jelaskan penerapan asynchronous programming pada AJAX.
Penerapan asynchronous programming pada AJAX ialah AJAX dapat mengambil data tanpa mengirim atau menerima (reload seluruh laman website) data dari server secara asynchronous. Dengan begitu, AJAX hanya akan mengirimkan request pada server dan kemudian dilanjutkan langsung untuk eksekusi tanpa menunggu balasan dari server terlebih dahulu.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat view baru untuk mengembalikan data task berbentuk json. Kemudian membuat path di urls.
2. Menggunakan ajax get untuk pengambilan data task di todolist.html.
3. Membuat tombol untuk menambahkan task dengan membuka sebuah modal
4. Membuat fungsi baru pada views untuk menambahkan task
5. Menghubungkan form dengan modal.
6. Menjalankan server pada localhost.
7. Melakukan deployment perubahan
