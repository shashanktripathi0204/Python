from logger import logging
# This script demonstrates how to use logging in Python for basic arithmetic operations.
def add (a,b):
    """Function to add two numbers with logging"""
    # Log the input values and the result of the addition
    logging.debug("Starting addition function")
    logging.debug("Adding %d and %d", a, b)
    result = a + b
    logging.info("Result of addition: %d", result)
    return result

def subtract(a, b):
    """Function to subtract two numbers with logging"""
    # Log the input values and the result of the subtraction
    logging.debug("Starting subtraction function")
    logging.debug("Subtracting %d from %d", b, a)
    result = a - b
    logging.info("Result of subtraction: %d", result)
    return result

def multiply(a, b):
    """Function to multiply two numbers with logging"""
    # Log the input values and the result of the multiplication
    logging.debug("Starting multiplication function")
    logging.debug("Multiplying %d and %d", a, b)
    result = a * b
    logging.info("Result of multiplication: %d", result)
    return result

def divide(a, b):
    """Function to divide two numbers with logging"""
    # Log the input values and the result of the division
    logging.debug("Starting division function")
    if b == 0:
        logging.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")
    logging.debug("Dividing %d by %d", a, b)
    result = a / b
    logging.info("Result of division: %f", result)
    return result


add_result = add(10, 5)
subtract_result = subtract(10, 5)
multiply_result = multiply(10, 5)
try:
    divide_result = divide(10, 0)  # This will raise an error
except ValueError as e:
    logging.error("Error occurred: %s", e)
divide_result = divide(10, 5)