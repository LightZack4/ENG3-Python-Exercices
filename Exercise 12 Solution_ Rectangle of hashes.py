# This is me modifying

width = int(input("Width: "))
length = int(input("Length: ")) # Ask for the length

rectangle = ""; # Change name to rectangle

for i in range(length):
    for j in range(width):
        rectangle += "#";
    rectangle += "\n"; # Add new line to signify end of line.

print(rectangle);