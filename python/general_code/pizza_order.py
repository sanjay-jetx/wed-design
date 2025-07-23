size=input("enter the size \s\m\l")
bill=0
if size == 's' or size == 'S':
    bill+=100
    print("you order small size pizza")
elif size == 'm' or size == 'M' :
    bill+=200
    print("you order medium size pizza")
else:
    bill+=300
    print("you order large size pizza")

 add_pepperoni=input("enter the yes or no")
 if  add_pepperoni == 'yes' or  add_pepperoni == 'YES':
     if size == 's' or size =='S':
         bill=bill+50
    else:
        bill=bill+50
else:
    print("do you want cheese ")
cheese=intput("enter do you want yes or no")
if cheese == 'yes' or cheese == 'YES':
    