import random 
secret_number = random.randint(1, 10)

number = -1

while number != secret_number:
  number = int(input("guess a number between 1 and 10 "))

if number > secret_number:
    print("too high")
elif number < secret_number:
    print("too low")
else:
    print("you guessed correct!")

print(f" The number was:{secret_number}")
