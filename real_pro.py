import random
#Error handing

try:
    result =10/0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# File Handling
    with open('notes.txt','w') as file:
        file.write("This is a sample note.\n")
    with open('notes.txt','r') as file:
        content = file.read()
        print(content)

# Using a module
print("Random Number:", random.randint(1,100))