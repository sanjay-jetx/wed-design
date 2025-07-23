import random
print("welcome to the password generator !")
letters=['a','b','g','t','y','i']
numbers=['0','1','3','4','5','6']
symbols=['!','@','#','*','%']
letters_input=int(input("enter the numbers of letters you needed :\n"))
for i in range(letters_input):
    choice=random.choice(letters)
    print(choice,end="\n")
numbers_input=int(input("enter the numbers of letters you needed :\n"))
for i in range(numbers_input):
    choice=random.choice(numbers)
    print(choice,end="")