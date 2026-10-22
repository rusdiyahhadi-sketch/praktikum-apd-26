import os

data_user ={
"admin":{"password":"admin123","akses":"admin"},
"cia": {"password":"cia123", "akses":"user"},
}
data_panen ={
   1:{"nama_tanaman" :"jagung", "berat":20.5, "tanggal":"14-10-2026", "lokasi": "kebun_A"},
   2:{"nama_tanaman":"kacang", "berat":15.5, "tanggal":"20-10-2026", "lokasi":"kebun_B"}, 
}
id_berikutnya = 3

user = None
while user is None:
    print("1. Login")
    print("2. Register")
    pilih_awal = input("Pilih: ").strip()
    if pilih_awal == "1":
        username = input("Username: ").strip()
        password = input("password: ").strip()
        if data_user.get(username) is not None and data_user[username]["password"] == password:
            user = username
        else:
            print("Username atau password salah!")
    elif pilih_awal == "2":
        username_baru = input("Username baru: ").strip()
        password_baru = input("Password baru: ").strip()
        if username_baru == "" or password_baru == "":
            print("Username dan password tidak boleh kosong!")
        elif data_user.get(username_baru) is not None:
            print("Username sudah terdaftar!")
        else:
            data_user[username_baru] = {"password": password_baru, "akses": "user"}
            user = username_baru
            print("Register berhasil!")

role = data_user[user]["akses"]                      
while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== MENU", role, "===")
    print("Login sebagai:", user)
    print("1. Tambah Panen")
    print("2. Lihat Panen")
    if role == "admin":
        print("3. Ubah Panen")
        print("4. Hapus Panen")
    print("0. Keluar")
 
    menu = input("Pilih menu: ").strip()
 
    if menu == "1":
       nama = input("Nama tanaman: ")
       while True:
            teks = input("Jumlah (kg): ").strip().replace(",", ".")
            if teks.replace(".", "", 1).isdecimal() and float(teks) > 0:
                berat = float(teks)
                break
            print("Jumlah harus angka lebih dari 0!")
       tanggal = input("Tanggal panen: ")
       lokasi = input("Lokasi kebun: ")
       data_panen[id_berikutnya] = {
        "nama_tanaman": nama,
        "berat": berat,
        "tanggal": tanggal,
        "lokasi": lokasi
       }
       id_berikutnya += 1
       print("Data berhasil ditambahkan!")
       print("Data yang ditambahkan:")
       print(nama, "|", berat, "kg |", tanggal, "|", lokasi)
       input("Tekan Enter untuk lanjut...")

    elif menu == "2":
        os.system("cls" if os.name == "nt" else "clear")
        print("=== DATA HASIL PANEN ===")
        if len(data_panen) == 0:
            print("Belum ada data.")
        else:
            for id_p, detail in data_panen.items():
                print("ID", id_p)   
                for key, value in detail.items():
                    print("  ", key, ":", value)
                print("")
        input("\nTekan Enter untuk lanjut...")

    elif menu == "3" and role == "admin":
        for id_p, detail in data_panen.items():
            print("ID", id_p)
            for key, value in detail.items():
                print("  ", key, ":", value)            
            print("")
        
        nomor = input("ID data yang diubah: ").strip()
        if nomor.isdecimal() and data_panen.get(int(nomor)) is not None:
            id_p = int(nomor)
            data_panen[id_p]["nama_tanaman"] = input("Nama tanaman baru: ")

            while True:
                teks = input("Jumlah (kg) baru: ").strip().replace(",", ".")
                if teks.replace(".", "", 1).isdecimal() and float(teks) > 0:
                    data_panen[id_p]["berat"] = float(teks)
                    break
                print("Jumlah harus angka lebih dari 0!")
            data_panen[id_p]["tanggal"] = input("Tanggal baru: ")
            data_panen[id_p]["lokasi"] = input("Lokasi baru: ")
            print("Data berhasil diubah!")
        else:
            print("ID tidak valid!")
        input("Tekan Enter untuk lanjut...")

    elif menu == "4" and role == "admin":
        for id_p, detail in data_panen.items():
            print("ID", id_p)
            for key, value in detail.items():
                print("  ", key, ":", value)
            print("")

        nomor = input("ID data yang dihapus: ").strip()
        if nomor.isdecimal() and data_panen.get(int(nomor)) is not None:
            del data_panen[int(nomor)]
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