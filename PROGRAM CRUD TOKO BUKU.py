import os
import time
Daftar = ["SANG PEMIMPI","BUMI MANUSIA","NONVERSATION","AROMA KARSA","DEAR NATHAN"]
HargaBuku = [90000,85000,98000,99000,85000]
subtotal =[]
def clear_screen():
   os.system('cls' if os.name == 'nt' else 'clear')

def awal():
    print("="*40)
    print("\t <<<Selamat Datang>>>")
    print("\t    <<<<<kasir>>>>>")
    print("\t<<<KARTONO BOOKSTORE>>>")
    print("="*40)
    login()

def login():
    print("\t---Silahkan Login---")
    user = "Fathia"
    user2 = "Mira"
    user3 = "Rifky"
    password = 1234
    Login = str(input("Masukkan Username anda: "))
    Pass = int(input("Masukkan Password     : "))

    if Login == user and Pass == password:
        print("\tLogin Berhasil")
        print("\tSelamat Datang")
        input("Tekan ENTER untuk melanjutkan.....")
        menu()
    elif Login == user2 and Pass == password:
        print("\tLogin Berhasil")
        print("\tSelamat Datang")
        input("Tekan ENTER untuk melanjutkan.....")
        menu()
    elif Login == user3 and Pass == password:
        print("\tLogin Berhasil")
        print("\tSelamat Datang")
        input("Tekan ENTER untuk melanjutkan.....")
        menu()
    elif Login == user and Pass != password:
        loop1()
    elif Login == user2 and Pass != password:
        loop1()
    elif Login == user3 and Pass != password:
        loop1() 
   elif Login != user and Pass == password:
        loop2()
  elif Login != user2 and Pass == password:
       loop2()
   elif Login != user3 and Pass == password:
       loop2()
   else:
      loop3()
    
def loop1():
    clear_screen()
    print("Maaf Password yang anda masukkan SALAH")
    login()
def loop2():
    clear_screen()
    print("Maaf Username yang anda masukkan SALAH")
    login()
def loop3():
    clear_screen()
    print("Username dan Password anda SALAH")
    login()

def menu():
    clear_screen()
    print("\t---pilih menu---")
    print("-"* 44)
    print("[1] Kasir")
    print("[2] Lihat Daftar")
    print("[3] Daftar Baru")
    print("[4] Edit Daftar")
    print("[5] Hapus Daftar")
    print("[0] Keluar")
    Pilihan = int(input("Pilih menu> "))

    if(Pilihan == 1):
        kasir()
    elif(Pilihan == 2):
        show_data()
        Kembali_menu()
    elif(Pilihan == 3):
       insert_data()
       Kembali_menu()
   elif(Pilihan == 4):
       edit_data()
       Kembali_menu()
   elif(Pilihan == 5):
       delete_data()
       Kembali_menu()
   elif (Pilihan == 0):
       keluar()
        time.sleep(5)
        exit()
    else:
        print("Pilihan Salah")
        Kembali_menu()

def show_data():
    clear_screen()
    if len(Daftar)<=0:
         print("Belum Ada Data")
    else:
        for indeks in range(len(Daftar)):
            print([indeks+1],Daftar[indeks])
            print(HargaBuku[indeks])

def insert_data():
    clear_screen()
    show_data()
    buku_baru = str(input("Judul>"))
    Harga_baru = int(input("Harga>"))
    Daftar.append(buku_baru)
    HargaBuku.append(Harga_baru)
    print ("Daftar Berhasil Disimpan")

def edit_data():
    clear_screen()
    show_data()
    indeks = int (input("Input code buku>>"))
    if(indeks > len(Daftar)):
        print ("Code Salah")
    else:
        Judul_Baru = str(input("Judul>"))
        harga_baru = int(input("Harga>"))
        Daftar[indeks-1] = Judul_Baru
        HargaBuku[indeks-1] = harga_baru
        print ("Daftar Berhasil Disimpan")

def delete_data():
    clear_screen()
    show_data()
    indeks = int (input("Input code buku>>"))
    if(indeks > len(Daftar)):
        print ("Code Salah")
    else:
       Daftar.remove(Daftar[indeks-1])
       HargaBuku.remove(HargaBuku[indeks-1])
       print ("Daftar Berhasil Dihapus")

def Kembali_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    menu()

def Kembali_kasir():
    print("\n")
    kasir()

def Trims():
    print("-"* 46)
    print("\tTerima kasih telah Berbelanja")
    print("\t             Di")
    print("\t   <<<KARTONO BOOKSTORE>>>")
    print("-"* 46)

def keluar():
    clear_screen()
    print("\tAnda Keluar Dari Aplikasi")
    print("-"* 40)

def loop():
    jawab=str (input("Ingin Membeli Lagi ? (ya/tidak)"))
    if jawab == 'ya':
        kasir()
    elif jawab == 'tidak':
        print("_"* 40)
    else:
       print("pilihan hanya ya/tidak")
       loop()

def lagii():
        lagi = str(input("tetap membeli(ya/tidak)>>> "))
        if lagi == 'ya':
            Kembali_kasir()
        elif lagi == 'tidak':
            loop()
        else:
            print("pilihan hanya ya/tidak")
            lagii()

def kasir():
    total = 0
    clear_screen() 
    print("-"* 40)
    show_data()
    codebukuu= int(input("Masukkan Kode Buku>"))
    jumlah = int (input("Masukkan Jumlah Buku>"))
    if(codebukuu > len(Daftar)or jumlah<=0):
        print ("Inputan Salah")
        lagii()

    else:
        subtot =(HargaBuku[codebukuu-1]*jumlah)
        print ("Judul Buku:",Daftar[codebukuu-1])
        print (" Subtotal Harga :",subtot)
        subtotal.append(subtot)
        for i in range(len(subtotal)):
            total = subtotal[i]+total
        print("Total :",total)
        loop()
        
        x = 1
        while (x==1):
            try:
                print("Total :",total)
                bayar = float(input("Pembayaran> "))
            except ValueError:
                Kembali_kasir()

            if(bayar >= total):
                print("Kembalian: Rp. %d" % (bayar-total))
                x = 0
                Trims()
                subtotal.clear()
                Kembali_menu()
            else:
                print("Uang Yang Diberikan Tidak Cukup")
                x = 1
            
awal()