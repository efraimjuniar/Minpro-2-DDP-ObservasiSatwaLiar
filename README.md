# Minpro-2-DDP-ObservasiSatwaLiar

Sistem Pengelolaan Data Observasi Satwa Liar Saat Pendakian — Mini Project 2 Praktikum Dasar-Dasar Pemrograman (DDP)

Nama : Efraim Juniar Tonda Kala' 

NIM : 2609116064 

Kelas : B

---------------------------------------------------------------------------------------------------------------------------------------
**1. Deskripsi Program**
   
Program ini lanjutan dari Mini Project 1, masih dengan tema yang sama: mencatat satwa liar yang ditemui pendaki saat naik gunung. Bedanya, sekarang programnya tidak bisa langsung dipakai. Pengguna harus login terlebih dahulu pakai username dan password.

Ada 2 jenis pengguna (role) yang hak aksesnya beda:

admin → bisa tambah, tampilkan, ubah, dan hapus data (akses penuh)
user (pendaki) → cuma bisa tambah dan tampilkan data saja

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

