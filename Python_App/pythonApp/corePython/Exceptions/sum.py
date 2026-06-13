import logging

from decorator import deco_fun


logging.basicConfig(
    filename="my_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class Calculate:

    def __init__(self, value, value2):

        self.x = value
        self.y = value2
        self.total = 0

    def sum1(self) -> None:

        self.total = int(self.x) + int(self.y)

        logging.info(
            f'Calculated successfully {self.x} + {self.y} = {self.total}'
        )

        print("The sum is:", self.total)


@deco_fun
def main(value, value2):

    obj: Calculate = Calculate(value, value2)

    obj.sum1()


try:

    main()

except ValueError as e:

    print("Error:", e)

    logging.error(str(e))

except Exception as e:

    print("Unexpected Error:", e)

    logging.error(str(e))