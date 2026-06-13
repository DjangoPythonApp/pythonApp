import random
class BankAccount:
    def __init__(self,name:str=None, address:str=None,amount:int=None):
        self.name:str = name 
        self.address:str = address
        self.account_no:int = int(random.random() * 9000000000) +1000000000
        self.amount:int = amount
        self.data:dict = {"Acount holder name":self.name,
                            "Address":self.address,
                            "Account NO.":self.account_no,
                            "Balance":self.amount,
                            }

    def createAccount(self,name,address,amount)->None:
        self.name:str = name 
        self.address:str = address
        self.amount:int = amount
        self.data.update({"Acount holder name":self.name,
                            "Address":self.address,
                            "Balance":self.amount})


    def dipositMoney(self,amount)->int:
        self.amount+=amount
        self.data.update({"Balance":self.amount}) 
        return self.amount

    def withdram(self,amount)->int:
        self.amount-=amount
        self.data.update({"Balance":self.amount}) 
        return self.amount

    def checkBalance(self)->None:
        for k,v in self.data.items():
            print(f'''
                   {k}: {v}''')  



obj:BankAccount = BankAccount()


while True:
    choice:int = int(input('''
                        1.Create a account.
                        2.Deposite money.
                        3.Withdraw money.
                        4.Check balance.
                        5.Exit
                        Enter your choice:'''))

    if choice == 1:
        name:str = input("Enter the name of the holder:")
        address:str = input("Enter the address ofthe holder:")
        amount:int = int(input("Enter the amount:"))
        obj.createAccount(name,address,amount)
        print('Create account succesfully')
        
    elif choice == 2:
        x:int = obj.dipositMoney(int(input("Enter the amount:")))
        print(f"Money add succesfully corrent amount{x}")

    elif choice == 3:
        x:int = obj.withdram(int(input("Enter the amount:")))
        print(f"Money add withdraw corrent amount{x}")

    elif choice == 4:
       obj.checkBalance()

    elif choice == 5:
        exit()
      