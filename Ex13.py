jumlah_fibo = int(input('\nmasukkan mau berapa angka yang digenerate untuk deret fibonacci? '))

def fibonnaci(jumlah_fibo):
    list_awal = [x for x in range(1, jumlah_fibo+1)]

    list_fibo = []
    penambah = 0

    for i in range(len(list_awal)):
        if i == 0:
            list_fibo.append(list_awal[i] + penambah)
        elif i == 1:
            penambah = -1
            list_fibo.append(list_awal[i] + penambah)
        else:
            list_fibo.append(list_fibo[i-2] + list_fibo[i-1])

    return list_fibo

print(f'\nBerikut merupakan {jumlah_fibo} deret angka fibonacci:\n{fibonnaci(jumlah_fibo)}\n')