import logging
import re
logging.basicConfig(
 
   filename='my_log',
   level=logging.INFO,
   format="%(asctime)s - %(levelname)s - %(message)s"

)


def validation(value) -> None:

    pattern = r'^\d{2}$'

    if not re.match(pattern, value):
        logging.error(f'Invalid input value:{value}')
        raise ValueError(f"{value} is invalid. Enter exactly a 2-digit number.")

   


def deco_fun(sum1:object) -> object:

        def wrapper(self) -> object:
               


            logging.info(f'Validation succesfull: x = {self.x} and y = {self.y}')
                

            return sum1(self)

        return wrapper