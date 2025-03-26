print("Hello, this is phonebook" '\n'
                 "1 - stats" '\n'
                 "2 - add" '\n'
                 "3 - delete name" '\n'
                 "4 - list" '\n'
                 "5 - show name" '\n'
                 "6 - exit" '\n')

dict_phone = {}

while True:

    menu = input("Enter your choice: ")

    def check_empty():
        if len(dict_phone) == 0:
            print("Your phonebook is empty! Add your friends." '\n')
            return True
        return False

    if menu.isdigit():
        if int(menu) < 1 or int(menu) > 6:
            print("Error item! Try again" '\n')

        # command 1 stat
        elif int(menu) == 1:
           print(f"You have {len(dict_phone)} contacts." '\n')

        # command 2 name
        elif int(menu) == 2:
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
            else:
                print("Only numeric. Try again!"'\n')


        #command 3 delete name
        elif int(menu) == 3:
            if check_empty():
                continue
            delete_name = input("Enter name: ")
            if delete_name in dict_phone.keys():
                del dict_phone[delete_name]
                print("This person successfully deleted." '\n')
            else:
                print("This person is absent in your book." '\n')


        #command 4 list
        elif int(menu) == 4:
            if check_empty():
                continue
            print("All contacts:")
            print('\n'.join(dict_phone.keys()), '\n')


        # command 5 show name
        elif int(menu) == 5:
            if check_empty():
                continue
            show_name = input("Enter name: ")
            if show_name in dict_phone.keys():
                print(f"{show_name} - {dict_phone[show_name]}" '\n')
            else:
                print('This person is absent in your book.' '\n')


        # command 5 exit
        elif int(menu) == 6:
            break

    else:
        print("Error value, try again!" '\n')
