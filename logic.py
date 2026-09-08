age = int(input("Enter your age: "))

if age <13 :
    print("You are a child.")
elif age <20:
    print("You are a teenager.")
else:
    print("You are an adult.")
# and/or/not example
has_ticket = True
has_id = False

if has_ticket and not has_id:
    print("You can enter the concert.")