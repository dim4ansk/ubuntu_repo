from datetime import datetime
from functools import wraps

def times(num = 1):
    def time_check(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            count = 0
            res = func(*args, **kwargs)
            while count < num:
                print(f"Func name: {func.__name__}")
                dt = datetime.now()
                print(f"This func was opened in {dt.strftime("%H:%M:%S")}")
                count += 1
            return res
        return wrapper
    return time_check

@times(int(input("Enter choice: ")))
def add(a, b):
    """This is add"""
    return a + b

res1 = add(1, 25)
print(res1)
print(add.__doc__)


@times(int(input("Enter choice: ")))
def my_pow(a, b):
    """This is pow"""
    return a ** b


res2 = my_pow(3, 4)
print(res2)
print(my_pow.__doc__)


# def decore(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, int):
#             result += 1
#         return result
#     return wrapper
#
# @decore
# def add(a, b):
#     return a + b
#
# print(add(1, 1))

