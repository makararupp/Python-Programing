cart = ['T-shirt', 'Lamp', 'Pen']
print(cart)

# A list of mixed data types
my_list = [1, 'Hello', 3.14, True]
print(my_list)

# Empty list
my_empty_list = []
print(my_empty_list)

# Using the list()
vowels = "aeiou"
# Converting string to list
vowel_list = list(vowels)
print(vowel_list)

# Access list items by index
languagues = ['Python', 'Java', 'C++', 'JavaScript']
print(languagues[0])
print(languagues[2])

#  adding and update items
# UPDATE SECOND ITEM TO SHOPE
cart[1] ="Shope"
print(cart)

# adding items to the list
cart.append('Book')
print(cart)

# adding all item from another list
new_cart =['Notebook', 'Pencil']
cart.extend(new_cart)
print(cart)

# insert item at specific index
cart.insert(0, 'Bag')
print(cart)

# remove item from the list
carts =['T-shirt', 'Lamp', 'Pen', 'Book', 'Notebook', 'Pencil']
carts.remove('Lamp')
print(carts)