import re
import logging


def deco_fun(sum1: object) -> object:

    def wrapper() -> object:

        # First input
        value: str = input("Enter the 1st value: ")

        pattern = r'^\d{2}$'

        # Validate first value
        if not re.match(pattern, value):

            logging.error(f'Invalid input value: {value}')

            raise ValueError(
                f"{value} is not valid. Enter exactly a 2-digit number."
            )

        # Second input only if first is valid
        value2: str = input("Enter the 2nd value: ")

        # Validate second value
        if not re.match(pattern, value2):

            logging.error(f'Invalid input value: {value2}')

            raise ValueError(
                f"{value2} is not valid. Enter exactly a 2-digit number."
            )

        logging.info(
            f'Validation successful: x = {value} and y = {value2}'
        )

        return sum1(value, value2)

    return wrapper