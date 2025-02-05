import getpass

while True:
    pre_input = str(input('Apakah ingin mulai game nya sekarang? '))
    
    if pre_input == 'yes' or pre_input == 'y' or pre_input == 'ya' or pre_input == 'iya':
        input_1 = getpass.getpass(prompt='player 1 : ').lower()
        input_2 = getpass.getpass(prompt='player 2 : ').lower()
                
        match input_1:
            case 'rock' | 'batu':
                match input_2:
                    case 'rock' | 'batu':
                        print()
                        print('Hasilnya Seri')
                    case 'paper' | 'kertas':
                        print()
                        print('Hasilnya Player 2 win')
                    case 'scissor' | 'gunting':
                        print()
                        print('Hasilnya Player 1 win')
                    case _:
                        print()
                        print('tolong berikan input antara scissor/paper/rock atau gunting/kertas/batu')
                        
            case 'paper' | 'kertas':
                match input_2:
                    case 'rock' | 'batu':
                        print()
                        print('Hasilnya Player 1 win')
                    case 'paper' | 'kertas':
                        print()
                        print('Hasilnya Seri')
                    case 'scissor' | 'gunting':
                        print()
                        print('Hasilnya Player 2 win')
                    case _:
                        print()
                        print('tolong berikan input antara scissor/paper/rock atau gunting/kertas/batu')
                
            case 'scissor' | 'gunting':
                match input_2:
                    case 'rock' | 'batu':
                        print()
                        print('Hasilnya Player 2 win')
                    case 'paper' | 'kertas':
                        print()
                        print('Hasilnya Player 1 win')
                    case 'scissor' | 'gunting':
                        print()
                        print('Hasilnya Seri')
                    case _:
                        print()
                        print('tolong berikan input antara scissor/paper/rock atau gunting/kertas/batu')

            case _:
                print()
                print('tolong berikan input antara scissor/paper/rock atau gunting/kertas/batu')
                
        while True:
            
            post_input = str(input('Apakah mau main lagi? '))
            
            if post_input == 'yes' or post_input == 'y' or post_input == 'ya' or post_input == 'iya':
                print('Oke Ayo Main Lagi')
                print()
                break
            elif post_input == 'no' or post_input == 'n' or post_input == 'tidak':
                print('Sampai jumpa di lain waktu')
                print()
                exit() # ini built-in function untuk langsung terminate program
            else:
                print('Input tidak valid. Tolong berikan inputan (yes/y/ya/iya) atau (no/n/tidak)')
                print()
                
    elif pre_input == 'no' or pre_input == 'n' or pre_input == 'tidak':
        print('Sampai jumpa di lain waktu')
        print()
        break
    else:
        print('Input tidak valid. Tolong berikan inputan (yes/y/ya/iya) atau (no/n/tidak)')
        print()

# NOTES
'''
Kenapa pakai getpass bukan pakai input?

agar diterminal hasil ketikan player 1 dan player 2 tidak dimunculkan

'''