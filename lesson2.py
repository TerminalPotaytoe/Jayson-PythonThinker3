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

def order_item(orders, items):
    order = input("What would you like to order? (Type 'no more' to finish): ")
    while order != "no more":
        if order in items:
            choice = input(f"Are you sure that you want to order {order}? (y/n): ")
            if choice.lower() == "y":
                if order in orders:
                    orders[order] += 1
                else:
                    orders[order] = 1
                print(f"Order made for {order}!")
            else:
                print(f"Order canceled for {order}.")
        else:
            print("Sorry, that item isn't on the menu. Please try again.")
        
        order = input("What would you like to order? (Type 'no more' to finish): ")

def show_order_summary(orders, items):
    print("\n***** Your Order Summary *****")
    total = 0
    for item, quantity in orders.items():
        print(f"{item}: {quantity} x ${items[item]:.2f} = ${items[item] * quantity:.2f}")
        total += items[item] * quantity
    print(f"Total: ${total:.2f}")
    print("Thank you for ordering!")

display_menu(items)
orders = {}
order_item(orders, items)
if orders:
    show_order_summary(orders, items)
else:
    print("You didn't order anything.")
