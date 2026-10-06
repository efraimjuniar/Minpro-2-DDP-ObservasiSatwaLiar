# Minpro-2-DDP-ObservasiSatwaLiar

Sistem Pengelolaan Data Observasi Satwa Liar Saat Pendakian — Mini Project 2 Praktikum Dasar-Dasar Pemrograman (DDP)

Nama : Efraim Juniar Tonda Kala' 

NIM : 2609116064 

Kelas : B

---------------------------------------------------------------------------------------------------------------------------------------
**1. Deskripsi Program**
   
Program ini lanjutan dari Mini Project 1, masih dengan tema yang sama: mencatat satwa liar yang ditemui pendaki saat naik gunung. Bedanya, sekarang programnya tidak bisa langsung dipakai. Pengguna harus login terlebih dahulu pakai username dan password.

Ada 2 jenis pengguna (role) yang hak aksesnya beda:<br>
admin &rarr; bisa tambah, tampilkan, ubah, dan hapus data (akses penuh)<br>
user (pendaki) &rarr; cuma bisa tambah dan tampilkan data saja

Akun demo yang bisa dipakai buat coba program ini:

Username | Password | Role  |
---------|----------|-------|
admin    | admin123 | admin |
pendaki  | daki123  | user  |

Secara struktur, program ini dipecah jadi beberapa function supaya tidak ada kode yang ditulis berulang-ulang, misalnya **login()** buat proses masuk, **cek_status()** dan **tentukan_zona()** buat logika pengecekan otomatis (sama seperti di MP1), serta **tambah_data()**, **tampilkan_data()**, **ubah_data()**, **hapus_data()** buat keempat operasi CRUD. Data akun dan daftar menu per role disimpan dalam bentuk dictionary (akun dan akses_menu), sementara data satwa sendiri tetap disimpan sebagai list berisi tuple seperti di MP1, hanya saja sekarang ditambah satu elemen baru yaitu tanggal observasi.

Program ini juga memanfaatkan 3 library tambahan: pwinput untuk menyamarkan input password jadi tanda bintang (*) saat login, time untuk mencatat tanggal otomatis setiap kali data satwa ditambahkan, dan os untuk membersihkan layar terminal di awal program. Sebagai nilai tambah, validasi input angka (jumlah dan ketinggian) juga sudah memakai error handling (try/except), jadi kalau pengguna salah ketik (misalnya masukkan huruf padahal diminta angka), program tidak akan crash, tapi akan menampilkan pesan error dan minta input ulang.

-----------------------------------------------------------------------------------------------------------------------------------------------
**2. FLOWCHART & Penjelasan Alur**

<img width="279" height="395" alt="image" src="https://github.com/user-attachments/assets/b7616d45-508a-424e-a7d1-6ee41763d1d8" />


Flowchart Mini Project 1 dikembangkan menjadi satu diagram gabungan yang mencakup alur login sekaligus alur menu utama. Alurnya bisa dibagi jadi dua bagian besar:

**Bagian 1 — Login**

Program dimulai dengan meminta username dan password. Kedua input ini dicocokkan dengan data yang tersimpan di dalam dictionary akun. Kalau cocok, program akan mengambil role milik username tersebut (admin atau user) dari dictionary itu, menampilkan pesan "Login berhasil", lalu lanjut ke bagian menu. Kalau tidak cocok, jumlah percobaan ditambah satu, lalu dicek lagi: kalau percobaan masih kurang dari 3 kali, program minta input username/password ulang (balik ke awal); kalau sudah gagal 3 kali, program menampilkan pesan bahwa login gagal dan program langsung berhenti.

**Bagian 2 — Menu Utama**

Setelah login berhasil, program menampilkan daftar menu — tapi isinya tidak sama untuk semua orang, karena diambil dari dictionary akses_menu sesuai role masing-masing. Kalau role-nya admin, menunya lengkap (Tambah, Tampilkan, Ubah, Hapus, Logout). Kalau role-nya user, menunya terbatas (Tambah, Tampilkan, Logout saja). Setelah menu ditampilkan, program meminta pilihan dari pengguna. Kalau pilihannya logout, program menampilkan pesan "Logout berhasil" dan berhenti. Kalau bukan logout, program menjalankan proses sesuai pilihan tersebut (Tambah/Tampilkan Data, atau Ubah/Hapus Data khusus untuk admin), lalu kembali lagi ke tampilan menu supaya pengguna bisa pilih menu lain tanpa harus login ulang.

