import logging

#  logging settings
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler('app.log'),
        # StreamHandler to output logs to the console, and to the file
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("MathApp")

def add(a, b):
    """Function to add two numbers with logging"""
    logger.debug("Starting addition function")
    logger.debug(f"Adding {a} and {b}")
    result = a + b
    logger.info(f"Result of addition: {result}") 
    return result

def subtract(a, b): 
    """Function to subtract two numbers with logging"""
    logger.debug("Starting subtraction function")
    logger.debug(f"Subtracting {b} from {a}")
    result = a - b
    logger.info(f"Result of subtraction: {result}")
    return result

def multiply(a, b):
    """Function to multiply two numbers with logging"""
    logger.debug("Starting multiplication function")
    logger.debug(f"Multiplying {a} and {b}")
    result = a * b
    logger.info(f"Result of multiplication: {result}")
    return result

def divide(a, b):
    """Function to divide two numbers with logging"""
    logger.debug("Starting division function")
    if b == 0:
        logger.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")
    logger.debug(f"Dividing {a} by {b}")
    result = a / b
    logger.info(f"Result of division: {result}")
    return result

if __name__ == "__main__":
    add_result = add(10, 5)
    subtract_result = subtract(10, 5)
    multiply_result = multiply(10, 5)
    try:
        divide_result = divide(10, 0)  # This will raise an error
    except ValueError as e:
        logger.error(f"Error occurred: {e}")
    divide_result = divide(10, 5)