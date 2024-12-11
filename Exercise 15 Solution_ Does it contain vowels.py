word = input("Please type in a string: ")

word = word.lower()
contain_a = False
contain_e = False
contain_o = False

for char in word:
    if char == 'a':
        contain_a = True
    if char == 'e':
        contain_e = True
    if char == 'o':
        contain_o = True

if contain_a:
    print("a found")
else:
    print("a not found")

if contain_e:
    print("e found")
else:
    print("e not found")

if contain_o:
    print("o found")
else:
    print("o not found")
