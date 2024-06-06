import random
import time

from transliterate import translit

print("Введите год:")
year = input()
print("Введите факультет:")
dep = input()
print("Введите группу:")
group = input()
print("Введите курс:")
course = input()

start_time = time.time()

file = open("names.txt", "r")
ofile = open("names.csv", "w")

ofile.write(';'.join(
    ["username", "password", "first name", "last name", "email", "city", "maildisplay", "course", "group"]) + '\n')

names = file.readlines()

file.close()

for name in names:
    [lname, fname, mname] = name.rstrip("\n").split()
    username = dep.lower() + year + translit(fname[0] + mname[0] + lname, "ru", reversed=True)
    password = ''.join(random.choice("0123456789") for i in range(4))
    email = username + "@fiztest.gsu.by"
    ofile.write(';'.join([username, password, fname + ' ' + mname, lname, email, "Гомель", "0", course, group]) + '\n')

ofile.close()

end_time = time.time()
execution_time = end_time - start_time

print(f"Время выполнения программы: {execution_time} секунд")
