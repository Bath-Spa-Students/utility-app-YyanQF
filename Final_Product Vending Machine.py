#Asessment Python Vending Machine 
import time

print("""
        |\---/|
        | ,_, |
         \_`_/-..----.              "Welcome, oh great traveller! I am Gingy, the guardian of this mystical Purrfect Paws Vending Machine. 
      ___/ `   ' ,""+ \  sk             Within these compartments, you shall find treasures fit for feline royalty."
    (__...'   __\    |`.___.';      
         (_,...'(_,.`__)/'.....+ )        
 ________________________________________
 |                     |                |
 |    __   __   __     |                |
 |   |  | |  | |  |    |                | 
 |   |  | |  | |  |    |                |
 |   |__| |__| |__|    |  ___________   |
 |   _______________   | |           |  |
 |    __   __   __     | | 1 | 2 | 3 |  |
 |   |  | |  | |  |    | | 4 | 5 | 6 |  |
 |   |  | |  | |  |    | | 7 | 8 | 9 |  |
 |   |__| |__| |__|    | |___________|  |
 |                     | | A | B | C |  |
 |_____________________| |__________ |  |
 |                                      |
 |     __________________________       |
 |    |                          |      |
 |    |                          |      |
 |    |                          |      |
 |    |__________________________|      | 
 |                                      |
 |      _      _____ ____  _            |
 |     / \__/|/  __//  _ \/ \  /|       |
 |     | |\/|||  \  | / \|| |  ||       |
 |     | |  |||  /_ | \_/|| |/\||       |
 |     \_/  \|\____\\____/\_/  \|        |
 |___________________________________ __|                                                                    
          """) #An Introduction and Welcome message to the user

print("_____________________________________________________")  #Separates the introduction and the vending machine itself

items = {
    'Cat Food': {
        'A1': {
            'Product Name': 'Me-o Chicken and Vegetable Cat Food',
            'Code': 'A1',
            'Price': 15.53,
            'Stock': 7,
        },
        'A2': {
            'Product Name': 'Purina Friskies Chicken and Turkey Cat Food',
            'Code': 'A2',
            'Price': 22.62,
            'Stock': 2,
        },
        'A3': {
            'Product Name': "Dreamies with Tasty Chicken Treat",
            'Code': 'A3',
            'Price': 13.99,
            'Stock': 8,
        },
    },
    'Snacks (For Humans)': {
        'B1': {
            'Product Name': 'Toxic Waste Sour Candy',
            'Code': 'B1',
            'Price': 3.13,
            'Stock': 3,
        },
        'B2': {
            'Product Name': 'Haribo Goldbears',
            'Code': 'B2',
            'Price': 4.55,
            'Stock': 4,
        },
        'B3': {
            'Product Name': "Mars Bar",
            'Code': 'B3',
            'Price': 3.75,
            'Stock': 5,
        },
    },
    'Drinks (For Human)': {
        'C1': {
            'Product Name': 'Apple Juice',
            'Code': 'C1',
            'Price': 4,
            'Stock': 3,
        },
        'C2': {
            'Product Name': 'Milk',
            'Code': 'C2',
            'Price': 3.5,
            'Stock': 6,
        },
        'C3': {
            'Product Name': 'Water',
            'Code': 'C3',
            'Price': 2,
            'Stock': 1,
        },
    }
    
}

# Function to display the list of items
def display_items():

    #ANSI escape codes for formatting
    bold = "\033[1m"
    underline = "\033[4m"
    reset_format = "\033[0m"

    print("\t\n-----------------------------------------Items List:-------------------------------------------------------------")
    for category, items_dict in items.items():
        for item_key, item_value in items_dict.items(): 
            print("{}Catergory:{} {}".format(bold, reset_format, category)) #This formats the Item Code and Category to highlight it
            print("{}Item Code:{} {}".format(underline, reset_format, item_value["Code"]))
            print("\n\tName: {}, Price: ${}, Stock: {}".format(item_value["Product Name"], item_value["Price"], item_value["Stock"])) #The specified values are formatted and inserted into the string's placeholder.
            print("-----------------------------------------------------------------------------------------------------------------")

# Call the function to display the list of items
display_items()

