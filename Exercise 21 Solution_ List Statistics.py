import statistics

def length(lst):
    if not isinstance(lst, list):
        return "Input must be a list."
    return len(lst)

def mean(lst):
    if not isinstance(lst, list):
        return "Input must be a list."
    if len(lst) == 0:
        return "List is empty."
    try:
        return sum(lst) / len(lst)
    except TypeError:
        return "List must contain only numeric values."

def range_of_list(lst):
    if not isinstance(lst, list):
        return "Input must be a list."
    if len(lst) == 0:
        return "List is empty."
    try:
        return max(lst) - min(lst)
    except TypeError:
        return "List must contain only numeric values."

def median(lst):
    if not isinstance(lst, list):
        return "Input must be a list."
    if len(lst) == 0:
        return "List is empty."
    try:
        return statistics.median(lst)
    except TypeError:
        return "List must contain only numeric values."

def standard_deviation(lst):
    if not isinstance(lst, list):
        return "Input must be a list."
    if len(lst) == 0:
        return "List is empty."
    try:
        return statistics.stdev(lst)
    except TypeError:
        return "List must contain only numeric values."
    except statistics.StatisticsError:
        return "Standard deviation requires at least two data points."

def list_statistics(lst):
    if not isinstance(lst, list):
        return "Input must be a list."
    
    stats = {
        "Length": length(lst),
        "Mean": mean(lst),
        "Range": range_of_list(lst),
        "Median": median(lst),
        "Standard Deviation": standard_deviation(lst)
    }
    return stats

numbers = [1, 2, 3, 4, 5]
single_element = [5]
empty_list = []
negative_numbers = [-1, -2, -3, -4, -5]
float_numbers = [1.5, 2.5, 3.5, 4.5]

print("Test: List with numbers")
print(list_statistics(numbers))

print("\nTest: List with a single element")
print(list_statistics(single_element))

print("\nTest: Empty list")
print(list_statistics(empty_list))

print("\nTest: List with negative numbers")
print(list_statistics(negative_numbers))

print("\nTest: List with floating-point numbers")
print(list_statistics(float_numbers))

print("\nTest: Invalid input (string instead of list)")
print(list_statistics("Not a list"))
