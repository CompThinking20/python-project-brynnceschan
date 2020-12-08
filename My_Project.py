# Lists that I will need for the whole program
to_do_list = []
to_do_time = []

# Function to ask what is on the to-do list and fill the lists with the information
# Does not take an argument, but does ask the user for an input inside the function
# Returns the number of items on the to-do list
def get_my_schedule():
    # Creating starting variables
    item_counter = 0
    item = ""
    # Creating a loop that will continue to fill in the lists until a user wants it to stop
    item = str(input("What is the title of item 1 on your to-do list? (Input 0 when you are done, 1 to edit the list): "))
    while(item != "0"):
        if(item == "1"):
            edit_schedule()
            item = str(input("What is the title of item " + str(item_counter + 1) + " on your to-do list? (Input 0 when you are done, 1 to edit the list): "))
        else:
            item_counter += 1
            add_item_to_schedule(item)
            item = str(input("What is the title of item " + str(item_counter + 1) + " on your to-do list? (Input 0 when you are done, 1 to edit the list): "))
    return item_counter

# Function to add items to each list
# Added this function down here to make the while loop easier to follow
# Takes the name of the item as an argument, asks the user for how long it will take
def add_item_to_schedule(item_name):
    to_do_list.append(item_name)
    time = str(input("How long will '" + item_name + "' take to complete in minutes?: "))
    to_do_time.append(time)

# Function to check off items
def edit_schedule():
    print("Here is your to-do list:")
    print(to_do_list)
    item_select = str(input("Which item would you like to check off?: "))
    # Assume the item is not in the list until it is found in the following for loop
    item_found = False
    # Checks to see if the user input is actually in the to-do list
    for item in to_do_list:
        if(item == item_select):
            item_found = True
    if(item_found):
        to_do_list.remove(item)
        print("Item successfully removed.")
    # If the input is not in the to-do list, send an error message and let them try again
    else:
        response = str(input("Item not found :( Input 0 to view the list again, 1 to go back: "))
        if(response == "0"):
            # Have the user go back to the top of this function
            edit_schedule()
        elif(response == "1"):
            # Send the user back to where they were
            return
        else:
            # Neither 0 or 1, send them to the top of this function anyway
            print("Invalid input, let's try this again.")
            edit_schedule()


# Prints to Show that the function is working
number_of_items = get_my_schedule()
print("Number of things to do today: " + str(number_of_items))
print("To-do List:")
print(to_do_list)
print("To-do Times:")
print(to_do_time)