from colorama import init
init()
from colorama import Fore, Back, Style

check_list = []
print("Create a CheckList of Things you want to Remember and then mark them off once completed!")
def create(item):
    check_list.append(item)
    return check_list

def read(index):
    try:
        print(check_list[index])
    except IndexError:
        print("out of range")

def update(index, item):
    check_list[index] = item

def destroy(index):
    check_list.pop(index)

def list_all_items():
    index = 0
    if len(check_list) == 0:
        print("List is Empty")
    else:
        for list_item in check_list:
            print(Fore.BLACK + Back.YELLOW + ("{} {}".format(index, list_item)))
            # print(str(index+1)+ " " + list_item)
            index += 1

# function will uncheck the checklist after checklist is checkedtouch 
def un_mark(index):
    try:
        check_list[int(index)].replace("√", " ")
        print(list_all_items())
    except:
        print("not checked")
# method to insert √ on check List
def mark_completed(index):
    try:
        check_list[int(index)] = "√" + check_list[int(index)]
        list_all_items()
    except IndexError:
        print("out of range")


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read Item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist on out program
        read(int(item_index))
    # Print all items
    elif function_code == "P":
        list_all_items()
        #  insert √
    elif function_code == "M":
        item_index = user_input("Select object to be checked:")
        mark_completed(item_index)
    #attempt remove
    elif function_code == "U":
        item_index = user_input("Select object to be un-marked:")
        un_mark(item_index)


    elif function_code == "Q":
        # Stop the infinite loop
        return False

    else:
        print("Unkown Option")

    return True


def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input


def test():
    create("purple sox")
    create("red cloak")

    select("C")
    list_all_items()
    select("R")
    list_all_items()
    user_value = user_input("Please Enter a Value:")
    print(user_value)


# test()

running = True
while running:
    selection = user_input("Press C to add to list, R to Read from list, P to display list, U to un-mark and Q to quit or M check mark: ")
    running = select(selection.upper())
