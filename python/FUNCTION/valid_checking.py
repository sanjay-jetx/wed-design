user_name="sanjay"
password=1234
user=input("enter the user_name :")
password1=int(input("enter the password :"))

def validate():
    if user_name==user :
        if password==password1:
            print("valid login")
            return True
    else:
        print("invalid")
        return False
    
validate()
a=validate()
print(a)