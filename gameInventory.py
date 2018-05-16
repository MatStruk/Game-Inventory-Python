# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

# Displays the inventory.
def display_inventory(inventory):
    print("Inventory:")
    for items, amount in inventory.items():
        print("{0} {1}".format(amount, items) + "\n")
    pass


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    new_dict = {}   # creates new empty dictionary
    for item in added_items:    # iterates through the list and appends freshly created dictionary
        if item not in new_dict:
            new_dict[item] = 1
        else:
            new_dict[item] += 1

    for a in new_dict:      # mergers dictionaries
        if a in inventory:
            inventory[a] += new_dict[a]     # updates value
        else:
            inventory[a] = new_dict[a]      # creates new element

    print("Inventory:")
    total_amount = []
    for items, amount in inventory.items():
        print("{0} {1}".format(amount, items))
        total_amount.append(amount)
    total_amount = sum(total_amount)
    print("Total number of items: {0}".format(total_amount) + "\n")
    pass


# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    print("Inventory:")
    total_amount = []
    item_strings = []
    space = " "
    if order == "count,desc":
        max_length = max(len(x) for x in inventory)
        count = 2 * space + "count"
        item_name = (int((max_length / 2)) * space + "item name")
        headline = count + item_name
        print(headline + "\n" + "-" * len(headline))
        for items, amount in sorted(inventory.items(), key=lambda x: x[1], reverse=True):
            print(
                (7 - len(str(amount))) * space + str(amount) + space * (len(item_name) - len(str(items))) + str(items))
            total_amount.append(amount)
            item_strings.append(items)
        print("-" * len(headline))
    if order == "count,asc":
        max_length = max(len(x) for x in inventory)
        count = 2 * space + "count"
        item_name = (int((max_length / 2)) * space + "item name")
        headline = count + item_name
        print(headline + "\n" + "-" * len(headline))
        for items, amount in sorted(inventory.items(), key=lambda x: x[1]):
            print(
                (7 - len(str(amount))) * space + str(amount) + space * (len(item_name) - len(str(items))) + str(items))
            total_amount.append(amount)
            item_strings.append(items)
        print("-" * len(headline))
    if order == None:
        max_length = max(len(x) for x in inventory)
        count = 2 * space + "count"
        item_name = (int((max_length / 2)) * space + "item name")
        headline = count + item_name
        print(headline + "\n" + "-" * len(headline))
        for items, amount in inventory.items():
            print(
                (7 - len(str(amount))) * space + str(amount) + space * (len(item_name) - len(str(items))) + str(items))
            total_amount.append(amount)
            item_strings.append(items)
        print("-" * len(headline))

    total_amount = sum(total_amount)
    print("Total number of items: {0}".format(total_amount) + "\n")
    pass


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="test_inventory.csv"):
    filename = open(filename).readlines()
    new_string = str(filename)
    new_string = new_string.replace("'", "")
    new_string = new_string.replace("[", "")
    new_string = new_string.replace("]", "")
    new_string = new_string.split(",")
    add_to_inventory(inventory, new_string)
    pass


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    newstring = ""
    for x in inventory:
        newstring += (x + ",") * inventory[x]
    with open(filename, "w") as myfile:
        myfile.write(newstring)
    pass


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, "wea   fwea": 3}
import_inventory(inv, filename="export_inventory.csv")