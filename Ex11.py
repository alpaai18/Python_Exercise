def prima(num = 'Angka berapa yang mau di cek? '):
    num = int(input(num))
    
    indicator = 0
    
    divider = [x for x in range(2, num)]
    
    for x in divider:
        if num % x == 0:
            indicator += 1
    if num > 1:        
        if num % 1 == 0 and num % num == 0 and indicator == 0:
            print('angka {} termasuk kedalam bilangan prima'.format(num))
        else:
            print('angka {} tidak termasuk kedalam bilangan prima'.format(num))
    else:
        print('Pastikan angka yang dicantumkan itu lebih besar dari 1')
        
prima()