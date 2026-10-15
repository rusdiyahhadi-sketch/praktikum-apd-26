# lemari = ["Baju", "Celana", 69, 7, 2, True, 70, 222, 240]


# angka1 = [ [1, 2], [3, 4] ]
# print(angka1[1][1])
# angka2 = [2, 4, 6]

# print("sebelum di ubah")
# print(lemari)

# ulang = angka1 * 3
# print(ulang)
# lemari[0:2] = ["Celana panjang", "jaket", "jas hujan"]

# print("sesudah di ubah")
# print(lemari)
# del lemari [1]
# hapus = "Baju"
# lemari.remove("Baju")

# sisa = lemari.pop(2)
# print = lemari



# print ("sebelum di insert")
# print (lemari)
# lemari.insert(1, "KTP")
# print ("sesudah di insert")
# print (lemari)

# for index,item in enumerate(lemari):
#     print(f"Index ke-{index + 1} : {item}")


# angka = (1, 2, 3, "hallo", True)
# ubah = list(angka)
# ubah.append("hai")

# angka = tuple(ubah)
# print(ubah)

# lemari ="baju", "celana", "sepatu"
# (atasan, *bawahan) = lemari

# print(bawahan)

# nilai = int(input("Masukkan nilai: "))
# if nilai >= 75:
#     print("Lulus")
# else:
#     print("Tidak Lulus")

# buah = ["jeruk", "apel"]

import os
 
# =====================================================
#  PENCATATAN HASIL PANEN KEBUN (CRUD dengan Nested List)
#  Tanpa def, tanpa try-except
# =====================================================
 
# Nested list pengguna : [username, password, role]
data_user = [
    ["admin", "admin123", "admin"],
    ["budi", "1234", "user"],
]
 
# Nested list panen : [id, nama_tanaman, jumlah_kg, tanggal_panen, lokasi_kebun, pencatat]
data_panen = [
    [1, "Cabai", 25.5, "10-10-2026", "Kebun A", "budi"],
    [2, "Jagung", 120.0, "12-10-2026", "Kebun B", "admin"],
]
 
# Tuple (data tetap)
KOLOM = ("ID", "Tanaman", "Jumlah (kg)", "Tanggal", "Lokasi", "Pencatat")
 
perintah_clear = "cls" if os.name == "nt" else "clear"
 
user = None          # None = belum login, selain itu berisi [username, password, role]
berjalan = True
 
