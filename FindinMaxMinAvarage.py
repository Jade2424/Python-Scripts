def lst_of_operat(num_list):
    """Calculates the maximum, minimum, and average of a list of numbers."""
    
    if not num_list:
        return {"max": None, "min": None, "average": None}

    maximum = max(num_list)
    minimum = min(num_list)
    average = sum(num_list) / len(num_list)

    return {"max": maximum, "min": minimum, "average": average}

# Example of the list of numbers
num_list = [6, 12, 18, 24, 30]
results = lst_of_operat(num_list)
print(f"Maximum: {results['max']}")
print(f"Minimum: {results['min']}")
print(f"Average: {results['average']}")
