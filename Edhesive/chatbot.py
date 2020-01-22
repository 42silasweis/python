from random import randrange
random1 = (randrange(10))
random2 = (randrange(10))
random3 = (randrange(10))
random4 = (randrange(10))
random5 = (randrange(10))
print (random1)
print (random2)
print (random3)
print (random4)
print (random5)

name1 = input("What is your first name?" )
name2 = input("What is your last name?")

print ("Hi there, " + name1 + " " + name2 +", nice to meet you!")

age = int(input("How old are you? "))

print (str(age) + " is a good age.")

if(age > 16):
    if(random2 < random5):
        print("You are old enough to drive.")
    elif(random4 > random1):
        print("Old enough to drive you are.")
    else:
        print("You appear to be old enough to drive.")
if(age < 16):
    if(random1 < random3):
        print("You cannot drive yet since you are too young")
    elif(random5 < random2):
        print("You are too young to drive")
    else:
        print("You are not old enough to drive")

if(random4 > random1):
    feel1 = input("So, Pascal, how are you today? ")
elif(random5 < random3):
    feel1 = input("So, Pascal, how do you feel today? ")
else:
    feel1 = input("So, Pascal, how are you feeling today? ")

if(random1 > random2):
    print ("You are " + feel1)
elif(random3 < random5):
    print("You say you are " + feel1)
else:
    print("Feeling you are " + feel1)

if(feel1 == "Happy" or feel1 == "happy"):
    print ("That is good to hear.")
elif(feel1 == "Sad" or name1 == "sad"):
    print("I am sorry to hear that.")
else:
    print("That is interesting to hear.")

if(random1 < random3 or random5 > random2):
    feel2 = input("Tell me more. ")
elif(random4 > random2 or random5 > random1):
    feel2 = input("Please tell me more. ")
else:
    feel2 = input("Could you tell me more? ")
#print (feel2)

if(feel2 == "Happy" or feel2 == "happy"):
    print ("That's good to hear.")
elif(feel1 == "Sad" or name1 == "sad"):
    print("I am sorry to hear that.")
else:
    print("That is interesting to hear.")


if(random3 < random5):
    print ("Well, "+ name1 + ", it has been nice chatting with you.")
elif(random4 > random3):
    print ("Well, "+ name1 + ", I enjoyed chatting with you.")
else:
    print ("Well, "+ name1 + ", it was nice talking to you.")
