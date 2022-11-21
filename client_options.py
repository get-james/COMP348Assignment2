def display_options():
        print("Python DB Menu\n")
        print("1. Find Customer")
        print("2. Add Customer")
        print("3. Delete Customer")
        print("4. Update Customer Age")
        print("5 Update Customer address")
        print("6. Update customer phone")
        print("7. Print Report")
        print("8. Exit\n")
        print("Select: ")


def make_choice():
    print("Please enter a valid choice")
   
    while(True):
        try:
             choice = int(input())
             if(choice >=1 and choice <= 8):
                inputs = choice_manager(choice)
                return inputs
           
             print("invalid option, try again 1-8")

        except ValueError:
            print("invalid option, try again")
            continue




    print("nice job")

def choice_manager(choice):
    choice_data = [choice]
    if(choice == 1):
        print("Please enter name:")
        name = input()
        choice_data.append(name)
        return choice_data
    if(choice == 2):
        print("Please enter all fields seperated by | (Example: John|20|15 Pengy Lane|5145554444)")
        input_list = input()
        input_list = input_list.split("|")
        choice_data.extend(input_list)
        return choice_data
    if(choice == 3):
        print("Please enter name:")
        name = input()
        choice_data.append(name)
        return choice_data
    if(choice == 4):
        print("Please enter name and age seperated by |")
        input_list = input()
        input_list = input_list.split("|")
        choice_data.extend(input_list)
        return choice_data
    if(choice == 5):
        print("Please enter name and adress seperated by |")
        input_list = input()
        input_list = input_list.split("|")
        choice_data.extend(input_list)
        return choice_data
    if(choice == 6):
        print("Please enter name and phone number seperated by |")
        input_list = input()
        input_list = input_list.split("|")
        choice_data.extend(input_list)
        return choice_data
    if(choice == 7):
        return choice_data
    if(choice == 8):
        print("thanks for using :)\nGoodbye!")
        quit()