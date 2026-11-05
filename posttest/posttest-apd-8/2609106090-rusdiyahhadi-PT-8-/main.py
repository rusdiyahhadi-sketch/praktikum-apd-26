from utils import bersihkan_layar, input_berat
from auth import menu_awal
from data import data_user, data_panen
from crud import cek_id, hitung_total, tampil_data

def tampil_menu(role, user):
    print("=== MENU", role, "===")  
    print("Login sebagai:", user)
    print("1. Tambah Panen") 
    print("2. Lihat Panen")
    if role == "admin":
        print("3. Ubah Panen")
        print("4. Hapus Panen")
    print("0. Keluar")

user = menu_awal()
role = data_user[user]["akses"]
while True:
    bersihkan_layar()
    tampil_menu(role, user)
    menu = input("Pilih menu: ").strip()
    if menu == "1":
        nama = input("Nama tanaman: ")
        berat = input_berat()
        tanggal = input("Tanggal panen: ")
        lokasi = input("Lokasi kebun: ")
        id_baru = max(data_panen, default=0) + 1
        data_panen[id_baru] = {
            "nama_tanaman": nama,
            "berat": berat,
            "tanggal": tanggal,
            "lokasi": lokasi
        }

        print("Data berhasil ditambahkan!")
        input("Tekan Enter untuk lanjut...")

    elif menu == "2":
        bersihkan_layar()
        print("=== Data Panen ===")
        if len(data_panen) == 0:
            print("Belum ada data panen.")
        else:
            tampil_data()
            print("Total panen:", hitung_total(list(data_panen.values())), "kg")
        input("\nTekan Enter untuk lanjut...")

    elif menu == "3" and role == "admin":
        tampil_data()
        nomor = input("ID data yang diubah: ").strip()
        id_p = cek_id(nomor)
        if id_p is not None:
            data_panen[id_p]["nama_tanaman"] = input("Nama tanaman baru: ")
            data_panen[id_p]["berat"] = input_berat()
            data_panen[id_p]["tanggal"] = input("tanggal: ")
            data_panen[id_p]["lokasi"] = input("lokasi: ")
            print("Data berhasil diubah!")
        else:
            print("ID tidak valid!")
        input("Tekan Enter untuk lanjut...")

    elif menu == "4" and role == "admin":
        tampil_data()
        nomor = input("ID data yang dihapus: ").strip()
        id_p = cek_id(nomor)
        if id_p is not None:
            del data_panen[id_p]
            print("Data berhasil dihapus!")
        else:
            print("ID tidak valid!")
        input("Tekan Enter untuk lanjut...")

    elif menu == "0":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk lanjut...")    


