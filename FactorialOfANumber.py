def factorial(t):
    """ 
    This function calculates the factorial of a number using a loop.

    Args:
        t: The number to calculate the factorial of.

    Returns:
        The factorial of t, or 1 if t is 0.
    """
    if t < 0:
        return None  # Factorial is not defined for negative numbers
    elif t == 0 or t == 1:
        return 1
    else:
        factorial = 1
        for b in range(1, t + 1):
            factorial *= b
        return factorial

# Example to use for this code  
num = 6
factorial_result = factorial(num)
print(f"The factorial of {num} is {factorial_result}.")