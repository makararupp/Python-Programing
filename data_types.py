# ==========================================
# Python Data Types Overview
# ==========================================

# 1. Text Type: str (String)
name = "Makara"
print("1. String (str):", name, "->", type(name))

# 2. Numeric Types: int, float, complex
age = 23              # int (Integer: whole numbers)
salary = 500.50       # float (Decimal numbers)
c_number = 2 + 3j     # complex (Complex numbers)
print("2. Integer (int):", age, "->", type(age))
print("   Float (float):", salary, "->", type(salary))
print("   Complex (complex):", c_number, "->", type(c_number))

# 3. Boolean Type: bool (True or False)
is_active = True
has_car = False
print("3. Boolean (bool):", is_active, "->", type(is_active))

# 4. Sequence Types: list, tuple, range
# List: ordered, changeable, allows duplicates
skills = ["Python", "JavaScript", "HTML"]
# Tuple: ordered, unchangeable, allows duplicates
coordinates = (10, 20)
# Range: sequence of numbers
numbers = range(5)
print("4. List (list):", skills, "->", type(skills))
print("   Tuple (tuple):", coordinates, "->", type(coordinates))
print("   Range (range):", list(numbers), "->", type(numbers))

# 5. Mapping Type: dict (Key-Value pairs)
person = {
    "name": "Makara",
    "age": 23,
    "role": "Developer"
}
print("5. Dictionary (dict):", person, "->", type(person))

# 6. Set Types: set (Unique, unordered items)
unique_numbers = {1, 2, 3, 3, 4}  # duplicates are automatically removed
print("6. Set (set):", unique_numbers, "->", type(unique_numbers))

# 7. None Type: NoneType (Represents the absence of a value)
bonus = None
print("7. NoneType (None):", bonus, "->", type(bonus))

