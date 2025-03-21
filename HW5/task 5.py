#task 1
enter = input("Enter your text: ")

for elem in range(len(enter)):
    if enter[elem].isdigit():
        if int(enter[elem]) % 2 == 0:
            print(f"'{enter[elem]}' -- is a even number")
        else:
            print(f"'{enter[elem]}' -- is a odd number")
    elif enter[elem].isalpha():
        if enter[elem].islower():
            print(f"'{enter[elem]}' -- is a small letter")
        else:
            print(f"'{enter[elem]}' -- is a big letter")
    else:
        print(f"'{enter[elem]}' -- is a symbol")

# task 2
# import time
# while True:
#     print("I love Python")
#     time.sleep(4.2)

# task 3 part 1
x = 1
number = int(input("Enter your number: "))
while x <= number:
    for i in range(1, x):
        print(i, end=' ')
    print(x)
    x += 1


# task 3 part 2
for i in range(int(input("Enter your number: "))):
    for j in range(1, i+1):
        print(j, end=' ')
    print(i+1)

