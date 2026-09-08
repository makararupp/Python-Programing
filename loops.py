#while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# for loop with range
for i in range(1,11):
    if i %3 == 0 and i %5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)