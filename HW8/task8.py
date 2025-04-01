from curses.ascii import isdigit

set1 = {1, 2, 4, 56, 34}
set2 = {1, 2, 56, 3, 34, 99}

# task 1
def my_intersection(arg_1, arg_2):
    lst = []
    for i in arg_1:
        if i in arg_2:
            lst.append(i)
    return lst

print(my_intersection(set2, set1))
print(set1.intersection(set2))


# task 2
def my_sym_dif(arg_1, arg_2):
    lst = []
    for i in arg_1:
        if i not in arg_2:
            lst.append(i)

    for j in arg_2:
        if j not in arg_1:
            lst.append(j)
    return lst


print(my_sym_dif(set2, set1))
print(set1.symmetric_difference(set2))



# task 3

text = "Hello! I love Python."
map_lst = list(map(lambda x: x.upper(), text))

new_text = "".join(map_lst)
print(new_text)



# task 4
lst_filter = ["a", "v", "x", 3, "we", 12, 0, -1, True, 4.3]
print(list(filter(lambda x: type(x) in [int, float], lst_filter)))



