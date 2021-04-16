# program pengurutan bilangan

a = 2.4
b = 3.2
c = 1.6
d = 7.2
e = 7.3

#masukkan dalam list
isi_data = [a,b,c,d,e]
print("isi list semua data adalah :", isi_data)
# nilai mutlak dari ketiga bilangan
print("nilai mutlak dari :", abs(a),abs(b),abs(c),abs(d),abs(e))

# pencarian nilai minimum dan maksimum
print("nilai terkecil dari semua bilangan adalah :", min(isi_data))
print("nilai terbesar dari semua bilangan adalah :", max(isi_data))

# pembulatan keatas angka yang berada dalam list
import math
print("nilai bulat dari a adalah :",math.ceil(a))
print("nilai bulat dari b adalah :",math.ceil(b))
print("nilai bulat dari c adalah :",math.ceil(c))
print("nilai bulat dari d adalah :",math.ceil(d))
print("nilai bulat dari e adalah :",math.ceil(e))
