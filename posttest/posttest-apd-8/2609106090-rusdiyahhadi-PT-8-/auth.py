from data import data_user
import pwinput

def menu_awal():
    user = None
    while user is None:
        print("1. Login")
        print("2. Register")
        pilih_awal = input("Pilih: ").strip()
        if pilih_awal == "1":
            username = input("Username: ").strip()
            password = pwinput.pwinput("Password: ", mask="*").strip()
            if data_user.get(username) is not None and data_user[username]["password"] == password:
                user = username
            else:
                print("Username atau password salah!")
        elif pilih_awal == "2":
            username_baru = input("Username baru: ").strip()
            password_baru = pwinput.pwinput("Password baru: ", mask="*").strip()
            if username_baru == "" or password_baru == "":
                print("Username dan password tidak boleh kosong!")
            elif data_user.get(username_baru) is not None:
                print("Username sudah terdaftar!")
            else:
                data_user[username_baru] = {"password": password_baru, "akses": "user"}
                user = username_baru
                print("Register berhasil!")

    return user