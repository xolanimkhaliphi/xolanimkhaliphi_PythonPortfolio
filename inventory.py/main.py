# Inventory Management Code
import tabulate


# Define shoe class
class Shoes:
    # Constructor
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Define get_cost function that returns the cost of the shoe
    def get_cost(self):
        return self.cost

    # Define get_quantity function that returns the quantity of the shoe
    def get_quanty(self):
        return self.quantity

    #  Define the __str__ method to return a string representation of the shoe
    def __str__(self):
        return f'{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}'


# Creating a Variable with an empty list
list_shoes = []


# Define the read_shoes_data function to read data from inventory.txt and create shoe objects
def read_shoes_data():
    # Use try-expect to handle any error
    try:
        with open("inventory.txt", "r") as inventory_file:
            next(inventory_file)  # This will skip the first line of the file
            for line in inventory_file:
                data = line.strip().split(',')  # Strip white spaces and split the line on the comma
                country = data[0]  # The first data will be for country in each line
                code = data[1]
                product = data[2]
                cost = int(data[3])  # int() to convert to integer -
                quantity = int(data[4])
                shoe_object = Shoes(country, code, product, cost, quantity)  # Call the Class Shoes
                list_shoes.append(shoe_object)  # Append shoe object to list
    except Exception as e:
        print(f'An error has occurred:{e}')  # If error occurs


# Define capture_shoes function to allow user to capture shoe data

def capture_shoes():  # To allow user to capture information about a shoe, Request user input for each piece of data
    country = input("Please Enter the country's Name:")
    code = input("Please Enter the code of the product:")
    product = input("Please Enter the Name of the product:")
    cost = int(input("Please Enter how much the product cost :"))
    quantity = int(input("Please Enter the quantity of the product:"))
    # Create a new shoes object using user input and add it to the list
    shoe_object = Shoes(country, code, product, cost, quantity)
    # Add the shoe object to the list
    list_shoes.append(shoe_object)


# Define a function to  iterate over all the shoes list and
# print the details of the shoes that you return from the __str__  function
def view_all():
    # Create an empty list to store the data for each shoe
    data = []
    # Iterate over the list of shoes and append the data for each shoe to the data list
    for shoes in list_shoes:
        data.append([shoes.country, shoes.code, shoes.product, shoes.cost, shoes.quantity])

    # Print the table
    print(tabulate.tabulate(data, headers=['Country', 'Code', 'Product', 'Cost', 'Quantity']))


# Define a Function that will find the shoe object with the lowest stock quantity that needs to be re-stocked
def restock():
    # Sort the list of shoes by quantity ( lowest to highest)
    list_shoes.sort(key=lambda x: x.quantity)  # Use Sort() method to sort a list in ascending order,the key function
    # is defined using a lambda expression (a small anonymous function) that takes an element x and returns its
    # quantity attribute
    shoe_to_restock = list_shoes[0]  # Get the shoe with the lowest quantity
    # Print the details of the shoe
    print(f'Shoe to restock:{shoe_to_restock}')
    # Ask the user if the want to restock the shoe
    answer = input("Do you want to restock this shoe? (Y/N)")
    if answer.lower() == "y":
        # If the user wants to restock, ask them how much to add
        add_quantity = int(input("Please Enter the quantity to add:"))
        # update the quantity of the shoe
        shoe_to_restock.quantity += add_quantity
        # Find the index of the shoe in the list
        index = list_shoes.index(shoe_to_restock)
        # update the list with the new quantity for the shoe
        list_shoes[index] = shoe_to_restock
        # Open the inventory file in write mode
        with open("inventory.txt", "w") as inventory_file:
            # iterate over the list of shoes and write their details to the file
            for shoe in list_shoes:
                inventory_file.write(f'{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n')
    else:
        # If the user does not want to restock, do nothing
        pass


# Define a Function that will search for a shoe from the list using the shoe code and return this object, so it will
# be printed
def search_shoe():
    # Ask the user to Enter the search code
    code = input("Enter the code of the shoe you want to search for:")
    # Iterate over the list of shoes
    for shoe in list_shoes:
        # If the shoe's code matches the search code, return the shoe
        if shoe.code == code:
            return print(f'{shoe}')
    # If no shoe was found, return None
    return print("Sorry!! The is no matching shoe with that code")


# Define a Function that will calculate the total value for each item.
def value_per_item():
    # iterate over the list of shoes
    for shoe in list_shoes:
        # Calculate the value of the shoe using the formula value = cost* quantity
        Value = shoe.cost * shoe.quantity
        # Print out the details of the shoe and its value
        print(f'{shoe}: Value = {Value}')


def highest_qty():
    # Use the max function and pass it a key function that returns the quantity attribute of each Shoe object
    max_qty = max(list_shoes, key=lambda x: x.quantity)
    # Find the Shoes object with the highest quantity in the list_shoes list
    highest_qty_shoe = next(shoe for shoe in list_shoes if
                            shoe.quantity == max_qty.quantity)  # next function returns the next item produced by the
    # iterator
    # Print the details of the shoe
    print(f'Shoe for sale:  {highest_qty_shoe}')


while True:
    # Display menu
    print("Welcome to the Inventory Management System!")
    print("Please select an option from the following menu:")
    print("Please Note: Start selecting option 1 to load Data to the system before clicking any option:")
    print("1. Read data from inventory file")
    print("2. Capture new shoe data")
    print("3. View all shoe data")
    print("4. Find shoe to restock")
    print("5. Search Shoe by Code")
    print("6. Calculate the total value for each item")
    print("7. Find shoe to with highest quantity")
    print("8. Exit")

    # Accept user input
    selection = input("Enter your selection:")

    # Process user selection
    if selection == "1":
        read_shoes_data()
    elif selection == "2":
        capture_shoes()
    elif selection == "3":
        view_all()
    elif selection == "4":
        restock()
    elif selection == "5":
        search_shoe()
    elif selection == "6":
        value_per_item()
    elif selection == "7":
        highest_qty()
    elif selection == "8":
        print("Goodbye!!Thank you for Using the System.")
        break
    else:
        print("Invalid selection. Please try again.")
