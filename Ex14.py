import numpy as np

batas_bawah = int(input('Masukkan batas bawah untuk range yang diinginkan! '))
batas_atas = int(input('Masukkan batas atas untuk range yang diinginkan! '))
jumlah_angka = int(input('Masukkan jumlah angka yang ingin ada di list! '))

def remove_duplicates(batas_bawah, batas_atas, jumlah_angka):
    list_awal = np.random.randint(batas_bawah, batas_atas, size=jumlah_angka)

    list_akhir = []

    for x in list_awal:
        if x not in list_akhir:
            list_akhir.append(x)

    list_akhir.sort()
    
    return list_akhir

print(remove_duplicates(batas_bawah, batas_atas, jumlah_angka))
