items = {
    "Cheeseburger" : 5.50,
    "Double Bacon Burger": 7.90,
    "Spicy Chicken Sandwich": 6.20,
    "Veggie Delight Burger" : 5.00,
    "Crispy Fries" : 2.80,
    "Cheese Fries" : 4.50,
    "Chocolate Sundae": 3.00,
    "Apple pie": 2.50,
    "Milkshake": 4.20,
    "Coke per gram": 420.50
}

def display_menu(items):
    print("*****Welcome to HanBaoBao!*****\n*****This is our menu!*****\n")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")
def order_item():
    orders = {}
    order = input("What would you like to order?: ")
    if order in items:
        choice = input(f"Are you sure that you want to order {order}? y/n")
        if choice == "y":
            print(f"Order made for {order}!")
            orders.insert(order)
        else:
            order = input("What would you like to order?: ")
    pass
display_menu(items)
