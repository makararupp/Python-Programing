# ==========================================
# Python Sets Overview
# ==========================================

# 1. Creating a Set with Curly Braces {}
# Sets are unordered, unindexed, and do NOT allow duplicate values.
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate "apple" is automatically removed
print("1. Fruits Set:", fruits)

# 2. Creating an Empty Set
# NOTE: {} creates an empty dictionary, not an empty set!
# You must use set() for an empty set.
empty_set = set()
print("\n2. Empty Set:", empty_set, "->", type(empty_set))

# 3. Creating a Set from a List (Great for removing duplicates!)
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print("\n3. List with duplicates:", numbers_list)
print("   Set of unique numbers:", unique_numbers)

# 4. Adding and Removing Elements
colors = {"red", "green"}
colors.add("blue")                  # Add a single element
print("\n4. After add('blue'):", colors)

colors.discard("red")               # Remove element (safe: won't error if not found)
print("   After discard('red'):", colors)

# 5. Checking if an item exists in a set (in operator)
# Sets are very fast (O(1)) for checking membership
print("\n5. Is 'green' in colors?", "green" in colors)
print("   Is 'red' in colors?", "red" in colors)

# 6. Set Operations (Union, Intersection, Difference)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: all elements from both sets
print("\n6. Set Operations:")
print("   Union (A | B):", set_a | set_b)

# Intersection: only elements present in both sets
print("   Intersection (A & B):", set_a & set_b)

# Difference: elements in A but not in B
print("   Difference (A - B):", set_a - set_b)

# Symmetric Difference: elements in A or B, but NOT both
print("   Symmetric Difference (A ^ B):", set_a ^ set_b)
