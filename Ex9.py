import random

while True:
    user_input = int(input('Silahkan tebak angka antara 1-9: '))
    
    wrong_guesses = 0
    right_guesses = 0
    
    random_number = random.randint(1, 9)
    if user_input > 0 and user_input == random_number and user_input < 10:
        right_guesses += 1
        print('Selamat tebakan anda benar')
        print()
        
    elif user_input > 0 and user_input < random_number and user_input < 10:
        wrong_guesses += 1
        print('Maaf tebakan angka anda terlalu rendah')
        print()
        
    elif user_input > 0 and user_input > random_number and user_input < 10:
        wrong_guesses += 1
        print('Maaf tebakan angka anda terlalu besar')
        print()
        
    else:
        print('Angka yang anda inputkan terlalu jauh dari range permainan. Silahkan inputkan angka diantara 1-9')
        print()
        
    while True:
        post_input = str(input('Apakah ingin bermain lagi? '))
        if post_input == 'yes' or post_input == 'y' or post_input == 'ya' or post_input == 'iya':
            print('Oke Ayo Main Lagi')
            print()
            break
        elif post_input == 'no' or post_input == 'n' or post_input == 'tidak':
            print('\nHasil permainannya adalah:\nJumlah tebakan benar : {} \nJumlah tebakan salah: {}\n'.format(right_guesses, wrong_guesses))
            print('Permainan yang baik. Sampai jumpa di lain waktu')
            print()
            exit() # ini built-in function untuk langsung terminate program
        else:
            print('Input tidak valid. Tolong berikan inputan (yes/y/ya/iya) atau (no/n/tidak)')
            print()