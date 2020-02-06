# Function Logic

def introFunction(arg):
    while(arg != 'y'):
        if arg == 'stop':
            print('No, you stop. Party pooper.')
        print('Are you sure? It\'ll be a good one!')
        arg = input()
    


# Game Text

print("********************************************");
print("***** Welcome to the Rockport Limited! *****");
print("***Are you ready to begin your adventure?***")
print("********************************************");

introFunction(input())