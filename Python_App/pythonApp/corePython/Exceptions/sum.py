import logging
import re
from decorator import deco_fun, validation

logging.basicConfig(
    filename="my_log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Calculate:

    def __init__(self,value,value2):

        self.x = value
        self.y = value2
        self.total = 0


    


          


    @deco_fun
    def sum1(self) -> None:

        self.total:int = int(self.x) + int(self.y)

        logging.info(f'calculated succesfully {self.x} + {self.y} = {self.total}')
        print("The sum is:",self.total)
        



def main():

    try:

      value:str = input("Enter the 1st value:")


      validation(value)

      value2:str = input("Enter the 2nd value:")

      validation(value2)

      logging.info('user entered the values')
      
      obj: Calculate = Calculate(value,value2)

      obj.sum1()


    except ValueError as e:

         print("Error:", e)

         logging.error(str(e))


    except Exception as e:

        print("Error:", e)

        logging.error(str(e))


if __name__ == '__main__':

    
    main()



