# fizzBuzzSKW.py
import time

def main():
    for n in range(1,100):
        if(n % 3 != 0 and n % 5 != 0):
            print("\033[34m" + str(n))
        
        if(n % 2 == 0):
            time.sleep(0.5)
            print("\033[32m Fizz")
        if(n % 5 == 0):
            time.sleep(0.5)
            print("\033[31m Buzz")
        if(n % 3 == 0 and n % 5 == 0):
            time.sleep(0.5)
            print("\033[33m FizzBuzz")

if(__name__ == "__main__"):
    main()
    '''
    it counts 1 to 100
    I prevent it from printing n if either Fizz or Buzz is true
    then it will print Fizz if n % 3 == 0 or if n % 5 == 0
    and will print FizzBuzz if both happen to be true
    Just change from % 3 to % 5 pretty easy stuff
    Added ANSI code to the text strings to change their color.
    Notice when printing n it is blue but Fizz is Green and Buzz is Red
    and FizzBuzz is Yellow since Red and Green combined make Yellow.
    '''