# menghitung huruf dan memperbaiki judul
# contoh judul = KanCIL MenYUsuri mEnUJu sawAH

# input kalimat yang akan dijadikan judul
kalimat_judul = input("Masukkan kalimat yang akan dibuat judul : ")
a = kalimat_judul
#input huruf yang akan dihitung
huruf = input("masukkan huruf yang akan dihitung : ")
# karena judul menggunakan huruf besar maka menggunakan :
print("judul pembenahan menjadi :", a.upper())

# menghitung jumlah karakter pada judul
print("jumlah karakter dalam judul adalah (termasuk spasi) :", len(a))

# menghitung jumlah huruf a yang muncul
print("jumlah huruf ",huruf,"adalah : ",a.count(huruf)) #perhatikan besar kecil huruf