class SoldHouse:
    def _init_(self, property1=None, property2=None, property3=None, property4=None, property5=None):
        self.property1 = property1
        self.property2 = property2
        self.property3 = property3
        self.property4 = property4
        self.property5 = property5


rang = float(input("How many properties would you like to sell?  >>"))
for x in range(rang):
    sold = House()
    sold.property = input("Enter Property >> ")
    sold.price = input("Enter Price >> ")


houseListCounter = 1
for h in houseList:
    print(f"House #{houseListCounter}:")
    print(f"""
    soldProperty ............ {x.property}
    soldPrice ............... {x.Price}""")
    houseList += 1
