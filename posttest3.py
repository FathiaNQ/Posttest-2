print("-----------------------")
print( '    SELAMAT DATANG')
print ('    DI TOKO KUE SULE')
print("-----------------------")

print ('-'*30,"!! PROMO ALERT !!",'-'*38)
print ("|1. Setiap Pembelian Kue Keju Sebanyak 4-15 pcs Mendapat Potongan Harga Sebesar 10%   |")
print ("|2. Setiap Pembelian Kue Keju Sebanyak 16-25 pcs Mendapat Potongan Harga Sebesar 15%  |")
print ("|3. Setiap Pembelian Kue Coklat Sebanyak 5-20 pcs Mendapat Potongan Harga Sebesar 7%  |")
print ("|4. Setiap Pembelian Kue Coklat Sebanyak 21-35 pcs Mendapat Potongan Harga Sebesar 12%|")
print ('-'*87)

def menu():
    print ('MENU TOKO KUE SULE \n 1.KUE KEJU [Stok Kue : 25]\n 2.KUE COKLAT [Stok Kue :35]')
    pilihan = int(input('Masukkan Pilihan Anda :'))
    if pilihan == 1:
        print ('Harga 1 pcs kue keju = Rp 6000,-')
        kue_keju()
        loop()
    elif pilihan == 2:
        print ('Harga 1 pcs kue coklat = Rp 3500,-')
        kue_coklat()
        loop()
    else:
        print ("================================")
        print ('Maaf Pilihan Anda Belum Tersedia')
        print ("================================")
        loop()

def kue_keju():
    print("________________________________________________")
    K_Keju = int (input("Jumlah Kue Keju yang dibeli ="))
    if K_Keju >=1 and K_Keju <=25:
        Harga_K = 6000*K_Keju
        Diskon1 = (10/100)*Harga_K
        Diskon2 = (15/100)*Harga_K
        if K_Keju >=4 and K_Keju <=15:
            print ('Anda Mendapat Potongan Harga Sebesar 10%')
            print ('Harga Normal =' ,'Rp',Harga_K) 
            print ('Harga Setelah Diskon =', 'Rp',Harga_K-Diskon1)
        elif K_Keju >=16 and K_Keju <=25:
            print ('Anda Mendapat Potongan Harga Sebesar 15%')
            print ('Harga Normal =' ,'Rp',Harga_K) 
            print ('Harga Setelah Diskon =', 'Rp',Harga_K-Diskon2)  
        else:
            print ("Total Harga =", 'Rp',Harga_K)
    else:
        print ("-"*55)
        print("\tMaaf Pembelian Anda Melebihi Stock Toko\nToko Hanya Memproduksi Kue Keju Sebanyak 25 pcs Perhari")
        print ("-"*55)

def kue_coklat():
    print("________________________________________________")
    K_Coklat = int (input("Jumlah Kue Coklat yang dibeli ="))
    if K_Coklat >=1 and K_Coklat <=35:
        Harga_C = 3500*K_Coklat
        Diskon3 = (7/100)*Harga_C
        Diskon4 = (12/100)*Harga_C
        if K_Coklat >=5 and K_Coklat<=20:
            print ('Anda Mendapat Potongan Harga Sebesar 7%')
            print ('Harga Normal =' ,'Rp',Harga_C) 
            print ('Harga Setelah Diskon =', 'Rp',Harga_C-Diskon3)
        elif K_Coklat >=21 and K_Coklat<=35:
            print ('Anda Mendapat Potongan Harga Sebesar 12%')
            print ('Harga Normal =' ,'Rp',Harga_C) 
            print ('Harga Setelah Diskon =', 'Rp',Harga_C-Diskon4) 
        else:
            print ("Total Harga =", 'Rp',Harga_C)
    else:
        print ("-"*58)
        print("\tMaaf Pembelian Anda Melebihi Stock Toko\nToko Hanya Memproduksi Kue Coklat Sebanyak 35 pcs Perhari")
        print ("-"*58)

def loop():
    print("_______________________________________________")
    Beli = str(input("Ingin Membeli Kue lagi ? [ya/tidak]"))
    if Beli == 'ya':
        menu()
    else:
        Trims()

def Trims():
    print ("-"*32)
    print (" TERIMA KASIH TELAH BERBELANJA\n \tDI TOKO KUE SULE")
    print ("-"*32)

menu()

