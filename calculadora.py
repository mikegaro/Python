num1 = raw_input("Ingresa un numero: ")
num2 = raw_input("Ingresa otro numero: ")

result = float(num1) + float(num2)
print("\nLa suma es: " + str(result))

result = float(num1)*float(num2)
print("\nEl producto es: " + str(result))

result = float(num1) - float(num2)
print("\nLa resta es: " + str(result))

if float(num2) == float(0):
    print("\nNo es posible hacer division")
else:
    result = float(num1)/float(num2)
    print("\nLa division es: " + str(result))
