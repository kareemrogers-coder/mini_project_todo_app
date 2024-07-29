### Mini-Project.

# Introduction


# In this project, you will apply your Python programming skills to create a functional To-Do List Application from scratch. The objective of this project is to reinforce your understanding of Python syntax, data types, control structures, functions, and error handling while building a practical and interactive application.


def add_on(list_items):
    to_do_list = input("Please enter your to do list item: ")
    list_item = [to_do_list]
    list_items.append(list_item)
    print(f"Please be advised {to_do_list.upper()} has been added to your to do list.")
    return list_items


def display_list (list_items):
    if not list_items:
        print("There are currently no item/items on your do to list.")
    else:
        for item in list_items:
            print(item)
    print(f''' Your current list are:
                {list_items}''')    

def del_item(list_items):
    for item_del in list_items:
        print(item_del)
    while True:
        try:
            to_do_list = input("Please enter the item name from the list above you wish to delete: ")
            list_item = [to_do_list]
            list_items.remove(list_item)
            print("*"*60)
            print(f"Please be advised {to_do_list.upper()} has been removed from your to do list.")
            break
        except ValueError:
            print("*"*60)
            for item_del in list_items:
                print(item_del)
            print("The item you enter isn't currently on your to do list. Please try again and select from the list above.")
            continue
        
    return list_items

def main ():
    to_do_list = []
    flag = True
    while flag:
        command = input(""" 
Welcome to the To-Do List App!

        Menu:
        1. Add a task
        2. View tasks
        3. Delete a task
        4. Quit

""")
        
        if command == "1":
            print("Option 1 selected")
            print("*"*60)
            list_update = add_on(to_do_list)
            #to_do_list = list_update
        elif command == "2":
            print("Option 2 selected")
            print("*"*60)
            display_list (to_do_list)

        elif command == "3":
            print("Option 3 selected")
            print("*"*60)
            del_item(to_do_list)

        elif command == "4":
            print("Option 4 selected")
            print("Exiting Application. GoodBye")
            break
        else:
            print("Invalid entry please select on of the entries below....")

main ()