while berjalan:
    os.system(perintah_clear)
 
    # =================================================
    #  BELUM LOGIN : LOGIN / REGISTER / KELUAR
    # =================================================
    if user is None:
        print("=" * 62)
        print("  PENCATATAN HASIL PANEN KEBUN")
        print("=" * 62)
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        pilih = input("Pilih menu: ").strip()
 
        # ---------- LOGIN ----------
        if pilih == "1":
            os.system(perintah_clear)
            print("=" * 62)
            print("  LOGIN")
            print("=" * 62)
            username_input = input("Username: ").strip().lower()
            password_input = input("Password: ").strip()
            for u in data_user:
                if u[0] == username_input and u[1] == password_input:
                    user = u
            if user is None:
                print("\nUsername atau password salah!")
                input("\nTekan Enter untuk lanjut...")
 
        # ---------- REGISTER ----------
        elif pilih == "2":
            os.system(perintah_clear)
            print("=" * 62)
            print("  REGISTER AKUN BARU")
            print("=" * 62)
            username_baru = input("Username (min 3 karakter, huruf/angka): ").strip().lower()
            password_baru = input("Password (min 4 karakter): ").strip()
            ulang_password = input("Ulangi password: ").strip()
 
            pesan = ""
            if len(username_baru) < 3 or not username_baru.isalnum():
                pesan = "Username minimal 3 karakter dan hanya boleh huruf/angka!"
            if pesan == "":
                for u in data_user:
                    if u[0] == username_baru:
                        pesan = "Username sudah dipakai!"
            if pesan == "" and len(password_baru) < 4:
                pesan = "Password minimal 4 karakter!"
            if pesan == "" and ulang_password != password_baru:
                pesan = "Password dan ulangi password tidak sama!"
 
            if pesan == "":
                data_user.append([username_baru, password_baru, "user"])
                print("\nRegister berhasil! Silakan login.")
            else:
                print("\n" + pesan)
            input("\nTekan Enter untuk lanjut...")
 
        # ---------- KELUAR ----------
        elif pilih == "0":
            print("Terima kasih!")
            berjalan = False
 
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk lanjut...")
 
    # =================================================
    #  SUDAH LOGIN : MENU ADMIN / USER
    # =================================================
    else:
        username, _, role = user  # unpack
 
        # Data yang boleh diakses: admin = semua, user = miliknya saja
        milik = []
        for baris in data_panen:
            if role == "admin" or baris[5] == username:
                milik.append(baris)
 
        print("=" * 62)
        print(f"  MENU {role.upper()} - {username}")
        print("=" * 62)
        print("1. Tambah data panen")
        print("2. Lihat data panen")
        print("3. Ubah data panen")
        print("4. Hapus data panen")
        if role == "admin":
            print("5. Kelola pengguna")
        print("0. Logout")
        pilih = input("Pilih menu: ").strip()
 
        daftar = None        # list yang akan ditampilkan sebagai tabel
        judul_tabel = ""
 
        # ---------- CREATE ----------
        if pilih == "1":
            os.system(perintah_clear)
            print("=" * 62)
            print("  TAMBAH DATA PANEN")
            print("=" * 62)
 
            while True:
                nama = input("Nama tanaman         : ").strip().title()
                if nama != "":
                    break
                print("Nama tanaman tidak boleh kosong!")
 
            while True:
                teks = input("Jumlah panen (kg)    : ").strip().replace(",", ".")
                if teks.count(".") <= 1 and teks.replace(".", "", 1).isdecimal() and float(teks) > 0:
                    jumlah = float(teks)
                    break
                print("Jumlah harus angka lebih dari 0 (contoh: 25 atau 25.5)!")
 
            while True:
                tanggal = input("Tanggal (DD-MM-YYYY) : ").strip()
                valid = False
                bagian = tanggal.split("-")
                if (len(bagian) == 3 and bagian[0].isdecimal() and bagian[1].isdecimal()
                        and bagian[2].isdecimal() and len(bagian[0]) == 2
                        and len(bagian[1]) == 2 and len(bagian[2]) == 4):
                    hari = int(bagian[0])
                    bulan = int(bagian[1])
                    tahun = int(bagian[2])
                    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
                        hari_per_bulan[1] = 29
                    if 1 <= bulan <= 12 and 1 <= hari <= hari_per_bulan[bulan - 1]:
                        valid = True
                if valid:
                    break
                print("Tanggal tidak valid! Gunakan format DD-MM-YYYY (contoh: 14-10-2026).")
 
            while True:
                lokasi = input("Lokasi kebun         : ").strip().title()
                if lokasi != "":
                    break
                print("Lokasi kebun tidak boleh kosong!")
 
            if len(data_panen) == 0:
                id_baru = 1
            else:
                id_baru = data_panen[-1][0] + 1
            data_panen.append([id_baru, nama, jumlah, tanggal, lokasi, username])
            print("\nData panen berhasil ditambahkan!")
            input("\nTekan Enter untuk lanjut...")
 
        # ---------- READ (pilih jenis tampilan) ----------
        elif pilih == "2":
            os.system(perintah_clear)
            print("=" * 62)
            print("  LIHAT DATA PANEN")
            print("=" * 62)
            print("1. Tampilkan semua data")
            print("2. Tampilkan 5 data terbaru")
            print("3. Cari berdasarkan nama tanaman")
            print("0. Kembali")
            sub = input("Pilih: ").strip()
            if sub == "1":
                daftar = milik
                judul_tabel = "SEMUA DATA PANEN"
            elif sub == "2":
                daftar = milik[-5:]  # slicing
                judul_tabel = "5 DATA PANEN TERBARU"
            elif sub == "3":
                kata = input("Nama tanaman yang dicari: ").strip().lower()
                daftar = []
                for baris in milik:
                    if kata in baris[1].lower():
                        daftar.append(baris)
                judul_tabel = f"HASIL PENCARIAN: {kata}"
            elif sub != "0":
                print("Pilihan tidak valid!")
                input("\nTekan Enter untuk lanjut...")
 
        # ---------- UPDATE / DELETE (tampilkan tabel dulu) ----------
        elif pilih == "3":
            daftar = milik
            judul_tabel = "UBAH DATA PANEN"
        elif pilih == "4":
            daftar = milik
            judul_tabel = "HAPUS DATA PANEN"
 
        # ---------- KELOLA PENGGUNA (ADMIN) ----------
        elif pilih == "5" and role == "admin":
            kelola = True
            while kelola:
                os.system(perintah_clear)
                print("=" * 62)
                print("  KELOLA PENGGUNA (ADMIN)")
                print("=" * 62)
                for i in range(len(data_user)):
                    print(f"{i + 1}. {data_user[i][0]:<15} ({data_user[i][2]})")
                print("\n1. Hapus pengguna")
                print("0. Kembali")
                sub = input("Pilih: ").strip()
                if sub == "1":
                    nomor = input("Nomor pengguna yang dihapus: ").strip()
                    if not nomor.isdecimal() or int(nomor) < 1 or int(nomor) > len(data_user):
                        print("Nomor tidak valid!")
                    elif data_user[int(nomor) - 1][2] == "admin":
                        print("Akun admin tidak dapat dihapus!")
                    else:
                        dihapus = data_user.pop(int(nomor) - 1)
                        print(f"Pengguna '{dihapus[0]}' berhasil dihapus.")
                    input("\nTekan Enter untuk lanjut...")
                elif sub == "0":
                    kelola = False
                else:
                    print("Pilihan tidak valid!")
                    input("\nTekan Enter untuk lanjut...")
 
        # ---------- LOGOUT ----------
        elif pilih == "0":
            user = None
 
        else:
            print("Pilihan tidak valid!")
            input("\nTekan Enter untuk lanjut...")
 
        # =================================================
        #  TAMPILKAN TABEL (dipakai menu Lihat, Ubah, Hapus)
        # =================================================
        if daftar is not None:
            os.system(perintah_clear)
            print("=" * 71)
            print(f"  {judul_tabel}")
            print("=" * 71)
            if len(daftar) == 0:
                print("Belum ada data panen.")
            else:
                print(f"{KOLOM[0]:<4}{KOLOM[1]:<16}{KOLOM[2]:<14}{KOLOM[3]:<13}{KOLOM[4]:<14}{KOLOM[5]:<10}")
                print("-" * 71)
                total = 0
                for baris in daftar:
                    id_, nama, jumlah, tgl, lokasi, pencatat = baris  # unpack
                    print(f"{id_:<4}{nama:<16}{jumlah:<14.2f}{tgl:<13}{lokasi:<14}{pencatat:<10}")
                    total += jumlah
                print("-" * 71)
                print(f"Total panen : {total:.2f} kg  ({len(daftar)} catatan)")
 
            # Menu Lihat: cukup tampilkan saja
            if pilih == "2" or len(daftar) == 0:
                input("\nTekan Enter untuk lanjut...")
 
            # Menu Ubah / Hapus: minta ID
            else:
                id_input = input("\nMasukkan ID data: ").strip()
                idx = -1
                if id_input.isdecimal():
                    for i in range(len(data_panen)):
                        if data_panen[i][0] == int(id_input) and (role == "admin" or data_panen[i][5] == username):
                            idx = i
 
                if idx == -1:
                    print("Data tidak ditemukan atau bukan milik Anda!")
 
                # ---------- UPDATE ----------
                elif pilih == "3":
                    baris = data_panen[idx]
                    print("\nKosongkan (Enter) jika tidak ingin mengubah.")
 
                    nama_baru = input(f"Nama tanaman [{baris[1]}]: ").strip().title()
 
                    while True:
                        teks = input(f"Jumlah kg [{baris[2]}]: ").strip().replace(",", ".")
                        if teks == "":
                            jumlah_baru = None
                            break
                        if teks.count(".") <= 1 and teks.replace(".", "", 1).isdecimal() and float(teks) > 0:
                            jumlah_baru = float(teks)
                            break
                        print("Jumlah harus angka lebih dari 0!")
 
                    while True:
                        tanggal_baru = input(f"Tanggal [{baris[3]}]: ").strip()
                        if tanggal_baru == "":
                            break
                        valid = False
                        bagian = tanggal_baru.split("-")
                        if (len(bagian) == 3 and bagian[0].isdecimal() and bagian[1].isdecimal()
                                and bagian[2].isdecimal() and len(bagian[0]) == 2
                                and len(bagian[1]) == 2 and len(bagian[2]) == 4):
                            hari = int(bagian[0])
                            bulan = int(bagian[1])
                            tahun = int(bagian[2])
                            hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                            if tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0):
                                hari_per_bulan[1] = 29
                            if 1 <= bulan <= 12 and 1 <= hari <= hari_per_bulan[bulan - 1]:
                                valid = True
                        if valid:
                            break
                        print("Tanggal tidak valid! Gunakan format DD-MM-YYYY.")
 
                    lokasi_baru = input(f"Lokasi kebun [{baris[4]}]: ").strip().title()
 
                    if nama_baru != "":
                        baris[1] = nama_baru
                    if jumlah_baru is not None:
                        baris[2] = jumlah_baru
                    if tanggal_baru != "":
                        baris[3] = tanggal_baru
                    if lokasi_baru != "":
                        baris[4] = lokasi_baru
                    print("\nData panen berhasil diperbarui!")
 
                # ---------- DELETE ----------
                else:
                    yakin = input(f"Yakin hapus data '{data_panen[idx][1]}'? (y/n): ").strip().lower()
                    if yakin == "y":
                        del data_panen[idx]
                        print("Data panen berhasil dihapus!")
                    else:
                        print("Penghapusan dibatalkan.")
 
                input("\nTekan Enter untuk lanjut...")
 