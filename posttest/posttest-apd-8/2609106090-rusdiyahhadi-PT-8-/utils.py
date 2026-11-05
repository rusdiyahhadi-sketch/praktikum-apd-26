import os

def input_berat():
    while True:
        try:
            teks = input("Jumlah (kg): ").strip().replace(",", ".")
            try:
                berat = float(teks)
            except ValueError:
                raise ValueError("Jumlah harus berupa angka!")
            if berat <= 0:
                raise ValueError("Jumlah harus lebih dari 0!")
        except ValueError as e:
            print("Input salah:", e)
        else:
            return berat

def bersihkan_layar():
     os.system("cls" if os.name == "nt" else "clear")
     
        