current_temperature=int(input("enter the input"))
if(current_temperature<0):
    print("Stay inside and drink hot chocolate")
elif(current_temperature>=0 and current_temperature<10):
    print("Wear a coat and go for a walk")
elif(current_temperature>=10 and current_temperature<20):
    print("perfect weather for a jog")
elif(current_temperature>=20 and current_temperature<30):
    print("ideal for a panic")
else:
    print("stay cool and drink plenty of water")