# file 3 : quadtratic_lambda.py

def quadratic_function(a,b,c):
    return lambda x: a*(x**2) + b*x + c

a1 = quadratic_function(1,2,1)
print(a1(1))
print("Input a,b and c from a quadratic equation in the form of")
print("x = ax^2 + bx + c")
#problem? idek
a = input("Input a ")
b = input("Input b ")
c = input("Input c ")
a2 = quadratic_function(a,b,c)
fx = a2(1)
print("f(x) = ",fx)
#quadratic files end here!
