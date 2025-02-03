# palindrome case string

kata = str(input("Masukkan kata yang ingin dicek apakah palindrom atau bukan : ")).lower()

list_kata = [x for x in kata]

list_kebalikan_kata = list_kata[::-1]

if list_kata == list_kebalikan_kata:
    print("kata tersebut termasuk kepada palindrom")
else:
    print("Kata yang diinputkan bukan termasuk kata palindrom")

print(list_kata)
print(list_kebalikan_kata)