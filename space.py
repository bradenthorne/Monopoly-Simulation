class Space():
    def __init__(self, name, position, type):
        self.name = name
        self.position = position
        self.type = type
        self.count = 0
        self.is_property = False
        self.can_buy_houses = False

class Property(Space):
    def __init__(self, name, position, price, type):
        super().__init__(name, position, "Property")
        self.price = price
        self.type = type
        self.is_property = True
        self.owner = None
        self.rent_collected = 0
        self.money_invested = 0

    def set_owner(self, player):
        self.owner = player
    
    def clear_owner(self):
        self.owner = None

class Street(Property):
    def __init__(self, name, position, price, rent_list, building_cost, group):
        super().__init__(name, position, price, "Street")
        self.rent_list = rent_list
        self.building_cost = building_cost
        self.houses = 0
        self.group = group
        self.current_rent = self.rent_list[0]
        self.can_buy_houses = True
    
    def add_houses(self, quantity):
        if self.houses + quantity <= 5:
            self.houses += quantity
            self.owner.pay_money(self.building_cost * quantity)
            self.money_invested += self.building_cost * quantity
            self.update_rent()
        else:
            return
    
    def remove_houses(self, quantity):
        if self.houses - quantity >= 0:
            self.houses -= quantity
            self.owner.receive_money(self.building_cost * quantity * 0.5)
        else:
            return
    
    def update_rent(self):
        self.current_rent = self.rent_list[self.houses]

class Railroad(Property):
    def __init__(self, name, position, price, rent_list):
        super().__init__(name, position, price, "Railroad")
        self.rent_list = rent_list
        self.current_rent = 100 # Adjust later
        self.group = "Railroad"

class Utility(Property):
    def __init__(self, name, position, price):
        super().__init__(name, position, price, "Utility")
        self.current_rent = 100 # Adjust later
        self.group = "Utility"

class Tax(Space):
    def __init__(self, name, position, amount):
        super().__init__(name, position, "Tax")
        self.amount = amount

class Card(Space):
    def __init__(self, name, position):
        super().__init__(name, position, "Card")

class Neutral(Space):
    def __init__(self, name, position):
        super().__init__(name, position, "Neutral")