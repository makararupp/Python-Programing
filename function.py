# ==========================================
# Python Functions Overview
# ==========================================

# 1. Basic Function (No parameters, no return)
def greet():
    print('Hello World!')

# Calling the function
greet()


# 2. Function with Parameters (Passing data into function)
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Makara")

# 3. Function with Return Value (Sends back a result)
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("5 + 3 =", result)


# 4. Function with Default Parameter Value
def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()          # Uses default value "Guest"
welcome("Makara")  # Overrides default with "Makara"