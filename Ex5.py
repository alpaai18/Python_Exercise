import random

jumlah_angka_1              = int(input('Mau berapa angka untuk list pertama? '))
batas_bawah_list_pertama    = int(input('Mau berapa batas bawah angka untuk list pertama? '))
batas_atas_list_pertama     = int(input('Mau berapa batas atas angka untuk list pertama? '))

jumlah_angka_2              = int(input('Mau berapa angka untuk list kedua? '))
batas_bawah_list_kedua      = int(input('Mau berapa batas bawah angka untuk list kedua? '))
batas_atas_list_kedua       = int(input('Mau berapa batas atas angka untuk list kedua? '))

# list_pertama                = random.sample(range(batas_bawah_list_pertama, batas_atas_list_pertama), jumlah_angka_1)
# list_kedua                  = random.sample(range(batas_bawah_list_kedua, batas_atas_list_kedua), jumlah_angka_2)

# NOTES
''' Tidak bisa menggunakan random.sample karena itu didesain untuk menciptakan number secara unique.
    Sebagai alternatif kita bisa menggunakan random.choice dengan menambahkan variabel kedua dengan + 1
    serta memberikan k sebagai argumen yang mengatur jumlah range angka yang akan dilakukan generate'''

list_pertama                = random.choices(range(batas_bawah_list_pertama, batas_atas_list_pertama + 1), k = jumlah_angka_1)
list_kedua                  = random.choices(range(batas_bawah_list_kedua, batas_atas_list_kedua + 1), k = jumlah_angka_2)

list_akhir_2 = []

for x in list_pertama:
    if x in list_kedua:
        if x not in list_akhir_2:
            list_akhir_2.append(x)
print(list_akhir_2)