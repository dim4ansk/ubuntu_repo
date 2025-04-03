# task 1
def recursion(num: int):
    if num < 0:
        return None
    print(num)
    return recursion(num - 1)

recursion(int(input("Enter number: ")))


# task 2
def fibonachi(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonachi(num - 1) + fibonachi(num - 2)

print(fibonachi(int(input("Enter number: "))))


# task 3
def factorial(num: int):
    if num == 0:
        return 1
    return num * factorial(num - 1)

print(factorial(int(input("Enter number: "))))
