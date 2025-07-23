import random
name=input("enter the name:")
name_list=name.split(",")
random_choice=random.choice(name_list)
print(random_choice)   