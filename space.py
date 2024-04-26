class Space():
    def __init__(self, name, position, type):
        self.name = name
        self.position = position
        self.type = type
        self.count = 0

class Property(Space):
    def __init__(self, name, position, price, type):
        super().__init__(name, position, "Property")
        self.price = price
        self.type = type
        self.owner = None

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
    
    def add_houses(self, quantity):
        if self.houses + quantity <= 5:
            self.houses += quantity
            super().owner.pay_money(self.building_cost * quantity)
        else:
            return False
    
    def remove_houses(self, quantity):
        if self.houses - quantity >= 0:
            self.houses -= quantity
            super().owner.receive_money(self.building_cost * quantity * 0.5)
        else:
            return False

class Railroad(Property):
    def __init__(self, name, position, price, rent_list):
        super().__init__(name, position, price, "Railroad")
        self.rent_list = rent_list

class Utility(Property):
    def __init__(self, name, position, price):
        super().__init__(name, position, price, "Utility")

class Event(Space):
    def __init__(self, name, position, type):
        super().__init__(name, position, "Event")
        self.type = type

class Tax(Event):
    def __init__(self, name, position, amount):
        super().__init__(name, position, "Tax")
        self.amount = amount

class Card(Event):
    def __init__(self, name, position, type):
        super().__init__(name, position, "Card")
        self.type = type

class Neutral(Event):
    def __init__(self, name, position):
        super().__init__(name, position, "Neutral")