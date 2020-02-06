def helloLoop(arg):
    if len(arg) > 4:
        print('Wow, that\'s a long first name!')
    else:
        print('Your name is kinda short!')

print("Hello Friend, what is your name?")
name = input()
helloLoop(name)