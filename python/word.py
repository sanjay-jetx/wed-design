1. Importing the Random Module
import random
2. Getting the User's Name, and Greeting the User
The program asks the user for their name using the input() function. This name is stored in the variable name.

name = input("What is your name? ")
print("Good Luck ! ", name)
3. List of Words and Choosing a Random Word
A list of possible words for the guessing game is defined. These words are strings stored in a list called words. Also, the program selects a random word from the words list using random.choice(). The selected word is stored in the variable word.

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
4. Prompting the User to Guess
The program prompts the user to start guessing the characters of the randomly chosen word.

print("Guess the characters")
5. Initializing Guesses and Turns
guesses: An empty string that will hold all the characters guessed by the user.
turns: The number of attempts the user has to guess the word. Initially set to 12.
guesses = ''
turns = 12
6. The Main Game Loop
This while loop runs as long as the user has remaining turns. Inside the loop, the user will be prompted to guess characters.

while turns > 0:
6.1. Checking Each Character in the Word
failed = 0: A counter for the number of characters that have not been correctly guessed.
The for loop iterates through each character in the word.
If the character has been guessed (i.e., it is in guesses), it is displayed.
If the character has not been guessed, an underscore (_) is displayed, and failed is incremented.
failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1
6.2. Checking if the User Has Won
If failed is 0, it means all characters in the word have been guessed correctly. The user wins, and the correct word is displayed. The game ends with a break statement.

if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break
6.3. Prompting for the Next Guess
The user is prompted to guess a character.
The guessed character is added to the guesses string.
guess = input("guess a character:")
    guesses += guess
6.4. Handling Incorrect Guesses
If the guessed character is not in the word, the number of turns decreases by 1.
A "Wrong" message is displayed, along with the number of remaining guesses.
if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
6.5. Checking if the User Has Lost
If the user runs out of turns, the game ends with a "You Lose" message.

if turns == 0:
            print("You Loose")
7. Ending the Game
The game loop will end either when the user guesses the word correctly (all characters are guessed) or when the user runs out of turns.
Complete Code

import random

name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)
        break

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")