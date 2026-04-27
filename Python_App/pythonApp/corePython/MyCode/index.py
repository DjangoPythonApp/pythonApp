# This line sets the total budget available for the project 
# to 150 .
PROJECT_BUDGET = 150

'''=========================================== DEPTRAMENT PART ==========================================='''
'''
Here we declear the memory of the deptramnet.
we assign it with the deptraments reference variable with empty dictonary.

'''


deptraments: dict[int,Deprament] = {}

'''
1 .Here we bulid the Department class, 
2 .The class has one constructor,
3 . inside it two instance reference variable one is dept id and dept name.

'''

class Deptrament:
  def __init__(self,dept_id,dept_name):
    self.dept_id = dept_id
    self.dept_name = dept_name


'''
Here we create a add_deptrament method,
 the help of this method we can add the name and unique id in the dept dict help of class dept.
'''

def add_deptrament():
  dept_name:str = input("Enter the deptrament name:")
  dept_id:int = max(deptraments.keys(),default=0)+1
  deptraments[dept_id] = Deptrament(dept_id,dept_name)
  print("Deptrament added!!")

'''
here we define another function name is view_deptrament(),
the purpose of this function is show the the id and deptrament name.
'''
def view_deptrament():
  if not deptraments:
    print("Deptrament is not found!!!")
  else:
    print("-"*5,"Deptraments","-"*5)
    for d in deptraments.values():
      print(f"{d.dept_id} | {d.dept_name}")


'''=========================================== END OF DEPTRAMENT PART ==========================================='''

'''=========================================== START OF EMPLOYEE PART ==========================================='''

'''
Here we create a reference variable that assign a empty dict,
the empty dict has a key, type of key is string and type of value is object of Employee class.
'''
employess:dict[str,Employee]={}

'''
Here we declear a class the name of the class is Employee,
 and its have a constructor that have a two formal arguments one is name another deptrament.
 and we assign it by self.anme ref var and self.deptrament ref var.
'''
class Employee:
  def __init__(self,name,deptrament):
    self.name = name
    self.deptrament = deptrament


'''
Here we define a function the name of the function is add_employee() the help of this function we can,
add the name of employee with the purticular deptrament.
'''
def add_employee():

  name:str = input("Enter the employee name:")

  view_deptrament()    

  dept_id:int = int(input("Enter the deptrament id:"))

  if dept_id not in deptraments:
    print("Invalid id!!!")
    return

  employess[name] = Employee(name, deptraments[dept_id])


'''
Here we add the employee with the corosponding deptrament with the help of dept id.
'''

def list_employee():

  if not employess:
    print("No employee found!!!!")
    return []

  print("-"*5,"Employess","-"*5)
  emp_list = []
  index = 1

  for dept in deptraments.values():
    print(f"\nDeptrament:{dept.dept_name}")
    found = False

    for emp in employess.values():
      if emp.deptrament == dept:
        print(f"\n{index}. {emp.name}")
        emp_list.append(emp)
        index+=1
        found = True

    if not found:
      print("No employees!!!")

  return emp_list

  
'''=========================================== END OF EMPLOYEE PART ==========================================='''

'''=========================================== ASSIGN EMPLOYEE ON PROJECT ADD ALSO TIME ==========================================='''


'''
here we create a reference variable type is dect and its store string as a key,
and Project class object as a value.
And assign it with empty list.
'''


projects: dict[str, Project] = {}



'''
Here we declear a class name of this class project , the class have a one constructor,
and one method. have one formal argument is name we assign it with the ref var is,
self.name. also declear a ref var name is self.employee and assign it with empty dict.

we also have a method name is add_work() have two formal parameter name is employee and
another is hours, 

ANOTHER METHOD TOTAL HOURS FOR CALCULATE TOTAL TIME


'''

class Project:
  def __init__(self, name):
    self.name = name
    self.employee_hours = {}

  def add_work(self, employee, hours):
        if employee in self.employee_hours:
            self.employee_hours[employee] += hours
        else:
            self.employee_hours[employee] = hours

  def total_hours(self):
        return sum(self.employee_hours.values())


'''
In this add_work() function we add the work or the project for a particular employee.
and also time.
'''


def add_work():
  if not employess:
    print("No employess available!!!")
    return

  emp_list = list_employee()

  choice:int = int(input("\nSelect the employee id:"))

  if choice < 1 or choice > len(emp_list):
    print("Invalid choice!!!")
    return

  emp = emp_list[choice - 1]

  project_name = input("Enter the project name:")
  hours = int(input("Enter the hours:"))

  if project_name not in projects:
    projects[project_name] = Project(project_name)

  projects[project_name].add_work(emp, hours)

  print("Work added successfully!")



'''=========================================== END ASSIGN EMPLOYEE ON PROJECT ADD ALSO TIME ==========================================='''

'''=========================================== Exception Part ==========================================='''

'''
Here we decler a class the name of the class is BudgetExceededException its take a argument,
Exception , tis hava a constructor its have three parameter project, total, budget.
we have three instance reference variable name of its self.project, self.total, self.budget,
assign by the three parameters.
'''
class BudgetExceededException(Exception):
    
def __init__(self, project, total, budget):
        self.project = project
        self.total = total
        self.budget = budget

'''
Help of this method show_summary(),
 we can check the project is under the budget or over the budget.
'''

def show_summary():
    print("\n--- PROJECT SUMMARY ---")

    for proj in projects.values():
        total = proj.total_hours()

        try:
            if total > PROJECT_BUDGET:
                raise BudgetExceededException(proj.name, total, PROJECT_BUDGET)

            print(f"{proj.name} | {total} | Within Budget")

        except BudgetExceededException as e:
            print(f"{e.project} | {e.total} | BUDGET EXCEEDED")




'''=========================================== END of Exception Part ==========================================='''


def main():
    while True:
        print("\n========= MENU =========")
        print("1. Add Department")
        print("2. View Departments")
        print("3. Add Employee")
        print("4. View Employees")
        print("5. Add Work Entry")
        print("6. Show Project Summary")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_deptrament()
        elif choice == "2":
           view_deptrament()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            list_employee()
        elif choice == "5":
               add_work()
        elif choice == "6":
            show_summary()
 
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


# -----------------------------------
# RUN
# -----------------------------------
if __name__ == "__main__":
    main()