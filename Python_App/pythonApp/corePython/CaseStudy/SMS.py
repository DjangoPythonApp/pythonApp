class SMS:
    def __init__(self)->None:
        self.data:list = []
        self.subjects:list = []

    def InsertStudentData(self) -> None:

        fname:str = input('Enter the first name:')
        lname:str = input('Enter the last name:')
        roll:int = int(input('Enter the roll:'))

        totalSubject:int = int(input('Enter the number of total subjects:'))

        for i in range(totalSubject):

            subjectName:str = input(f"Enter the subject name {i+1}:")
            marks:int = int(input("Enter the marks:"))


            self.subjects_marks:dict = {
                'subject':subjectName,
                'marks':marks
            }

            self.subjects.append(self.subjects_marks)



        self.data.append({
            'fname':fname,
            'lname':lname,
            'roll':roll,
            'subjects':self.subjects
        })

        print("="*30,"Added succesfully","="*30)



    def UpdateStudentData(self) -> None:


        roll:int = int(input("Enter the roll number:"))

        for i in range(len(self.data)):

            if roll == self.data[i]['roll']:
               y:str = input("Update the name ? (YES/NO)")

               if 'yes' == y.lower():
                print("Recent first name is:",self.data[i]['fname'])
                self.data[0]['fname'] = input("Enter the name:")
                print("="*30,"updated succesfully","="*30)


               y:str = input("Update the last name ? (YES/NO)")

               if 'yes' == y.lower():
                 print("Recent last name is:",self.data[i]['lname'])
                 self.data[i]['lname'] = input("Enter the last name:")
                 print("="*30,"updated succesfully","="*30)


               y:str = input('Update the name of the subject ? (YES/NO)')

               if 'yes' == y.lower():

                 subject:str = input('Enter the subject name which you want to update:')

                 for j in range(len(self.subjects)):

                    if self.subjects[j]['subject'] == subject:

                        self.subjects[j]['subject'] = input('Enter the new subject name:')
                        print("="*30,"updated succesfully","="*30)


               y:str = input('Update the marks of the subject ? (YES/NO)')

               if 'yes' == y.lower():

                 for j in range(len(self.subjects)):
                    print(f'Subject : {self.subjects[j]['subject']} and Marks: {self.subjects[j]['marks']}')

                 subject:str = input('Enter the subject  which marks you want to update:')

                 for j in range(len(self.subjects)):

                    if self.subjects[j]['subject'] == subject:

                        self.subjects[j]['marks'] = input(f'Enter the new subject {self.subjects[j]['subject']} marks:')
                        print("="*30,"updated succesfully","="*30)







    def DisplayStudentData(self) -> None:

        print(self.data)

        print("1.Show the whole record.")
        print("2.Show the specific record.")
        choice:int = int(input("Enter the choice:"))

        if choice == 1:

             print("="*30,"Students Recoard","="*30)
     
             for i in range(len(self.data)):
     
                 print(f'''
                         Student first name:{self.data[i]['fname']},
                         Student last name:{self.data[i]['lname']},
                         Student Roll:{self.data[i]['roll']},
                         Subject name:{self.data[i]['subjects'][i]['subject']} and marks:{self.data[i]['subjects'][i]['marks']}
                 ''')
           
     
            
                        
              


        elif choice == 2:

            roll:int = int(input('Enter the student roll:'))
     
            for i in range(len(self.data)):

                if self.data[i]['roll'] == roll:

                     print(f'''
                         Student first name:{self.data[i]['fname']},
                         Student last name:{self.data[i]['lname']},
                         Student Roll:{self.data[i]['roll']},
                         Subject name:{self.subjects[i]['subject']} and marks:{self.subjects[i]['marks']}
                         ''')
                     break
                


    def DeleteStudentRecord(self) -> None:

        roll:int = int(input('Enter the student roll:'))
     
        for i in range(len(self.data)):
            
                print(self.data[i]['roll'])


                if roll == self.data[i]['roll'] :

                    del self.data[i]

        print("="*30,"Deleted succesfully","="*30)

     

def main() -> None:

    obj:SMS = SMS()
    
    while True:
        print('='*30,'Student management system', '='*30)
        choice:int = int(input(('''
        1.Insert the student data.
        2.Update the student data.
        3.Display the student data.
        4.Delete the student data.
        5.Exit
        Enter the choice..
        ''')))
    
    
        if choice == 1:
            obj.InsertStudentData()
    
        elif choice == 2:
            obj.UpdateStudentData()
    
        elif choice == 3:
            obj.DisplayStudentData()
    
        elif choice == 4:
            obj.DeleteStudentRecord()
        elif choice == 5:
            exit()
        else:
            print('Invalid choice..')



if __name__ == '__main__':
    main()
    
        













print(obj.data)