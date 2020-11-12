print ("==================================================")
print ("Selamat Datang Di Aplikasi Menghitung Energi Benda")
print ("==================================================")

print ("--------------------------------")
nama = str(input ("Masukkan Nama Anda ="))
nim = int (input ("Masukkan NIM Anda ="))
print ("--------------------------------")

def awal() :
    print ("Program Menghitung Energi Benda :\n 1.Energi Potensial\n 2.Energi Kinetik\n 3.Energi Mekanik")
    p = int(input("Masukkan Pilihan Anda = "))

    if p == 1 : 
            EP()
            loop()
    elif p == 2 :
            EK()
            loop()
    elif p == 3 :
            EM()
            loop()
    else : 
        salah()
        loop()       

def EP() :
    print ("________________________________________________________________")
    print ("1.Menghitung Energi Potensial")
    m = int (input (" Masukkan Massa Benda (Kg) ="))
    g = int (input (" Masukkan Gravitasi Bumi (m/s2) ="))
    h = int (input(" Masukkan Ketinggian Benda (m) ="))
    ep = m*g*h 
    print (" Energi Potensial Benda Tersebut Adalah =",ep,"Joule")
def EK() :
    print ("________________________________________________________________")  
    print ("2.Menghitung Energi Kinetik")
    M = float (input(" Masukkan Massa Benda (Kg) ="))
    v = float (input(" Masukkan Kecepatan Benda (m/s) ="))
    ek = 0.5*M*(v)**2
    print (" Energi Kinetik Benda Tersebut Adalah =",ek,"Joule")
def EM() :
    print ("________________________________________________________________")
    print ("3.Menghitung Energi Mekanik")
    EP = int (input(" Masukkan Jumlah Energi Potensial Benda ="))
    EK = float (input(" Masukkan Jumlah Energi Kinetik Benda ="))
    em = EP + EK
    print (" Energi Mekanik Benda Tersebut Adalah =",em,"Joule")

def loop() : 
    print ("________________________________________________________________")
    LOOP = str(input("Apakah Anda Ingin Mengulang ? (ya/tidak)"))
    if LOOP == "ya" :
        awal()
    else :
        akhir()

def salah() :
    print ("******************************")
    print ("!! Tidak Tersedia Pada Menu !!")
    print ("******************************")


def akhir() :
    print ("===========================================")
    print ("Terima Kasih Telah Menggunakan Aplikasi Ini") 
    print ("===========================================")     
awal()
