batas_angka = int(input('Masukkan angka yang ingin anda ketahui divisor nya: '))

list_awal = [x for x in range(1, batas_angka+1)]
list_divisor = []

for i in list_awal:
    if batas_angka % i == 0:
        list_divisor.append(i)
    
print(list_divisor)