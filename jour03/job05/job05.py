def calcule (num1, operator, num2):
    if operator == "+":
        print (num1 + num2)
    elif operator == "-":
        print (num1 - num2)
    elif operator == "*":
        print (num1 * num2)    
    elif operator == "/":
        if num2 != 0:
            print (num1 / num2)
        else:
            print ("impossible de diviser par 0")
    elif operator == "%":
        if num2 != 0:
            print (num1 % num2)
        else:
            print ("impossible de diviser par 0")
    else:
        print ("opérateur non valide")

calcule(12, "+", 15)
calcule(8, "-", 2)
calcule(4, "*", 6)
calcule(10, "/", 2)
calcule(14, "%", 7)
calcule(14, "%", 0)
calcule(14, "!", 0)


