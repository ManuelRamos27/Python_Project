import sys
import random

# created a function to generate a random name
def main():

# print statement for the user to know what the program does
    print("This is a program that generates a random hacker name.")
    print("Let's create a cool hacker name.\n")
# created some  first names
    first = ('Baby','Big','Young','The','Black')
# created some last names
    last = ('Worm', 'Morty', 'Chapo','Cipher')

# created a while loop for the user to keep generating names
    while True :
        first_name = random.choice(first)
        last_name = random.choice(last)
        print('\n')
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print('\n')
        # ask the user if they want to try again
        try_again = input('\n Would you like to try again? (y/n): ')
        # if the user wants to try again, the program will continue
        # if the user does not want to try again, the program will lead user to exit
        if try_again.lower() == 'n':
            break
    # asks user to press enter to exit
    input('\n\n Press Enter to exit.')    

if __name__=="__main__":
    main()