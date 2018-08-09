# Bite size project to harness the excitement around my proto-niece/nephew
# to teach concepts to my siblings!

import string
# To get specifics of this library, just uncomment this line!
#print(f"{help(string)}")
# And to get help on specific members/properties/functions:
#print(f"{string.ascii_letters}")
#print(f"{string.ascii_lowercase}")

import random
# Learn more about random:
#print(f"{help(random)}")
#print(f"{random.choice('These are the options for a random character!')}")
#print(f"{random.choice(string.ascii_lowercase)}")

# To clear the screen for the user later on!
import os

# Start counting the number of letter for the name
iter = 0 
# Set the input constraints to empty
name = input_flag = ''
while input_flag != '3':
    # Give the instructions and get the input from the user
    print(f"Current number of letters: {len(name)}")
    print(f"Enter a letter for this letter's constraints: ")
    input_flag = input("1 for vowel, 2 for consonant, 3 to finish, or any letter for that letter. ")

    # Clear the screen for the user
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if the user wants a vowel
    if input_flag == '1':
        name += random.choice("aeiouy")
    # Check if the user wants a consonant
    elif input_flag == '2':
        name += random.choice('bcdfghjklmnpqrstvwxz')
    # Check if the user wants a specific character.
    elif input_flag != '3':
        name += input_flag
    # Debug statement
    #print(f"Current name: {name}")
    iter += 1

# Tell the user the name they get!
print(f"{name}")




# 