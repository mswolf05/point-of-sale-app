# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

import datetime
currentDT = datetime.datetime.now()
currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")

product_ids = []

while True:
    product_id = input("Input a product identifier or 'DONE': ")
# make sure the id exists in the products list of dictionaries

    # if clerk is done, go to print receipt
    if product_id == "DONE":
        break
    else:
        # check to see if prouct id exists in product list, if not have clerk try again
        if not any(p['id'] == int(product_id) for p in products):
            print("Product identifier is not in the list, please try again.")
        else:
            product_ids.append(int(product_id))


def matching_products(product_identifier):
    product_list = [p for p in products if p["id"] == pid]
    return product_list[0]

sub_total = 0
cart_items = ""

for pid in product_ids:
    product = matching_products(int(pid))
    #raw_total = raw_total + product["price"]
    product_id = str(product["id"])
    product_name = " + " + product["name"]
    product_price = " (${0:.2f})".format(product["price"])
    sub_total += product["price"]
    if cart_items != "":
        cart_items = cart_items + "\n" + product_name + product_price
    else:
        cart_items = cart_items +  product_name + product_price

# Calculate other owed amount
sales_tax = sub_total * .0875
total = sub_total + sales_tax

#format owed amounts
sub_total = "Subtotal: ${0:.2f}".format(sub_total)
sales_tax =  "Plus NYC Sales Tax: ${0:.2f}".format(sales_tax)
total =  "Total: ${0:.2f}".format(total)

#Format printed receipt
print("-----------------------------------")
print("MIKE'S GROCERY STORE")
print("-----------------------------------")
print("Web: www.mikesgrocery.com")
print("Phone: 1-914-960-9745")
print("Checkout Time: " + currentDT)
print("-----------------------------------")
print("Shopping Cart Items:")
print(cart_items)
print("-----------------------------------")
print(sub_total)
print(sales_tax)
print(total)
print("-----------------------------------")
print("Thank you for your business! Please come again.")

# write the receipt to the point-of-sale-app folder
file_name = "printed_receipt.txt" # refers to a file path relative to the path from which you invoke your your script.

with open(file_name, "w") as file: # NOTE: "w" means "open the file for writing"
    file.write("-----------------------------------\n")
    file.write("MIKE'S GROCERY STORE\n")
    file.write("-----------------------------------\n")
    file.write("Web: www.mikesgrocery.com\n")
    file.write("Phone: 1-914-960-9745\n")
    file.write("Checkout Time: " + currentDT + "\n")
    file.write("-----------------------------------\n")
    file.write("Shopping Cart Items:\n")
    file.write(cart_items +"\n")
    file.write("-----------------------------------\n")
    file.write(sub_total +"\n")
    file.write(sales_tax+ "\n")
    file.write(total +"\n")
    file.write("-----------------------------------\n")
    file.write("Thank you for your business! Please come again.")
