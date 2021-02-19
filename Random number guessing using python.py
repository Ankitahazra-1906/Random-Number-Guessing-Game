import random
number=random.randrange(1,100)
guess=int(input("Enter a number between 1 to 100: "))
while guess != number:
    if guess<number:
        print("Your guess is too low!")
        guess=int(input("Enter a number between 1 to 100: "))

    else: 
        print("Your guess is too high!")
        guess=int(input("Enter a number between 1 to 100: "))

    
print("Congratulations!You got it correct.")
print("Thanks for playing!")
