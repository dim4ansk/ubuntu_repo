import json
from functools import wraps
from datetime import datetime

print("Hello, this is phonebook" '\n'
      "1 - stats" '\n'
      "2 - add" '\n'
      "3 - delete name" '\n'
      "4 - list" '\n'
      "5 - show name" '\n'
      "6 - exit" '\n')

dt = datetime.now()

def decore(func):
    @wraps(func)
    def wrapper():
        with open("text.txt", "a") as wrap_file:
            wrap_file.write(func.__name__ + " - " + dt.strftime("%H:%M:%S" +"\n"))
            func()
    return wrapper


try:
    with open("data.json", "r") as json_file:
        dict_phone = json.load(json_file)
except FileNotFoundError:
    with open("error.txt", "a") as error_file:
        error_file.write(FileNotFoundError.__name__ + " - " + dt.strftime("%H:%M:%S" + "\n"))
    dict_phone = {}

@decore
def save_data():
    with open("data.json", "w") as json_file:
        json.dump(dict_phone, json_file, indent= 4)

while True:
    try:
        menu = int(input("Enter your choice: "))
    except ValueError:
        with open("error.txt", "a") as error_file:
            error_file.write(ValueError.__name__ + " - " + dt.strftime("%H:%M:%S" + "\n"))
        print("Error value, try again!" '\n')
        continue


    @decore
    def check_empty():
        if len(dict_phone) == 0:
            print("Your phonebook is empty! Add your friends." '\n')
            return True
        return False


    if menu < 1 or menu > 6:
        print("Error item! Try again" '\n')

    # command 1 stat
    elif menu == 1:
        print(f"You have {len(dict_phone)} contacts." '\n')

    # command 2 name
    elif menu == 2:
        name = input("Enter name: ")
        if name in dict_phone.keys():
            print(f"This person is already in your book. With number: {dict_phone.get(name)}" '\n')
            continue

        # command 2 number
        number = input("Enter number: ")
        if number.isdigit():
            if number[0] != "0":
                print("First num is '0'. Try again!" '\n')
            elif len(number[1:]) != 9:
                print("Number have only 10 num. Try again!" '\n')
            elif number in dict_phone.values():
                print(f"This number is already in your book"'\n')
            else:
                print("Your contact successfully added!"'\n')
                dict_phone[name] = number
                save_data()

        else:
            print("Only numeric. Try again!"'\n')


    # command 3 delete name
    elif menu == 3:
        if check_empty():
            continue
        delete_name = input("Enter name: ")
        try:
            del dict_phone[delete_name]
            save_data()
            print("This person successfully deleted." '\n')
        except KeyError:
            with open("error.txt", "a") as error_file:
                error_file.write(KeyError.__name__ +  " - " + dt.strftime("%H:%M:%S" +"\n"))
            print("This person is absent in your book." '\n')


    # command 4 list
    elif menu == 4:
        if check_empty():
            continue
        print("All contacts:")
        print('\n'.join(dict_phone.keys()), '\n')


    # command 5 show name
    elif menu == 5:
        if check_empty():
            continue
        show_name = input("Enter name: ")
        try:
            print(f"{show_name} - {dict_phone[show_name]}" '\n')
        except KeyError:
            with open("error.txt", "a") as error_file:
                error_file.write(KeyError.__name__ +  " - " + dt.strftime("%H:%M:%S" +"\n"))
            print('This person is absent in your book.' '\n')


    # command 5 exit
    elif menu == 6:
        break



