# Im gonna explain everything in comments so no one thinks i am a fraud

Playing = True

# Make a dictionary containing all the items
Items = {
    "GTX 1080 Ti": 300, # legendary card btw
    "RTX 3060": 350, 
    "RTX 4090": 1600, 
    "Ryzen 5 5600X": 200, 
    "Ryzen 7 7800X3D": 450, 
    "Intel Core i5-13600K": 320, 
    "Intel Core i9-13900K": 570, 
    "Asus ROG Strix B550-F": 180, 
    "MSI MAG B650 TOMAHAWK": 250, 
    "Gigabyte Z790 Aorus Master": 500, 
    "Corsair Vengeance 16GB (2x8GB) DDR4-3200": 80,
    "G.Skill Trident Z5 RGB 32GB DDR5-6000": 180, 
    "Samsung 970 EVO Plus 1TB NVMe SSD": 100, 
    "WD Black SN850X 2TB NVMe SSD": 180, 
    "Seagate Barracuda 4TB HDD": 100, 
    "Corsair RM850x 850W PSU": 140, 
    "EVGA SuperNOVA 1000W PSU": 200, 
    "NZXT H510 Flow": 110,
    "Lian Li O11 Dynamic XL": 200,
    "Noctua NH-D15": 100,
    "Corsair iCUE H150i Elite Capellix": 250,
    "ASUS ROG Swift PG27UQ 27-inch 4K Monitor": 1400, 
    "Dell S2721DGF 27-inch 1440p Monitor": 400,
    "Logitech G Pro X Mechanical Keyboard": 130, 
    "Razer Basilisk V3": 70,
    "SteelSeries Arctis 7 Wireless Headset": 180, 
    "Elgato Stream Deck MK.2": 150, 
}

# Create a shopping cart Class
class ShoppingCart():

    # Cart Constructor function called when you do ShoppingCart()
    def __init__(self):
        self.Cart = []
        self.Price = 0

    # Create functions To add and remove items from cart
    def AddItem(self,Item):
        if Item in Items:
            self.Cart.append(Item)
            self.Price += Items[Item]
    def RemoveItem(self,Item):
        if Item in self.Cart:
            Price = Items[Item]
            self.Cart.remove(Item)
            self.Price -= Price
    # return a string so it doenst print a cart object in The memory
    def __str__(self):
        return f"Cart: {"\n".join(self.Cart1)}, \n For ${self.Price}"

# Create the Shopping Cart
Cart = ShoppingCart()
# Print all items with their prices
print("Our Shop Includes:")
for item, price in Items.items():
    print(f"{item}: ${price}")

while Playing:
    # this is just input with a try so if someone types in something that cant be converted to a integer it doesnt break 
    print("1 Add Item | 2 Remove Item | 3 Exit")
    try:
        Inpt = int(input(""))
        # Stop the game if inpt is 3
        if Inpt == 3:
            Playing = False
            print("Your Cart: ")
            print(Cart)
            print("Goodbye")
            break
        else:
            # Ask for the item
            Item = input(f"Enter Item To {"Add" if Inpt == 1 else "Remove"}: ")
            # Check if item is in Items
            if Item in Items:
                # Choose A String value which will be add it to cart if Inpt was 1 and Remove it from the if it was 2
                String = "add it to cart" if Inpt == 1 else "Remove it from the"
                # Print How much it costs and if they woud like to add it / remove it from the cart
                print(f"This item Costs ${Items[Item]} Woud you like to {String} Cart?")
                # Ask for a yes/no answer if the answer is yes then Add or remove the item
                Answer = input("Yes/No: ")
                if Answer == "Yes":
                    Cart.AddItem(Item) if Inpt == 1 else Cart.RemoveItem(Item)
            else:
                print("Item Not Available")
    except ValueError:
        print("Enter a number")

# So some more things i gotta explain \n breaks the line in strings and thats it