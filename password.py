import random
import datetime

pass_length = int(input("enter the length of password: "))
char_sequence = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = "".join(random.sample(char_sequence, pass_length))
print(password)

current_time = datetime.datetime.now()

with open("security_key.txt", "a") as file:
    file.write("\n" + password + " " + str(current_time))
