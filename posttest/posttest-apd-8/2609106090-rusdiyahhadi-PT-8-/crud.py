from data import data_panen
from prettytable import PrettyTable

def cek_id(teks):
    try:
        id_p = int(teks)
        if data_panen.get(id_p) is None:
            raise ValueError("ID tidak ditemukan!")
    except ValueError:
        return None
    else:
        return id_p

def hitung_total(daftar):
    if len(daftar) == 0:
        return 0
    return daftar[0]["berat"] + hitung_total(daftar[1:])

def tampil_data():
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Tanaman", "Berat (kg)", "Tanggal", "Lokasi"]
    for id_p, detail in data_panen.items():
        tabel.add_row([id_p, detail["nama_tanaman"], detail["berat"], detail["tanggal"], detail["lokasi"]])
    print(tabel)