# Function to make a purchase
def make_purchase(money):
    # Let the user choose the item to purchase
    choice = input("\nPlease enter the code of the item you want to purchase or 'quit' to end the program: ")
    # Check if the user wants to quit
    if choice.lower() == 'quit':
        print("""
        |\---/|                            
        | ,_, | 
         \_`_/-..----.              ""Oh, esteemed traveler, thank you for visiting the Purrfect Paws Vending Machine.
      ___/ `   ' ,""+ \  sk                            I wish you safe travels on your journey!"
    (__...'   __\    |`.___.';      
         (_,...'(_,.`__)/'.....+ )        
 ________________________________________
 |                     |                |
 |    __   __   __     |                |
 |   |  | |  | |  |    |                | 
 |   |  | |  | |  |    |                |
 |   |__| |__| |__|    |  ___________   |
 |   _______________   | |           |  |
 |    __   __   __     | | 1 | 2 | 3 |  |
 |   |  | |  | |  |    | | 4 | 5 | 6 |  |
 |   |  | |  | |  |    | | 7 | 8 | 9 |  |
 |   |__| |__| |__|    | |___________|  |
 |                     | | A | B | C |  |
 |_____________________| |__________ |  |
 |                                      |
 |     __________________________       |
 |    |                          |      |
 |    |                          |      |
 |    |                          |      |
 |    |__________________________|      | 
 |                                      |
 |      _      _____ ____  _            |
 |     / \__/|/  __//  _ \/ \  /|       |
 |     | |\/|||  \  | / \|| |  ||       |
 |     | |  |||  /_ | \_/|| |/\||       |
 |     \_/  \|\____\\____/\_/  \|        |
 |___________________________________ __|                
""") 
        return money

    # Iterate through each category and find the corresponding item
    for category, items_dict in items.items():
        for item_key, item_value in items_dict.items(): 
            if item_value["Code"] == choice:
                # Check if the item is in stock
                if item_value["Stock"] > 0:
                    # Check if the user has enough money to purchase the item
                    if money >= item_value["Price"]:
                        # Make the purchase
                        print("Dispensing please wait...")
                        time.sleep(2) #transition effect
                        print("\nCongratulations! You have successfully purchased a {}.".format(item_value["Product Name"]))
                        print("You paid ${} for this item.".format(item_value["Price"]))
                        money -= item_value["Price"]
                        item_value["Stock"] -= 1
                        print("You now have ${} remaining in your account.".format(money))
                        print("\nThank you for purchasing at Purrfect Paws Vending machine:")
                        print("----------------------------------------------------------------")
                        print("Purchase Summary:")
                        print("\tItem Purchased: {}".format(item_value["Product Name"]))
                        print("\tItem Code: {}".format(item_value["Code"]))
                        print("\tPrice: ${}".format(item_value["Price"]))
                        print("\tNew Stock: {}".format(item_value["Stock"]))
                        print("----------------------------------------------------------------")
                        return money
                    else:
                        print("\nError: You do not have enough money to purchase this item. Please add more money and try again.")
                        return make_purchase(money)
                else:
                    print("\nError: The item you are trying to purchase is out of stock. Please choose another item.")
                    return make_purchase(money)

    print("\nError: Invalid item code. Please try again.")
    return make_purchase(money)

# Function to simulate the purchase process
def simulate_purchase_process():

    # Let the user input the amount of money they want to spend
    # or 'quit' to end the program
    money = input("\nPlease enter the amount of money you want to spend, or 'quit' to end the program: ")

    # Check if the user entered a valid amount of money
    if money.lower() == 'quit':
        print("""
        |\---/|                            
        | ,_, | 
         \_`_/-..----.              ""Oh, esteemed traveler, thank you for visiting the Purrfect Paws Vending Machine.
      ___/ `   ' ,""+ \  sk                            I wish you safe travels on your journey!"
    (__...'   __\    |`.___.';      
         (_,...'(_,.`__)/'.....+ )        
 ________________________________________
 |                     |                |
 |    __   __   __     |                |
 |   |  | |  | |  |    |                | 
 |   |  | |  | |  |    |                |
 |   |__| |__| |__|    |  ___________   |
 |   _______________   | |           |  |
 |    __   __   __     | | 1 | 2 | 3 |  |
 |   |  | |  | |  |    | | 4 | 5 | 6 |  |
 |   |  | |  | |  |    | | 7 | 8 | 9 |  |
 |   |__| |__| |__|    | |___________|  |
 |                     | | A | B | C |  |
 |_____________________| |__________ |  |
 |                                      |
 |     __________________________       |
 |    |                          |      |
 |    |                          |      |
 |    |                          |      |
 |    |__________________________|      | 
 |                                      |
 |      _      _____ ____  _            |
 |     / \__/|/  __//  _ \/ \  /|       |
 |     | |\/|||  \  | / \|| |  ||       |
 |     | |  |||  /_ | \_/|| |/\||       |
 |     \_/  \|\____\\____/\_/  \|        |
 |___________________________________ __|                
""") #Short Goodbye message to the user
        return

    try:
        money = float(money)
    except ValueError:
        print("\nError: Invalid amount of money. Please enter a positive number or 'quit'.")
        return simulate_purchase_process()
    
    # Let the user make purchases until they run out of money
    while money > 0:
        money = make_purchase(money)

# Call the function to simulate the purchase process
simulate_purchase_process()