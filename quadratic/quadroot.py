'''
quadroot.py SKW . Reference Amit Saha(Doing Math With Python)

I know i also typed in your comments and such but I did type all of this myself -SKW

Quadratic Calculator
D is the Discriminant of a quadratic equation . D = b^2 - 4ac
Try the folowing quations
y = x^2 + 2x +1 (1,2,1)
y = x^2 + 9    (1,0,9)
y = (5x^2 + 4x +2)
'''
def roots(a,b,c):
    D = (b*b - 4*a*c)
    print()
    print("D = " + str(D))
    if (D >= 0): #check for positive D
            print ("REAL ROOTS")
            D = D**0.5 # calculate square root of D
            x1 = (-b + D) / (2*a)
            x2 = (-b - D) / (2*a)
            print ("x1 = "+str(x1)+" x2 = "+str(x2))

    elif(D < 0): #check for negative D
            D = (D * -1)**0.5; #Change D to a positive.
            # Take square root of D then represent with "i"
            print("IMAGINARY ROOTS")
            print ("1x = -"+str(b/(2*a))+" - "+str(D/(2*a))+"i")
            print ("1x = -"+str(b/(2*a))+" + "+str(D/(2*a))+"i")
#The following has two underscores__ before and after name and main
if __name__ == '__main__':
        print("Input a,b and c for the quadratic (ax^2 + bx + c)")
        a = input("Enter a: ")
        b = input("Enter b: ")
        c = input("Enter c: ")
        roots(float(a), float(b), float(c))
'''
Your number inputs:
silas@Aegis:~/python$ python quadroot.py
Input a,b and c for the quadratic (ax^2 + bx + c)
Enter a: 5
Enter b: 4
Enter c: 2

D = -24.0
IMAGINARY ROOTS
1x = -0.4 - 0.4898979485566356i
1x = -0.4 + 0.4898979485566356i


silas@Aegis:~/python$ python quadroot.py
Input a,b and c for the quadratic (ax^2 + bx + c)
Enter a: 6
Enter b: 4
Enter c: 1
D = -8.0
IMAGINARY ROOTS
1x = -0.3333333333333333 - 0.23570226039551587i
1x = -0.3333333333333333 + 0.23570226039551587i
'''
