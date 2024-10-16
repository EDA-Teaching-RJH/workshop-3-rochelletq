def numCalc():
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))

    while True:   
     operation = input("what operation would you like performed?(+, -, *, /, ^, %)")
   
     match operation:
       case "+":
        result = num1 + num2
        print(f"{num1} +{num2} = {result}")
       case "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
       case "*":
        result = num1 * num2 
        print(f"{num1} * {num2} = {result}")
       case "/":
        if num2 == 0:
          print("error cannot divide by zero")
        else:
         result = num1 / num2 
         print(f"{num1} / {num2} = {result}")
       case "^":
        result = num1 ** num2 
        print(f"{num1} ** {num2} = {result}") 
       case "%":
        if num2 ==0:
         print("error cannot divide by zero")
        else:
         result = num1 % num2 
        print(f"{num1} % {num2} = {result}")
       case _: 
        print ("you've entered an invalid operation")

numCalc()
  



