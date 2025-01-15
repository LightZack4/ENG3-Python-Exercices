
user_list = []
def calculate_mean():
    sum = 0
    for i in user_list:
        sum += i
    print(sum)
    return sum/len(user_list)
def calculate_median():
    if len(user_list) %2 ==1:
        return user_list[len(user_list)//2]
    else:
        return (user_list[len(user_list)//2]+user_list[len(user_list)//2-1])/2
def save_to_file():
    with open("user_list.txt", "w") as file:
        for item in user_list:
            file.write(str(item) + "\n")
    print("List saved to 'user_list.txt'.")

def load_from_file():
    try:
        with open("user_list.txt", "r") as file:
            for line in file:
                user_list.append(int(line.strip()))
        print("List loaded from 'user_list.txt'.")
    except FileNotFoundError:
        print("No saved list found. Starting with an empty list.")

def calculate_statistics():
    if user_list:
        mean = calculate_mean()
        try:
            median = calculate_median()
        except ValueError:
            median = "N/A"  # Handle case if list has an odd number of elements
        print(f"List Statistics: Mean = {mean}, Median = {median}")
    else:
        print("List is empty. No statistics to calculate.")

load_from_file()
while True:
    
    
    user_input = input("Enter a number (0 to stop): ").strip()
    
    if not user_input.isdigit():
        print("Please enter a valid integer.")
        continue

    number = int(user_input)

    if number == 0:
        break

    user_list.append(number)

    print("Current List:", user_list)
    
    order_option = input("Sort in ascending or descending order? (a/d): ").strip().lower()
    
    if order_option == "a":
        print("Sorted List:", sorted(user_list))
    elif order_option == "d":
        print("Sorted List (Descending):", sorted(user_list, reverse=True))
    else:
        print("Invalid option. Showing in ascending order by default.")
        print("Sorted List:", sorted(user_list))

    calculate_statistics()

    save_option = input("Would you like to save the list? (y/n): ").strip().lower()
    if save_option == 'y':
        save_to_file()
