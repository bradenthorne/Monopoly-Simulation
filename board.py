import random

class Board:
    def __init__(self):
        self.spaces = {}
        self.players = []
        self.chance_cards = [
            {"description": "Advance to Boardwalk", "action": "move", "destination": 39},
            {"description": "Advance to Go", "action": "move", "destination": 0},
            {"description": "Advance to Illinois Avenue", "action": "move", "destination": 24},
            {"description": "Advance to St. Charles Place", "action": "move", "destination": 11},
            {"description": "Advance to the nearest Railroad", "action": "railroad"},
            {"description": "Advance to the nearest Railroad", "action": "railroad"},
            {"description": "Advance to the nearest Utility", "action": "utility"},
            {"description": "Bank pays you a dividend of $50", "action": "receive money", "amount": 50},
            {"description": "Get Out of Jail Free", "action": "get out of jail"},
            {"description": "Go back 3 spaces", "action": "three spaces"},
            {"description": "Go to jail", "action": "jail"},
            {"description": "Make repairs on all your property", "action": "repairs"},
            {"description": "Speeding fine", "action": "pay money", "amount": 15},
            {"description": "Take a trip to Reading Railroad", "action": "move", "destination": 5},
            {"description": "Pay each player $50", "action": "pay money", "amount": 150},
            {"description": "Your building load matures", "action": "receive money", "amount": 150}]

        self.community_chest_cards = [
            {"description": "Advance to Go", "action": "move", "destination": 0},
            {"description": "Bank error", "action": "receive money", "amount": 200},
            {"description": "Doctor's fee", "action": "pay money" , "amount": 50},
            {"description": "Sale of stock", "action": "receive money", "amount": 50},
            {"description": "Get Out of Jail Free", "action": "get out of jail"},
            {"description": "Go to Jail", "action": "jail"},
            {"description": "Holiday fund", "action": "receive money", "amount": 100},
            {"description": "Income tax refund", "action":"receive money" , "amount": 20},
            {"description": "Birthday", "action": "receive money", "amount": 30},
            {"description": "Life Insurance Matures", "action": "receive money", "amount": 100},
            {"description": "Hospital Fees", "action": "pay money", "amount": 100},
            {"description": "School Fees", "action": "pay money", "amount": 50},
            {"description": "Consultancy Fee", "action": "receive money", "amount": 25},
            {"description": "Repair", "action": "repair"},
            {"description": "Beauty Contest", "action": "receive money", "amount": 10},
            {"description": "Inheritance", "action": "receive money", "amount": 100}]
        
        random.shuffle(self.chance_cards)
        random.shuffle(self.community_chest_cards)
    
    def add_space(self, space):
        self.spaces[space.position] = space
    
    def add_player(self, player):
        self.players.append(player)