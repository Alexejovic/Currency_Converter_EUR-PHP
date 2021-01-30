print("press 1 for EUR to PHP:")
print("press 2 for PHP to EUR:")
x = input()
if int(x) == 1:
    print ("Now enter the amount you want to convert:")
    y = input()
    a = str(round(float(y) * 58.34, 2))
    print (a + " PHP")
elif int (x) == 2:
    print ("Now enter the amount you want to convert:")
    y = input()
    b = str(round(float(y) * 0.0172, 2))
    print (b + " PHP")
