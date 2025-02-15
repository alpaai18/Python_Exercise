import numpy as np

def first_last_element(batas_bawah, batas_atas, jumlah_angka):
    
    generate_list = np.random.randint(batas_bawah,batas_atas, size=jumlah_angka).tolist()
    generate_list.sort()

    return [generate_list[0], generate_list[-1]]

batas_bawah = int(input('Masukkan batas bawah untuk range yang diinginkan! '))
batas_atas = int(input('Masukkan batas atas untuk range yang diinginkan! '))
jumlah_angka = int(input('Masukkan jumlah angka yang ingin ada di list! '))

print(first_last_element(batas_bawah, batas_atas, jumlah_angka))