kalimat = str(input('Masukkan kalimat yang ingin di re-order: '))

list_kalimat = kalimat.split()

list_baru = [x for x in list_kalimat[::-1]]

list_baru = ' '.join(list_baru)

print()
print(kalimat)
print(list_baru)