Intinya, flowchart MP1(menu berulang pakai while) sekarang "dibungkus" dengan tahap login di depannya, dan menu yang ditampilkan jadi dinamis, bentuknya menyesuaikan siapa yang login.

-------------
**3. Dokumentasi Program & Output**

Struktur Program

Program ini disusun menggunakan beberapa function, antara lain:

Function                                                   |	Kegunaan                                                     |
-----------------------------------------------------------|---------------------------------------------------------------|
bersihkan_layar()                                          |	Membersihkan layar terminal (library os)                     |
input_angka()                                              |	Memvalidasi input angka memakai error handling (try/except)  |
login()                                                    |	Menangani proses login, maksimal 3 kali percobaan            |
cek_status()                                               |	Mengecek status perlindungan satwa                           |
tentukan_zona()                                            |	Menentukan zona habitat berdasarkan ketinggian               |
tambah_data(), tampilkan_data(), ubah_data(), hapus_data() |	Operasi CRUD terhadap data satwa                             |
tampilkan_menu()                                           |	Menampilkan menu sesuai role, memakai dictionary akses_menu  |
main()                                                     |	Menjalankan program secara keseluruhan                       |

Data akun (akun) dan daftar menu per role (akses_menu) disimpan sebagai dictionary, sedangkan data observasi satwa (data_satwa) tetap berupa list berisi tuple: (nama, jumlah, tinggi, status, zona, tanggal)

**Contoh Output — Login Gagal**

<img width="196" height="123" alt="image" src="https://github.com/user-attachments/assets/c69d8447-9fd3-4485-8036-ac19fd06ba33" />

(Karakter password tampil sebagai * berkat library pwinput, bukan tersembunyi total seperti getpass.)


**Contoh Output — Login Berhasil (role admin)**<br>
<img width="242" height="183" alt="image" src="https://github.com/user-attachments/assets/3e3098bf-36a4-4027-bb91-b8a130b21ffc" />

**Contoh Output — Login Berhasil (role user, menu terbatas)**<br>
<img width="275" height="167" alt="image" src="https://github.com/user-attachments/assets/0cb82a7e-8b42-4c6b-924a-1f9a317bec59" />

**Contoh Output — Tambah Data**<br>
<img width="219" height="229" alt="image" src="https://github.com/user-attachments/assets/dfb1978c-d00b-4e5d-b1a5-549c773c04f5" />

**Contoh Output — Input Salah (ditangani error handling)**<br>
<img width="165" height="62" alt="image" src="https://github.com/user-attachments/assets/e29c70b0-6f68-4c52-b6ab-f3ea54e4ecc5" />

**Contoh Output — Tampilkan Semua Data**<br>
<img width="293" height="69" alt="image" src="https://github.com/user-attachments/assets/e426bc58-1777-49f9-8cd0-9175a8141810" />

**Contoh Output — Hapus Data**<br>
<img width="325" height="77" alt="image" src="https://github.com/user-attachments/assets/99377fdf-7a32-47d2-ac19-53b476cb3e05" />

----------------------------------------
**4. Validasi input dengan error handling**

Input angka (jumlah satwa dan ketinggian) divalidasi menggunakan try/except di dalam function input_angka():

<img width="277" height="126" alt="image" src="https://github.com/user-attachments/assets/058a6db5-827c-4f21-88fd-5da1dcc695eb" />

Jika pengguna mengetik huruf atau teks lain (bukan angka), Python akan memunculkan ValueError saat dikonversi dengan int(). Di sini, ValueError berfungsi sebagai penanda spesifik agar program tau jenis kesalahan yang harus ditangani. Error ini ditangkap oleh blok except, sehingga program tidak berhenti/crash, melainkan menampilkan pesan dan meminta input ulang.

----------------------------------------
**5. Penerapan 3 library**

Program ini menggunakan 3 library Python, seluruhnya dari materi yang sudah diajarkan di praktikum:

library | Kegunaan dalam Program                                                                      |
--------|---------------------------------------------------------------------------------------------|
pwinput | Menyamarkan input password saat login (tampil sebagai *, tidak polos seperti input() biasa) |
time	  | Mencatat tanggal observasi secara otomatis setiap kali data ditambahkan                     |
os      | Membersihkan layar terminal (bersihkan_layar()) saat program pertama dijalankan             |
