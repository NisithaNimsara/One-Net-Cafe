import random
#Create variables
choice = 0
state = True
try_again = 0
itemCode = 0
inventory = []
invenCheck = []
dealers=0
fileSave = None


def sorting():
    # sorting inventory according  to the Item Code value
    length = len(inventory)

    for key in range(length):
        lowValue = key
        for newKey in range(key + 1, length):
            if int(inventory[newKey]['Item Code']) < int(inventory[lowValue]['Item Code']):
                lowValue = newKey
        # Change elements
        inventory[key], inventory[lowValue] = inventory[lowValue], inventory[key]

def date(givedate):
    "This function help to get date correctly "
    year = givedate[0: 4]
    month = givedate[5: 7]
    day = givedate[8:10]
    realdate = year + "/" + month + "/" + day
    return realdate

def displayMenu():
    "This function will Display the possible command manu."
    print("""
    Type AID for adding item details.
    Type DID for deleting item details.
    Type UID for updating item details.
    Type VID for viewing the items table.
    Type SID for saving the item details to the text file.
    Type SDD for selecting four dealers randomly from a file.
    Type VRL for displaying all the details of the randomly selected dealers.
    Type LDI for displaying the items of the given dealer.
    Type ESC to exit the program.
    """)

def addItemDetails():
    "This function get item details and store in inventory."
    itemName = None
    itemBrand = None
    price = 0.0
    quantity = 0
    category = None
    purchasedDate = None
    item = None
    print("Adding item details")
    while True:  # For get correct Item code
        try:
            #getting input from user
            itemCode = int(input("Enter Item Code (3 Digit): "))
            itemCode = f"{itemCode:03d}" #converting 3 digit
            if int(itemCode) < 0:
                print("Invalid Item Code! Try again..")
            elif invenCheck.count(itemCode) == 1:
                print("This item code already Registered!")
            else:
                invenCheck.append(itemCode)
                break
        except ValueError or TypeError:
            print("Invalid Format!!!")

    while True:                    # get correct item name
        itemName = input("Enter Item Name: ")
        if len(itemName) > 10 or len(itemName) <= 0:
            print("Invalid item name! Try  again..")
        else:
            break

    while True:                     # to get correct item brand
        itemBrand = input("Enter Item Brand: ")
        if len(itemBrand) > 10 or len(itemBrand) <= 0:
            print("Invalid item Brand! Try  again..")
        else:
            break

    while True:  # For get correct Item Price
        try:
            price = float(input("Enter Item Price: "))
            if price <= 0:
                print("Invalid Price! Try again..")
            else:
                break
        except ValueError or TypeError:
            print("Invalid Format!!!")

    while True:  # For get correct Item Quantity
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity < 0:
                print("Invalid Quantity! Try again..")
            else:
                break
        except ValueError or TypeError:
            print("Invalid Format!!!")

    while True:                     # to get correct item Category
        category = input("Enter Item Category: ")
        if len(category) > 10:
            print("Invalid item Category! try  again..")
        else:
            break

    while True:  # to get correct item Purchased Date
        try:
            Date = str(input("Enter Purchased Date (YYYY/MM/DD): "))
            year = int(Date[0:4])
            month = int(Date[5:7])
            day = int(Date[8:10])
            if len(Date) != 10 or year <= 0 or month > 12 or month <= 0 or day > 31 or day <= 0:
                print("Invalid Purchased Date! try  again..")
            else:
                purchasedDate = date(Date)
                break
        except ValueError:
            print("Invalid Format!!!")


    item = {
        'Item Code': itemCode,
        'Item Name': itemName,
        'Item Brand': itemBrand,
        'Price': price,
        'Quantity': quantity,
        'Category': category,
        'Purchased Date': purchasedDate}
    inventory.append(item)
    print("Item added successfully!")

def deleteitemDetails():
    "This function delete item from inventory"
    print("Deleting item details")
    while True:
        itemCode = int(input("Enter Item Code to delete: "))
        itemCode = f"{itemCode:03d}"  # converting 3 digit
        for item in inventory:
            if item['Item Code'] == itemCode:
                inventory.remove(item)
                print("Item deleted successfully!")
                return
        else:
            print("Item not found!")

