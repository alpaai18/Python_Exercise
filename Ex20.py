import random
import numpy as np

total_numbers = int(input('Mau berapa angka di dalam list? '))
batas_bawah = int(input('Mau berapa batas bawahnya? '))
batas_atas = int(input('Mau berapa batas atasnya? '))

guess_number = int(input('Masukkan angka yang ingin dicek: '))

def guess(total_numbers, batas_bawah, batas_atas, guess_number):
    list_angka = np.random.randint(batas_bawah, batas_atas, size=total_numbers)
    list_angka.sort()
    
    print(guess_number in list_angka)
    print(list_angka)
        
guess(total_numbers, batas_bawah, batas_atas, guess_number)