numbers = [1, 2, 3, 4, 5]

while True:
    option = input("""Menu: 
1. Append
2. Insert
3. Pop
4. Remove
5. Quit

Choose an option: """)

    if not option.isdigit():
        print("Please enter a valid choice.")
        continue

    option = int(option)
    
    if option == 5: 
        print("Quitting...")
        break

    elif option == 1:
        value = input("Enter value: ")
        if not value.isdigit():
            print("Please enter a valid value.")
            continue
        value = int(value)
        numbers.append(value)
        print("Updated numbers: ", numbers)

    elif option == 2:
        value = input("Enter value: ")
        index = input("Enter index: ")
        
        if not value.isdigit() or not index.isdigit():
            print("Please enter a valid value and index.")
            continue
        
        value = int(value)
        index = int(index)
        
        if index < 0 or index > len(numbers):
            print("Invalid index.")
            continue
        
        numbers.insert(index, value)
        print("Updated numbers: ", numbers)

    elif option == 3:
        index = input("Enter index to pop: ")
        if not index.isdigit():
            print("Please enter a valid index.")
            continue
        index = int(index)
        
        if index < 0 or index >= len(numbers):
            print("Invalid index.")
            continue
        
        numbers.pop(index)
        print("Updated numbers: ", numbers)

    elif option == 4:
        value = input("Enter value to remove: ")
        if not value.isdigit():
            print("Please enter a valid value.")
            continue
        value = int(value)
        
        if value not in numbers:
            print("Value not found in the list.")
            continue
        
        numbers.remove(value)
        print("Updated numbers: ", numbers)
