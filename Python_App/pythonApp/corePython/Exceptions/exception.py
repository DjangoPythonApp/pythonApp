import logging

logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    number = int(input("Enter number: "))
    result = 100 / number
    print(result)
    

except ValueError:
    print("Invalid input entered")
    logging.error("User entered invalid input")

except ZeroDivisionError:
    print("User tried division by zero")
    logging.error("User tried division by zero")



# logging.info()
# logging.warning()
# logging.error()
# logging.exception()


# Logging Level                Purpose
# DEBUG	                  Detailed debugging information
# INFO	                  General information
# WARNING	              Warning message
# ERROR	                  Serious problem
# CRITICAL	              Very severe error