import random
user_choice = int(input("Enter 1 for Rock, 2 for Paper, 3 for Scissors: "))
bot = random.randint(1, 3)
print("Bot choice:", bot)
if user_choice == bot:
    print("Draw")
elif (user_choice == 1 and bot == 3) or \
     (user_choice == 2 and bot == 1) or \
     (user_choice == 3 and bot == 2):
    print("You won")
else:
    print("You lose")
