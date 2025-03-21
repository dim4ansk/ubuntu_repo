#task 1
num = input("Enter your text: ")
if num.isdigit():
    if int(num) % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")
elif num.isalpha():
    print("Your text has words.", f"Length is {len(num)}")
else:
    print("Your text has another symbols")