decision_number = int(input("Masukkan angka penentu untuk list baru : "))

original_list = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]

new_list = [x for x in original_list if x < decision_number]

print(new_list)


# MISS THINKING FROM SOLUTION

# sorted_list = new_list.sort()     It would be None because sort() is not return any values

new_list.sort()                   # This is the right way to using sort()

print(new_list)

