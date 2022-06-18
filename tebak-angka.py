import random
import os

os.system("clear||cls")

def tebak(x) :
    benar = random.randint(1, x)
    jawaban = 0
    batas = 0
    
    while (jawaban != benar) and (batas != 3) :
        try :
            jawaban = int(input("- Masukkan angka yang kamu tebak : "))
            
            if jawaban > benar :
                print("- Angka yang kamu masukkan masih lebih besar dari angka yang benar XD")

            elif jawaban < benar :
                print("- Angka yang kamu masukkan masih lebih kecil dari angka yang benar XD")
                
            else :
                print("- Woah kamu berhasil menebak angka yang benar nih. Selamat ya XD")
            batas += 1
            
        except :
            print("- Input yang kamu masukkan tidak tepat.")
            
    if batas == 3 :
        print("-------------------------------------------------------------------")
        print("- Yah, kamu sudah gagal menebak angkanya.\n  Kalau masih mau main jalankan lagi program ini ya.\n  Sampai jumpa di tebak-tebakan selanjutnya :*")
        print("-------------------------------------------------------------------")

try :
    batas_atas = int(input('- Masukkan nilai tertinggi yang akan kamu tebak! : '))
    if batas_atas <= 1 :
        print('- Input kamu tidak tepat. Masukkan angka yang lebih besar dari 1')
        
except :
    print('- Inputya harus berupa integer yang lebih besar dari 1')

print("- Kamu akan menebak bilangan di antara 1 sampai", batas_atas)
tebak(batas_atas)