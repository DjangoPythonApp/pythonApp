class SMS:
    def __init__(self):

        self.userList:list = [{
            "userName":'admin',
            "pwd":'admin@123'
        },
        {
            "userName":'teacher',
            "pwd":'teacher@123'
        }
        
        ]

        self.studentList:list = []
        self.subjectList:list = []


    def UserList(self) -> None:

        input1 : str = input('Enter the username:')
        input2 : str = input('Enter the password:')

        for i in range(len(self.userList)):

            if self.userList[0]['userName'] == input1 and  self.userList[0]['pwd'] == input2:

                choice : int = int(input(f'''
                (Admin)
                1. Create subject.
                2. Press 0 for logout.
                Enter your choice.
                '''))

                if choice == 1:
                    subName:str = input('Enter the subject name:')
                    self.subjectList.append(subName)

                if choice == 0:
                    exit()

            
            

