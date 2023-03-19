def create_menu():
    """Function to create a pizza restaurant menu"""
    menu = {}
    menu['Margherita'] = 10.00
    menu['Pepperoni'] = 12.00
    menu['Vegetarian'] = 11.50
    menu['Hawaiian'] = 13.00
    return menu

def print_menu(menu):
    """Function to print the pizza restaurant menu"""
    print("Pizza Menu:")
    for item, price in menu.items():
        print(item, ": $", price)

menu = create_menu()
print_menu(menu)
