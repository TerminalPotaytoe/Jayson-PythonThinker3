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
    "Coke": 420.50
}

def display_menu(items):
    print("*****Welcome to HanBaoBao!*****\n*****This is our menu!*****\n")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")
    print("\n************ End of Menu ************\n")

def order_item(orders, items):
    order = input("What would you like to order? (Type 'no more' to finish): ").lower()
    while order != "no more":
        found_item = None
        for item in items:
            if item.lower() == order:
                found_item = item
                break
        
        if found_item:
            if found_item in orders:
                orders[found_item] += 1
                print(f"Order made for {found_item}!")
            else:
                orders[found_item] = 1
                print(f"Order made for {found_item}!")
        else:
            print("That order is not in the menu....")
        
        order = input("What would you like to order? (Type 'no more' to finish): ").lower()

def show_order_summary(orders, items):
    print("\n***** Order Summary *****\n")
    total = 0
    for item, quantity in orders.items():
        print(f"{item} x{quantity}: ${items[item] * quantity:.2f}")
        total += items[item] * quantity
    print(f"Total: ${total:.2f}")
    print("Thanks for ordering!")

display_menu(items)
orders = {}
order_item(orders, items)
if orders:
    show_order_summary(orders, items)
else:
    print(" You didn't order anything.")
