import random
import os

def generate_operation():
    operator = random.choice(['+', '-', '*', '/'])
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    if operator == '/' and num2 == 0:
        num2 = random.randint(1, 50)
    return f"{num1} {operator} {num2}"

def filter_and_generate_operations(input_file, output_file):
    if not os.path.exists(input_file):
        x = int(input("Enter a number of operations to generate > 0: "))
        while x <= 0:
            x = int(input("Enter a number of operations to generate > 0: "))
        print(f"Input file '{input_file}' not found. Creating a sample file.")
        with open(input_file, 'w') as infile:
            for _ in range(x):
                infile.write(generate_operation() + '\n')
    
    print(f"FILE EXISTS, Please delete it to generate new operations, Processing from the input file '{input_file}' and writing to '{output_file}'.")

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        operations = infile.readlines()
        for operation in operations:
            num1, operator, num2 = operation.split()
            if operator == '-' and int(num1) < 21 and int(num2) < 10:
                outfile.write(f"SUBTRACTION,{num1}-{num2},1,{random.randint(1000, 50000)},anon9159,\"2016-01-18 10:29:11\"\n")

input_file = './operationFilter/operations.txt'
output_file = './operationFilter/filtered_operations.csv'

filter_and_generate_operations(input_file, output_file)
