'''
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old. 

Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
If you want to do this in a generic way, see exercise 39.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
(Hint: order of operations exists in Python)

Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)

'''


import datetime

user_name = str(input("Siapa nama Anda? "))
user_age = int(input("Berapa umur Anda? "))

access_realtime_datatime = datetime.datetime.now()

existing_year = access_realtime_datatime.year

user_100_year = 100 - user_age

year_for_100_old_user = int(existing_year + user_100_year)

print("Baik Bapak/Ibu {}, Anda akan masuk usia 100 tahun pada tahun {}".format(user_name, year_for_100_old_user))

# STATUS ANSWER : DONE