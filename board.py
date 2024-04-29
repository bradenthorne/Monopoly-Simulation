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
            {"description": "Go back 3 spaces", "action": "go back three spaces"},
            {"description": "Go to jail", "action": "go to jail"},
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
            {"description": "Go to Jail", "action": "go to jail"},
            {"description": "Holiday fund", "action": "receive money", "amount": 100},
            {"description": "Income tax refund", "action":"receive money" , "amount": 20},
            {"description": "Birthday", "action": "receive money", "amount": 30},
            {"description": "Life Insurance Matures", "action": "receive money", "amount": 100},
            {"description": "Hospital Fees", "action": "pay money", "amount": 100},
            {"description": "School Fees", "action": "pay money", "amount": 50},
            {"description": "Consultancy Fee", "action": "receive money", "amount": 25},
            {"description": "Repair", "action": "repairs"},
            {"description": "Beauty Contest", "action": "receive money", "amount": 10},
            {"description": "Inheritance", "action": "receive money", "amount": 100}]
        
        random.shuffle(self.chance_cards)
        random.shuffle(self.community_chest_cards)

        self.street_dict = {
            "Mediterranean Avenue" : 
                {
                    "Position": 1,
                    "Price": 60,
                    "Rent": [2, 10, 30, 90, 160, 250],
                    "Building Cost": 50,
                    "Group": "Brown"
                },
            "Baltic Avenue" : 
                {
                    "Position": 3,
                    "Price": 60,
                    "Rent": [4, 20, 60, 180, 320, 450],
                    "Building Cost": 50,
                    "Group": "Brown"
                },
            "Oriental Avenue" : 
                {
                    "Position": 6,
                    "Price": 100,
                    "Rent": [6, 30, 90, 270, 400, 550],
                    "Building Cost": 50,
                    "Group": "Light Blue"
                },
            "Vermont Avenue" : 
                {
                    "Position": 8,
                    "Price": 100,
                    "Rent": [6, 30, 90, 270, 400, 550],
                    "Building Cost": 50,
                    "Group": "Light Blue"
                },
            "Connecticut Avenue" : 
                {
                    "Position": 9,
                    "Price": 120,
                    "Rent": [8, 40, 100, 300, 450, 600],
                    "Building Cost": 50,
                    "Group": "Light Blue"
                },
            "St. Charles Place" : 
                {
                    "Position": 11,
                    "Price": 140,
                    "Rent": [10, 50, 150, 450, 625, 750],
                    "Building Cost": 100,
                    "Group": "Pink"
                },
            "States Avenue" : 
                {
                    "Position": 13,
                    "Price": 140,
                    "Rent": [10, 50, 150, 450, 625, 750],
                    "Building Cost": 100,
                    "Group": "Pink"
                },
            "Virginia Avenue" : 
                {
                    "Position": 14,
                    "Price": 160,
                    "Rent": [12, 60, 180, 500, 700, 900],
                    "Building Cost": 100,
                    "Group": "Pink"
                },
            "St. James Place" : 
                {
                    "Position": 16,
                    "Price": 180,
                    "Rent": [14, 70, 200, 550, 750, 950],
                    "Building Cost": 100,
                    "Group": "Orange"
                },
            "Tennessee Avenue" : 
                {
                    "Position": 18,
                    "Price": 180,
                    "Rent": [14, 70, 200, 550, 750, 950],
                    "Building Cost": 100,
                    "Group": "Orange"
                },
            "New York Avenue" : 
                {
                    "Position": 19,
                    "Price": 200,
                    "Rent": [16, 80, 220, 600, 800, 1000],
                    "Building Cost": 100,
                    "Group": "Orange"
                },
            "Kentucky Avenue" : 
                {
                    "Position": 21,
                    "Price": 220,
                    "Rent": [18, 90, 250, 700, 875, 1050],
                    "Building Cost": 150,
                    "Group": "Red"
                },
            "Indiana Avenue" : 
                {
                    "Position": 23,
                    "Price": 220,
                    "Rent": [18, 90, 250, 700, 875, 1050],
                    "Building Cost": 150,
                    "Group": "Red"
                },
            "Illinois Avenue" : 
                {
                    "Position": 24,
                    "Price": 240,
                    "Rent": [20, 100, 300, 750, 925, 1100],
                    "Building Cost": 150,
                    "Group": "Red"
                },
            "Atlantic Avenue" : 
                {
                    "Position": 26,
                    "Price": 260,
                    "Rent": [22, 110, 330, 800, 975, 1150],
                    "Building Cost": 150,
                    "Group": "Yellow"
                },
            "Ventnor Avenue" : 
                {
                    "Position": 27,
                    "Price": 260,
                    "Rent": [22, 110, 330, 800, 975, 1150],
                    "Building Cost": 150,
                    "Group": "Yellow"
                },
            "Marvin Gardens" : 
                {
                    "Position": 29,
                    "Price": 280,
                    "Rent": [24, 120, 360, 850, 1025, 1200],
                    "Building Cost": 150,
                    "Group": "Yellow"
                },
            "Pacific Avenue" : 
                {
                    "Position": 31,
                    "Price": 300,
                    "Rent": [26, 130, 390, 900, 1100, 1275],
                    "Building Cost": 200,
                    "Group": "Green"
                },
            "North Carolina Avenue" : 
                {
                    "Position": 32,
                    "Price": 300,
                    "Rent": [26, 130, 390, 900, 1100, 1275],
                    "Building Cost": 200,
                    "Group": "Green"
                },
            "Pennsylvania Avenue" : 
                {
                    "Position": 34,
                    "Price": 320,
                    "Rent": [28, 150, 450, 1000, 1200, 1400],
                    "Building Cost": 200,
                    "Group": "Green"
                },
            "Park Place" : 
                {
                    "Position": 37,
                    "Price": 350,
                    "Rent": [35, 175, 500, 1100, 1300, 1500],
                    "Building Cost": 200,
                    "Group": "Dark Blue"
                },
            "Boardwalk" : 
                {
                    "Position": 39,
                    "Price": 400,
                    "Rent": [50, 200, 600, 1400, 1700, 2000],
                    "Building Cost": 200,
                    "Group": "Dark Blue"
                }
        }

        self.railroad_dict = {
            "Reading Railroad" : 
                {
                    "Position": 5,
                    "Price": 200,
                    "Rent": [25, 50, 100, 200]
                },
            "Pennsylvania Railroad" : 
                {
                    "Position": 15,
                    "Price": 200,
                    "Rent": [25, 50, 100, 200]
                },
            "B. & O. Railroad" : 
                {
                    "Position": 25,
                    "Price": 200,
                    "Rent": [25, 50, 100, 200]
                },
            "Short Line" : 
                {
                    "Position": 35,
                    "Price": 200,
                    "Rent": [25, 50, 100, 200]
                }
        }
        
        self.utility_dict = {
            "Electric Company" : 
                {
                    "Position": 12,
                    "Price": 150
                },
            "Water Works" : 
                {
                    "Position": 28,
                    "Price": 150
                }
        }
        
        self.tax_dict = {
            "Income Tax" :
                {
                    "Position": 4,
                    "Amount": 200
                },
            "Luxury Tax" :
                {
                    "Position": 38,
                    "Amount": 100
                }
        }
        
        self.card_dict = {
            "Chance" :
                {
                    "Positions": [7, 22, 36],
                },
            "Community Chest" :
                {
                    "Positions": [2, 17, 33]
                }
        }

        self.neutral_dict = {
            "Go" :
                {
                    "Position": 0
                },
            "Jail":
                {
                    "Position": 10
                },
            "Free Parking" :
                {
                    "Position": 20
                },
            "Go to Jail" :
                {
                    "Position": 30
                }
        }
        
        self.monopoly_counts = {"Brown": 2, "Light Blue": 3, "Pink": 3, "Orange": 3, "Red": 3, "Yellow": 3, "Green": 3, "Dark Blue": 2, "Railroad": 4, "Utility": 2}

    def add_space(self, space):
        self.spaces[space.position] = space
    
    def add_player(self, player):
        self.players.append(player)