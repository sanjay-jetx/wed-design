employee={}
#1.Function to add employee
def add_employee(employee_ID,employee_Name,age,salary,department):
    employee[employee_ID]={
        "name":employee_Name,
        "age":age,
        "salary":salary,
        "department":department
    }
    print(f"employee {employee_Name} added successfully")

#2.Function to view all the employee
def view_employee():
    if employee:
        for employee_ID,employee_details in employee.items():
            print("employee ID:",employee_ID)
            print("employee_details:",employee_details) 
    else:
        print("no employee added")
#3 update employee details
def update_employee(employee_ID,employee_Name=None,age=None,salary=None,department=None):
    try:
        if employee_ID in employee:
            if employee_Name:
                 employee[employee_ID]["name"]=employee_Name
            if age:
                employee[employee_ID]["age"]=age
            if salary:
                employee[employee_ID]["salary"]=salary
            if department:
                employee[employee_ID]["department"]=department
            print("successfully updated")
        else:
            print(f"employee ID {employee_ID}not found")
    except KeyError as e:
        print(f"error updating employee details+")
# delete the employee details
def remove_employee(employee_ID):
    try:
        emp=employee.pop(employee_ID)
        print(f"employee{emp['name']} removed successfully")
    except KeyError:
        print("not found")
        
#function to save employee data to a file
def save_to_file(filename):
    try:
        with open(filename,'w') as file:
            for employee_ID,details in employee.items():
                line=f"{employee_ID} :-> {details['name']},{details['age']},{details['salary']},{details['department']} \n"
                file.write(line)
        print("employee data saved successfully")
    except Exception as e:
        print("error")
 #function to load the employee data
def load_the_file(filename):
    try:
        with open(filename, 'r') as file:
            global employee
            employee = {}

            for line in file:
                # Split ID and details
                id_part, details_part = line.strip().split(':->')
                employee_ID = int(id_part.strip())
                employee_Name, age, salary, department = [x.strip() for x in details_part.strip().split(',')]

                employee[employee_ID] = {
                    "name": employee_Name,
                    "age": int(age),
                    "salary": int(salary),
                    "department": department
                }

        print("employee data added successfully")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error loading file: {e}")

#main menu function
def main():  
    while True:
        
        print("welcome to the employee management system")
        print("1.Add employee")
        print("2.View employee")
        print("3.Update employee")
        print("4.delete employee")
        print("5.save to file")
        print("6.load the file")
        print("7.exit")
        try:
            choice=int(input("enter your choice"))
        except valueError:
            print("invalid input")
            continue
        
        if(choice == 1):
            employee_ID=int(input("enter the employee ID :"))
            employee_Name=input("enter the employee Name :")
            age=int(input("enter the employee age:"))
            salary=int(input("enter the salary :"))
            department=input("enter the department :")
            add_employee(employee_ID,employee_Name,age,salary,department)   
        
        elif(choice == 2):
            view_employee()
         
        elif(choice == 3):
             employee_ID=int(input("enter the employee ID :"))
             employee_Name=input("enter the new name (leave the blank to skip )")
             age=int(input("enter the new age "))
             salary=int(input("enter the new salary"))
             department=input("enter the new department")
             update_employee(employee_ID,employee_Name,age,salary,department)  
        
        elif(choice == 4):
            
            employee_ID=int(input("enter the employee ID"))
            remove_employee(employee_ID)
         
        elif(choice == 5):
            filename = input("enter the file name to save ")
            save_to_file(filename)
            
        
        elif(choice == 6):
           filename =  input("enter the file name to load the file : ")
           load_the_file(filename)
        
        elif(choice == 7):
            print("exit")
            break
        else:
            print("enter the valid option")
main() 