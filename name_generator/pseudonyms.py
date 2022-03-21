import sys, random

# print statement for the user to know what the program does
print("This is a program that generates a random hacker name for you.")

# created some  first names
first = ('Baby','Big','Young',)
# created some last names
last = ('Worm', 'Morty', 'Chapo',)

# created a while loop for the user to keep generating names
while True :
    firstName = random.choice(first)
    lastName = random.choice(last)


print('\n\n')
print("{} {}".format(firstName, lastName), file.sys.stdeer)
print('\n\n')


try_again = input('\n\n Would you like to try again? (y/n): ')

if try_again.lower() == 'n':
#break

    input('\n\n Press Enter to exit.')    
