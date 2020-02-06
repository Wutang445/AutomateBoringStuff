import random
print("Hello! What is your name?")
name = input();
print('Nice to meet you ' + name + '!')

secretNum = random.randint(1,20)
print('Well ' + name + ' , I\'m thinking of a number between one and twenty')

for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNum:
        print('Too low. Guess higher.')
    elif guess > secretNum:
        print('Too high, guess lower')
    else:
        break

if guess == secretNum:
    print('Hooray, you\'ve guessed the right number!')
else:
    print('Better luck next time, you couldn\'t guess my number.')