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
    time = 0
    # Creating a loop that will continue to fill in the lists until a user wants it to stop
    item = input("What is the title of item 1 on your to-do list? (Input 0 when you are done): ")
    while(item != "0"):
        item_counter += 1
        to_do_list.append(item)
        time = input("How long will '" + item + "' take to complete in minutes?: ")
        to_do_time.append(time)
        item = input("What is the title of item " + str(item_counter + 1) + " on your to-do list? (Input 0 when you are done): ")
    return item_counter


# Prints to Show that the function is working
number_of_items = get_my_schedule()
print("Number of things to do today: " + str(number_of_items))
print("To-do List:")
print(to_do_list)
print("To-do Times:")
print(to_do_time)