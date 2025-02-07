import random

list_pertama    = random.sample(range(0,15), 7)
list_kedua      = random.sample(range(0,15), 10)

answer_list = [x for x in list_pertama if x in list_kedua]
answer_list.sort()

print(list_pertama)
print(list_kedua)
print()
print(answer_list)