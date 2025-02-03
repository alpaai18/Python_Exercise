first_number = float(input('Masukkan angka pertama : '))
second_number = float(input('Masukkan angka kedua : '))

output_number_first = first_number % 4

output_number_second = first_number % second_number

if output_number_first == 0 and output_number_second == 0:
    print("Angka yang dimasukkan merupakan kelipatan 4 dan merupakan angka genap")
elif output_number_first != 0 and output_number_second == 0:
    print("Angka yang dimasukkan merupakan angka genap")
elif output_number_first != 0 and output_number_second != 0:
    print("Angka yang dimasukkan merupakan angka ganjil")
