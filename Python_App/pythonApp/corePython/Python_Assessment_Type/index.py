# -----------------------------------
# Custom Exception
# -----------------------------------
class BudgetExceededException(Exception):
    def __init__(self, project, total, budget):
        self.project = project
        self.total = total
        self.budget = budget


# -----------------------------------
# Model CLASSES
# -----------------------------------
class Department:
    def __init__(self, dept_id, name):
        self.dept_id = dept_id
        self.name = name


class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"{self.name} ({self.department.name})"


class Project:
    def __init__(self, name):
        self.name = name
        self.employee_hours = {}  # {Employee: hours}

    def add_work(self, employee, hours):
        if employee in self.employee_hours:
            self.employee_hours[employee] += hours
        else:
            self.employee_hours[employee] = hours

    def total_hours(self):
        return sum(self.employee_hours.values())


# -----------------------------------
# In Memory STORAGE
# -----------------------------------
departments: dict[int, Department] = {}
employees: dict[str, Employee] = {}
projects: dict[str, Project] = {}

PROJECT_BUDGET = 150

# -----------------------------------
# DEPARTMENT FUNCTIONS
# -----------------------------------
def add_department():
    name = input("Enter department name: ")
    dept_id = max(departments.keys(), default=0) + 1
    departments[dept_id] = Department(dept_id, name)
    print("Department added!")


def view_departments():
    if not departments:
        print("No departments found!")
        return

    print("\n--- DEPARTMENTS ---")
    for d in departments.values():
        print(f"{d.dept_id}. {d.name}")


# -----------------------------------
# EMPLOYEE FUNCTIONS
# -----------------------------------
def add_employee():
    name = input("Enter employee name: ")

    view_departments()

    dept_id = int(input("Enter Department ID: "))

    if dept_id not in departments:
        print("Invalid department!")
        return

    employees[name] = Employee(name, departments[dept_id])
    print("Employee added!")


def list_employees():
    if not employees:
        print("No employees found!")
        return []

    print("\n--- EMPLOYEES ---")

    emp_list = []
    index = 1

    for dept in departments.values():
        print(f"\nDepartment: {dept.name}")
        found = False

        for emp in employees.values():
            if emp.department == dept:
                print(f"{index}. {emp}")
                emp_list.append(emp)
                index += 1
                found = True

        if not found:
            print("  No employees")

    return emp_list


# -----------------------------------
# WORK ENTRY
# -----------------------------------
def add_work():
    if not employees:
        print("No employees available!")
        return

    emp_list = list_employees()

    choice = int(input("\nSelect Employee ID: "))

    if choice < 1 or choice > len(emp_list):
        print("Invalid choice!")
        return

    emp = emp_list[choice - 1]

    project_name = input("Enter project name: ")
    hours = int(input("Enter hours: "))

    if project_name not in projects:
        projects[project_name] = Project(project_name)

    projects[project_name].add_work(emp, hours)

    print("Work added successfully!")


# -----------------------------------
# SUMMARY (WITH EXCEPTION)
# -----------------------------------
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


# -----------------------------------
# MENU
# -----------------------------------
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
            add_department()
        elif choice == "2":
            view_departments()
        elif choice == "3":
            add_employee()
        elif choice == "4":
            list_employees()
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