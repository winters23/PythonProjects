import random
n=100
to_be_guessed = int(n*random.random())+1
guess =0
while guess != to_be_guessed :
    guess = int(input("new number :"))
    if(guess >0):
        if guess > to_be_guessed:
            print("number too large")
        elif guess < to_be_guessed :
            print("number too small")
    else :
        print("sorry u r giving up")
        break
else :
    print("congratulation u made it")