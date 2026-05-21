class DSA:
    def __init__(self):
        self.stationary:list =[]
        self.garmens:list = []
        self.books:list = []

        self.container:dict ={}

    def add_element_stationary(self):

        self.data = input("Enter the element:")
        self.data2 = int(input("Enter the element price:"))

        self.stationary.append((self.data, self.data2))

        self.container.update({1:self.stationary})


    def add_element_garmens(self):

        self.data = input("Enter the element:")
        self.data2 = int(input("Enter the element price:"))

        self.garmens.append((self.data, self.data2))

        self.container.update({2:self.garmens})


    def add_element_books(self):

        self.data = input("Enter the element:")
        self.data2 = int(input("Enter the element price:"))

        self.books.append((self.data, self.data2))

        self.container.update({3:self.books})


    def display_data(self):

            for k,v in self.container.items():

                 print(k,v)

            print("-"*10)
            print(self.container)



obj:DSA = DSA()

while True:

    choice:int = int(input('''
    1.Stationery
    2.Garments
    3.Books
    4.Display
    5.Exit
    Enter the choice:'''))


    if choice == 1:
        obj.add_element_stationary()
    elif choice == 2:
        obj.add_element_garmens()
    elif choice == 3:
        obj.add_element_books()
    elif choice == 4:
        obj.display_data()
    elif choice == 5:
        exit()
    else:
        print('invalid choice!!!')