def updateItemDetails():
    "This function for update item detail other than item code."
    print("Updating item details")
    try:
        while True:
            itemCode = int(input("Enter Item Code to update: "))
            itemCode = f"{itemCode:03d}"  # converting 3 digit
            for item in inventory:
                if item['Item Code'] == itemCode:
                    while True:  # update item name
                        newItemName = input("Enter Item Name: ")
                        if len(newItemName) > 10 or len(newItemName) <= 0:
                            print("Invalid item name! Try  again..")
                        else:
                            item['Item Name'] = newItemName
                            break

                    while True:  # update item brand
                        newItemBrand = input("Enter Item Brand: ")
                        if len(newItemBrand) > 10 or len(newItemBrand) <= 0:
                            print("Invalid item Brand! Try  again..")
                        else:
                            item['Item Brand'] = newItemBrand
                            break

                    while True:  # update Item Price
                        try:
                            newPrice = float(input("Enter Item Price: "))
                            if newPrice <= 0:
                                print("Invalid Price! Try again..")
                            else:
                                item['Price'] = newPrice
                                break
                        except ValueError or TypeError:
                            print("Invalid Format!!!")

                    while True:  # update Item Quantity
                        try:
                            newQuantity = int(input("Enter Quantity: "))
                            if newQuantity < 0:
                                print("Invalid Quantity! Try again..")
                            else:
                                item['Quantity'] = newQuantity
                                break
                        except ValueError or TypeError:
                            print("Invalid Format!!!")

                    while True:  # update item Category
                        newCategory = input("Enter Item Category: ")
                        if len(newCategory) > 10:
                            print("Invalid item Category! try  again..")
                        else:
                            item['Category'] = newCategory
                            break

                    while True:  # update item Purchased Date
                        try:
                            newDate = str(input("Enter Purchased Date (YYYY/MM/DD): "))
                            year = int(newDate[0:4])
                            month = int(newDate[5:7])
                            day = int(newDate[8:10])
                            if len(newDate) != 10 or year <= 0 or month > 12 or month <= 0 or day > 31 or day <= 0:
                                print("Invalid Purchased Date! try  again..")
                            else:
                                newPurchasedDate = date(newDate)
                                item['Purchased Date'] = newPurchasedDate
                                break
                        except ValueError:
                            print("Invalid Format!!!")
                    print("Item updated successfully!")
                    return
            else:
                print("Item not found!")
    except ValueError:
        print("Try Again...")

def viewItemDetails():
    'This function will display Item Details as a table and Total value od items'
    print("Viewing the items table and current total")
    #display tables Headings
    print("| ", "Item Code", " " * (10 - len("Item Code")), " | ", "Item Name", " " * (10 - len("Item Name")), " | ", "Item Brand",
          " " * (10 - len("Item Brand")), " | ", "Price(Rs.)", " " * (10 - len("Price(Rs.)")), " | ", "Quantity",
          " " * (10 - len(str("Quantity"))), " | ", "Category", " " * (10 - len("Category")), " | ", "Purchased Date",
          " " * (15 - len("Purchased Date")), " |")
    #Display table
    for x in inventory:
        print("| ", x["Item Code"], " " * (10 - len(x["Item Code"])), " | ", x["Item Name"], " " * (10 - len(x["Item Name"])), " | ", x["Item Brand"],
              " " * (10 - len(x["Item Brand"])), " | ", x["Price"], " " * (10 - len(str(x["Price"]))), " | ", x["Quantity"],
              " " * (10 - len(str(x["Quantity"]))), " | ", x["Category"], " " * (10 - len(x["Category"])), " | ",
              x["Purchased Date"], " " * (15 - len(x["Purchased Date"])), " |")
    total = sum(item['Price'] * item['Quantity'] for item in inventory)
    print(f"Total value of items: Rs {total:.2f}")

def saveItemDetails():
    'This function will save item details to a text file.'
    # This will open the file in Writing mode
    with open('Item Details.txt',"w") as file:
        heading = ["Item Code", "Item Name", "Item Brand", "Price", "Quantity", "Category", "Purchased Date"]
        for i in heading:
            y = str(" " * (10 - len(i)))
            file.write(f"|  {i} {y}")
        file.write("|\n")

    # This will save item Details in the file
    with open("Item Details.txt",'a') as file:
        for dic in inventory:
            for item in dic:
                key = item
                value = dic[key]

                r = str(" " * (10 - len(str(value))))
                file.write(f"|  {value} {r}")
            file.write("    |\n")
    print("\nItem Details Saved to a File!")

