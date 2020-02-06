# Function Logic

def introFunction(arg):
    while(arg != 'yes'):
        if arg == 'stop':
            print('No, you stop. Party pooper.')
        elif arg == 'dab':
            print('*dabs back*')
        else:
            print('Are you sure? It\'ll be a good one!')
            
        arg = input()
    print('Good! Let us begin then..... \n');

def wagonInteraction(arg):

    


# Game Text

print("********************************************");
print("***** Welcome to the Rockport Limited! *****");
print("***Are you ready to begin your adventure?***")
print("********************************************");

introFunction(input())

print("Our story begins as you ride into town, on a wagon with several other rough-looking individuals...")
print("You don't know any of their names, backgrounds, or where they came from. What do you do? \n")
