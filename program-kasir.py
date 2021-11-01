menu_makanan = ["Nasi Goreng pedas","Nasi Goreng Sosing","Nasi Bakar Ndower"]
menu_minuman = ["Es Kelapan Muda","Es Teh Dingin","Teh Hangat"]
menu_kopi = ["kopi Hitam","Kopi Susu","Kopi Lanang"]
keranjang = []
harga = []

def menu_utama():
    print("-------Daftar Menu------")
    print("========================")
    print(" 1. |    Makanan    | --")
    print(" 2. | Minuman Segar | --")
    print(" 3. |      Kopi     | --")
    print("========================")
    for var in keranjang:
        print(f"Penasan Anda : {var}")
    pilih1 = int(input("Pilih Nomer Jenis Pesanan Anda : "))
    if pilih1 == 1:
        daftar_makanan()
    elif pilih1 == 2:
        daftar_minuman()
    elif pilih1 == 3:
        daftar_kopi()
    else:
        print("Menu Belum Terdaftar !!")

def daftar_makanan():
    print("-----------------Daftar Makanan--------------")
    print("=============================================")
    print(" 1. |    Nasi Goreng Pedas  = Rp 12.000  | --")
    print(" 2. |    Nasi Goreng Sosis  = Rp 10.000  | --")
    print(" 3. |    Nasi Bakar         = Rp 15.000  | --")
    print("==================================")
    pilihan_makanan = int(input("Pilih Nomer Pesanan anda : "))
    if pilihan_makanan == 1:
        keranjang.append(menu_makanan[0])
        jumlah_makanan = int(input("Masukkan Jumlah Pesanan : "))
        total = 12000 * jumlah_makanan
        harga.append(total)
        tanya()
    elif pilihan_makanan == 2:
        keranjang.append(menu_makanan[1])
        jumlah_makanan1 = int(input("Masukkan Jumlah Pesanan : "))
        total1 = 10000 * jumlah_makanan1
        harga.append(total1)
        tanya()
    elif pilihan_makanan == 3:
        keranjang.append(menu_makanan[2])
        jumlah_makanan2 = int(input("Masukkan Jumlah Pesanan : "))
        total2 = 15000 * jumlah_makanan2
        harga.append(total2)
        tanya()

def daftar_minuman():
    print("--------------Daftar Minuman-------------")
    print("=========================================")
    print(" 1. |    Es kelapa Muda  = Rp 6.000  | --")
    print(" 2. |    Es Teh Dingin   = Rp 5.000  | --")
    print(" 3. |    Es Teh Hangat   = Rp 4.000  | --")
    print("==================================")
    pilihan_minuman = int(input("Pilih Nomer Pesanan anda : "))
    if pilihan_minuman == 1:
        keranjang.append(menu_minuman[0])
        jumlah_minuman = int(input("Masukkan Jumlah Pesanan : "))
        total3 = 6000 * jumlah_minuman
        harga.append(total3)
        tanya()
    elif pilihan_minuman == 2:
        keranjang.append(menu_minuman[1])
        jumlah_minuman1 = int(input("Masukkan Jumlah Pesanan : "))
        total4 = 5000 * jumlah_minuman1
        harga.append(total4)
        tanya()
    elif pilihan_minuman == 3:
        keranjang.append(menu_minuman[2])
        jumlah_minuman7 = int(input("Masukkan Jumlah Pesanan : "))
        total7 = 4000 * jumlah_minuman7
        harga.append(total7)
        tanya()

def daftar_kopi():
    print("--------------Daftar Kopi-------------")
    print("======================================")
    print(" 1. |    Kopi Hitam  = Rp 3.000   | --")
    print(" 2. |    Kopi Susu   = Rp 4.000   | --")
    print(" 3. |    Kopi Lanang = Rp 5.000   | --")
    print("==================================")
    pilihan_kopi = int(input("Pilih Nomer Pesanan anda : "))
    if pilihan_kopi == 1:
        keranjang.append(menu_kopi[0])
        jumlah_kopi = int(input("Masukkan Jumlah Pesanan : "))
        total4 = 3000 * jumlah_kopi
        harga.append(total4)
        tanya()
    elif pilihan_kopi == 2:
        keranjang.append(menu_kopi[1])
        jumlah_kopi1 = int(input("Masukkan Jumlah Pesanan : "))
        total5 = 4000 * jumlah_kopi1
        harga.append(total5)
        tanya()
    elif pilihan_kopi == 3:
        keranjang.append(menu_kopi[2])
        jumlah_kopi6 = int(input("Masukkan Jumlah Pesanan : "))
        total6 = 5000 * jumlah_kopi6
        harga.append(total6)
        tanya()

def tanya():
    pilihan = input("Apa Mau Tambah Menu (y/t) : ")
    if pilihan == "y":
        menu_utama()

    elif pilihan == "t":
        hasil()
        
    else:
        print("Pilih [y] untuk ya dan [t] untuk tidak")
    


def hasil():
    print("-------Pesanan Anda--------")
    print("===========================")
    print("Anda Memesan : {}".format(",".join([str(pesan) for pesan in keranjang])))
    jumlah = sum(harga)
    print("============================")
    print("Jumlah Pembayaran Anda : ", jumlah)
    print("===========================")

menu_utama()