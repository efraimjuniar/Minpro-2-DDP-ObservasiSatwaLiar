import os
import time
import pwinput

data_satwa = []
satwa_dilindungi = ["elang jawa", "harimau sumatera", "anoa", "burung maleo",
                    "orangutan", "macan tutul", "komodo"]


akun = {
    "admin": {"password": "admin123", "role": "admin"},
    "pendaki": {"password": "daki123", "role": "user"}
}


akses_menu = {
    "admin": ["Tambah Data Satwa", "Tampilkan Semua Data", "Ubah Data", "Hapus Data", "Logout"],
    "user": ["Tambah Data Satwa", "Tampilkan Semua Data", "Logout"]
}


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def input_angka(teks):

    while True:
        try:
            nilai = int(input(teks))
            if nilai > 0:
                return nilai
            print("Nilai harus lebih dari 0, ulangi.")
        except ValueError:
            print("Input harus berupa angka, ulangi.")


def cek_status(nama):
    if nama.lower() in satwa_dilindungi:
        return "Dilindungi"
    jawab = input(f"'{nama}' tidak ada di daftar, apakah dilindungi? (y/n): ")
    if jawab.lower() == "y":
        return "Dilindungi"
    return "Tidak Dilindungi"


def tentukan_zona(tinggi):
    if tinggi < 1000:
        return "Zona Dataran Rendah (Hutan Hujan)"
    elif tinggi < 2400:
        return "Zona Montane (Hutan Pegunungan)"
    else:
        return "Zona Sub-Alpin (Puncak/Vegetasi Rendah)"


def login():
    percobaan = 0
    print("\n===== LOGIN SISTEM OBSERVASI SATWA LIAR =====")
    while percobaan < 3:
        username = input("Username: ")
        password = pwinput.pwinput(prompt="Password: ", mask="*")

        if username in akun and akun[username]["password"] == password:
            role = akun[username]["role"]
            print(f"\nLogin berhasil! Selamat datang, {username} (role: {role})")
            return username, role

        percobaan += 1
        print(f"Username/password salah! Sisa percobaan: {3 - percobaan}")

    print("Gagal login 3 kali. Program dihentikan.")
    return None, None


def tambah_data():
    print("\n--- Tambah Data Satwa ---")
    nama = input("Nama satwa       : ")
    jumlah = input_angka("Jumlah (ekor)    : ")
    tinggi = input_angka("Ketinggian (mdpl): ")

    status = cek_status(nama)
    zona = tentukan_zona(tinggi)
    tanggal = time.strftime("%d-%m-%Y")
    data_satwa.append((nama, jumlah, tinggi, status, zona, tanggal))

    print("\nData berhasil ditambahkan!")
    print(f"    Status  : {status}")
    print(f"    Zona    : {zona}")
    print(f"    Tanggal : {tanggal}")


def tampilkan_data():
    print("\n--- Riwayat Observasi Satwa ---")
    if len(data_satwa) == 0:
        print("Belum ada data satwa yang dicatat.")
        return

    nomor = 1
    for s in data_satwa:
        print(f"{nomor}. {s[0]} ({s[1]} ekor) | {s[2]} mdpl | dicatat {s[5]}")
        print(f"   Status: {s[3]} | Zona: {s[4]}")
        nomor += 1


def ubah_data():
    print("\n--- Ubah Data Satwa ---")
    if len(data_satwa) == 0:
        print("Belum ada data satwa yang bisa diubah.")
        return

    tampilkan_data()
    no = input_angka("Pilih nomor data yang mau diubah: ")
    if no < 1 or no > len(data_satwa):
        print("Nomor data tidak ditemukan.")
        return

    nama = input("Nama satwa baru       : ")
    jumlah = input_angka("Jumlah baru (ekor)    : ")
    tinggi = input_angka("Ketinggian baru (mdpl): ")

    status = cek_status(nama)
    zona = tentukan_zona(tinggi)
    tanggal_lama = data_satwa[no - 1][5]
    data_satwa[no - 1] = (nama, jumlah, tinggi, status, zona, tanggal_lama)

    print("\nData berhasil diubah!")
    print(f"    Status : {status}")
    print(f"    Zona   : {zona}")


def hapus_data():
    print("\n--- Hapus Data Satwa ---")
    if len(data_satwa) == 0:
        print("Belum ada data satwa yang bisa dihapus.")
        return

    nama_hapus = input("Nama satwa yang ingin dihapus: ")
    ditemukan = None
    for s in data_satwa:
        if s[0].lower() == nama_hapus.lower():
            ditemukan = s

    if ditemukan is not None:
        print(f"\n[Data Ditemukan] {ditemukan[0]} - {ditemukan[3]} - {ditemukan[4]}")
        konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
        if konfirmasi.lower() == "y":
            data_satwa.remove(ditemukan)
            print(f"Data '{ditemukan[0]}' berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f"Data satwa '{nama_hapus}' tidak ditemukan.")


def tampilkan_menu(role):
    print("\n==========================================")
    print("   LOGBOOK OBSERVASI SATWA LIAR PENDAKIAN  ")
    print(f"   (login sebagai: {role})")
    print("==========================================")

    daftar_menu = akses_menu[role]
    for i in range(len(daftar_menu)):
        print(f"{i + 1}. {daftar_menu[i]}")


def main():
    bersihkan_layar()
    username, role = login()
    if role is None:
        return

    while True:
        tampilkan_menu(role)
        pilihan = input("Pilih menu: ")

        if role == "admin":
            if pilihan == "1":
                tambah_data()
            elif pilihan == "2":
                tampilkan_data()
            elif pilihan == "3":
                ubah_data()
            elif pilihan == "4":
                hapus_data()
            elif pilihan == "5":
                print(f"\nLogout berhasil. Sampai jumpa, {username}!")
                break
            else:
                print("Pilihan tidak valid!")

        else:  
            if pilihan == "1":
                tambah_data()
            elif pilihan == "2":
                tampilkan_data()
            elif pilihan == "3":
                print(f"\nLogout berhasil. Sampai jumpa, {username}!")
                break
            else:
                print("Pilihan tidak valid!")


main()