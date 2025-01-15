numbers = [1, 2, 3, 4, 5]

while True:
    index_input = input("Enter index (-1 to quit): ")

    if not index_input.isdigit() and index_input != "-1":
        print("Please enter a valid integer.")
        continue

    index = int(index_input)

    if index == -1:
        break

    if index < 0 or index >= len(numbers):
        print("Invalid index. Please enter a valid index.")
        continue

    new_value_input = input("Enter new value: ")

    if not new_value_input.isdigit():
        print("Please enter a valid integer for the new value.")
        continue

    new_value = int(new_value_input)
    numbers[index] = new_value
    print("Updated numbers:", numbers)