def selectRandomDealers():
    'This function will select 4 dealers form text file'
    dealers = []
    dealerItems = []
    print("Selecting four dealers randomly from a file")
    try:
        with open("dealers.txt","r") as file2:     #Opening text file in read mode
            for line in file2:
                parts = line.strip().split(",")    #Spliting using "," mark

                name, contact, location, items = parts[0], parts[1], parts[2], parts[3]

                #Dealer's Item details separating
                for item in items.split(";"):      #Spliting using ";" mark
                    itemParts = item.strip().split("|")  #Spliting using "|" mark

                    if len(itemParts) == 4:  #Seperating item parts
                        itemDict = {
                            "name": itemParts[0],
                            "brand": itemParts[1],
                            "price": float(itemParts[2]),
                            "quantity": int(itemParts[3])}
                        dealerItems.append(itemDict) #append item parts to item Dict

                        if len(dealerItems) == 3:  #appending Dealer details to a list
                            dealers.append({
                                "name": name,
                                "contact": contact,
                                "location": location,
                                "items": dealerItems})
                            dealerItems = []

                    else:
                        print("Item details not Enough!")

        #Selecting 4 random dealers from all dealers
        selected = random.sample(dealers, 4)
        print("4 Dealers are Selected Randomly.")
        return selected
    except FileNotFoundError:
        print("Dealers file not found")

def viewRandomDealers(dealers):
    "This function will display the dealer's details"
    print("Displaying all the details of the randomly selected dealers")
    if dealers == 0:
        print("First you need to select Dealers.")
    else:
        print("--Dealer's Details--")
        # display tables Headings
        print("| ", "Name", " " * (10 - len("Name")), " | ", "Contact No", " " * (12 - len("Contact No")), " | ",
              "Location"," " * (10 - len("Location")), " |")

        # Sorting according to the location name (A to Z)
        n = len(dealers)
        for i in range(n):
            for j in range(0, n - i - 1):
                if dealers[j]["location"].lower() > dealers[j + 1]["location"].lower():
                    # Swap dealers
                    dealers[j], dealers[j + 1] = dealers[j + 1], dealers[j]

        # Display table
        for x in dealers:
            print("| ", x["name"], " " * (10 - len(x["name"])), " | ", x["contact"],
                  " " * (12 - len(x["contact"])), " | ", x["location"],
                  " " * (10 - len(x["location"]))," |")

def displayItemsOfDealer(dealers):
    "This function will display the dealer's item details"
    available = None
    print("Display the items of the given dealer")
    try:
        chooseDealer = input("Enter Dealer's Name : ")  #Getting input from user

        for x in dealers:
            if chooseDealer == x['name'] :               #Selecting the relavant item Details
                available = 1
                print("--Dealer's Item Details--")
                print("|", "Name", " " * (10 - len("Name")), "|", "Brand", " " * (10 - len("Brand")), "|",
                      "Price(Rs.)", " " * (10 - len("Price(Rs.)")), "|", "Quantity", " " * (10 - len("Quantity")), "|")
                for ss in x['items']:
                    for ee in ss:
                        print('|',ss[ee]," " * (10 - len(str(ss[ee]))),end=' ')
                    print('|','\r')
        if available != 1:
            print('Dealer Not Found!')
    except TypeError:
        print("Wrong Format Try Again!")

#-------------------Main Program-----------------------------------------


while state:
    displayMenu()
    choice = input("Enter your choice: ").upper()
    #Selection option
    if choice == "AID":
        addItemDetails()
        sorting()
        continue
    elif choice == "DID":
        deleteitemDetails()
        continue
    elif choice == "UID":
        updateItemDetails()
        continue
    elif choice == "VID":
        viewItemDetails()
        continue
    elif choice == "SID":
        saveItemDetails()
        continue
    elif choice == "SDD":
        dealers = selectRandomDealers()
        continue
    elif choice == "VRL":
        viewRandomDealers(dealers)
        continue
    elif choice == "LDI":
        displayItemsOfDealer(dealers)
        continue
    elif choice == "ESC":
        print("Have a nice day !!!")
        break
    else:
        print("Invalid choice.")

    #Try again option.
    try_again = str(input("Do you want to try again: ")).upper()
    if try_again == "NO":
        print("Have a nice day !!!")
        break
    elif try_again == "YES":
        continue
    else:
        print("Assume you want to try again.")
        continue