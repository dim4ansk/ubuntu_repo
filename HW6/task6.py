# task 1
def my_pow(x, y):
    return x ** y

print(my_pow(2,5 ))

# task 2

def any_add(*args):
    return sum(args)

print(any_add(1, 23, 6, 7))


# task 3

from functools import reduce

massive = [1, 5, 23, -3, 2, 51]

print(max(massive))

def my_max(elem):
    count = elem[0]
    for i in range(1, len(elem)):
        if count < elem[i]:
            count = elem[i]
    return count

print(my_max(massive))

lambda_max = reduce(lambda a, b: a if a > b else b, massive)
print(lambda_max)