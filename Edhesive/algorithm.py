a = int(input("Enter side A: "))#11
b = int(input("Enter side B: "))#2
c = int(input("Enter side C: "))#4
d = int(input("Enter side D: "))#7
e = int(input("Enter side E: "))#1

aminusc = a - c
areatriangle = (0.5*(aminusc)*e)
#print(areatriangle)#debugging
areassquarebytriangle = (d - b - e)*aminusc
bigtriangle = b*a

total = areatriangle + areassquarebytriangle + bigtriangle
print(float(total))