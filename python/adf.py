employee = {}

# 1. Function to add employee
def add_employee(employee_ID, employee_Name, age, salary, department):
    employee[employee_ID] = {
        "name": employee_Name,
        "age": age,
        "salary": salary,
        "department": department
    }
    print(f"Employee {employee_Name} added successfully")

# 2. Function to view all the employees
def view_employee():
    if employee:
        for employee_ID, employee_details in employee.items():
            print("Employee ID:", employee_ID)
            print("Employee Details:", employee_details) 
    else:
        print("No employee added")

# Main menu function
def main():
    while True:
        print("Welcome to the employee management system")
        print("1. Add employee")
        print("2. View employee")
        print("3. Update employee")
        print("4. Delete employee")
        print("5. Save to file")
        print("6. Load the file")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            try:
                employee_ID = int(input("Enter the employee ID: "))
                employee_Name = input("Enter the employee Name: ")
                age = int(input("Enter the employee age: "))
                salary = int(input("Enter the salary: "))
                department = input("Enter the department: ")
                add_employee(employee_ID, employee_Name, age, salary, department)
            except ValueError:
                print("Invalid input. Please enter numbers where required.")
        
        elif choice == 2:
            view_employee()
         
        elif choice == 3:
            print("Update employee feature not implemented yet.")
        
        elif choice == 4:
            print("Delete employee feature not implemented yet.")
        
        elif choice == 5:
            print("Save to file feature not implemented yet.")
        
        elif choice == 6:
            print("Load the file feature not implemented yet.")
        
        elif choice == 7:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()