class SMS:
    def __init__(self):
        self.users:list = [{
            "uname": "admin",
            "password": "admin@123"
        },{
            "uname": "teacher",
            "password": "teacher@123"
        }
    ]
        
    self.subjectList:list = list()
    self.studentList:list = list()



    # Method: login
    def login(self, uname:str, pwd:str) -> str:
        for user in self.users:
            if user["uname"] == uname and user["password"] == pwd and user["uname"] == 'admin':
                return 'admin'
            elif user["uname"] == uname and user["password"] == pwd and user["uname"] == 'teacher':
                return 'teacher'
        else:
                 print('Invalid, try again')
    
    def subjectRegister(self):
        while True:
            print('1: Add subject: ')
            subName: str = input('Enter the subject name: ')

            self.subjectList.append(subName)
            print(self.subjectList)

            choice:int = int(input('Press 0 to continue: '))
            if choice == 0:
                continue
            else:
                break
    
    def studentRegister(self):
        c=1
        while True:


    def studentMarkAllotment(self):
        pass

                

def main() -> None:
    obj:SMS = SMS()
   
    while True:
        username:str = input("Enter user name: ")
        password:str = input("Enter password: ")
        status: str = obj.login(username, password)
        if status == 'admin':
            obj.subjectRegister()
        elif status == 'teacher':
            pass

        
if __name__ == '__main__':
    main()
    