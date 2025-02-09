items = {
    "Notebook" : 2.50,
    "Pencil": 0.50,
    "Pen": 1.20,
    "Ruler" : 1.50,
    "Eraser" : 0.50,
    "Writing Pad" : 2.50,
    "Marker": 2.00,
    "Glue": 3.00,
    "Calculator": 35.00,
    "Coke": 120.65,
}

def display_menu(items):
    print("*****Welcome to Popular*****\n*****This is our menu!*****\n")
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")

def order_item(orders, items):
    order = input("What would you like to buy? (Type 'no more' to finish): ").lower()
    while order != "no more":
        found_item = None
        for item in items:
            if item.lower() == order:
                found_item = item
                break
        
        if found_item:
            quantity = input(f"How many of {found_item} would you like to buy? ")
            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                orders[found_item] = quantity
                print(f"Order made for {quantity} {found_item}!")
            else:
                print("Please enter a valid quantity (positive number).")
        else:
            print("That item is not in the menu....")
        
        order = input("What would you like to buy? (Type 'no more' to finish): ").lower()

def show_order_summary(orders, items):
    print("\n***** Order Summary *****\n")
    total = 0
    for item, quantity in orders.items():
        total += items[item] * quantity
        if total >= 20:
            total = total * 0.9
            discount = total * 0.1
            print(f"{item} x {quantity}: $({items[item] * quantity:.2f}) - {discount:.2f}(DISCOUNT)")
        else:
            print(f"{item} x {quantity}: $({items[item] * quantity:.2f})")
    print(f"Total: ${total:.2f}")
    print("Thanks for ordering!")

display_menu(items)
orders = {}
order_item(orders, items)
if orders:
    show_order_summary(orders, items)
else:
    print("You didn't buy anything.")
