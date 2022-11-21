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
                break
           
             print("invalid option, try again 1-8")

        except ValueError:
            print("invalid option, try again")
            continue




    print("nice job")
make_choice()