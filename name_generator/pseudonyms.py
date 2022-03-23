import sys
import random


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
    
        try_again = input('\n Would you like to try again? (y/n): ')

        if try_again.lower() == 'n':
            break

    input('\n\n Press Enter to exit.')    

if __name__=="__main__":
    main()