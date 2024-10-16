age = int(input("how old are you?"))
student = (input("are you a student?")).strip().lower()
if age < 12 or age >= 65:
    price = 5
elif 12<= age <= 64 and student == ("yes"):
    price = 8
elif 12<= age <= 64 and student == ("no"):
     price = 10

print(f"the price of your ticket is £{price}")

