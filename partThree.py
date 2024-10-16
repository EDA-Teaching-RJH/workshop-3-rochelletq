score = int(input("score:"))
if 90 <= score <= 100:
    print("you got an A")
elif 80 <= score <= 89:
    print ("you got a B")
elif 70 <= score <= 79:
    print ("you got a C")
elif 60 <= score <= 69:
    print ("you got a D")
elif score < 60:
    print ("you got an F")
else:
    print ("fail")
