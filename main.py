from board import Board
from player import Player
from space import Street, Railroad, Utility, Tax, Card, Neutral
from group import Group
import logging

import pandas as pd

logging.basicConfig(filename='monopoly_log.log', level=logging.INFO, format='%(message)s', filemode='w')

REPLICATIONS = 1
TURNS = 30
PLAYERS = 4

def initialize_board(board):
    # Street information
    street_dict = {
        "Mediterranean Avenue" : 
            {
                "Position": 1,
                "Price": 60,
                "Rent": [2, 10, 30, 90, 160, 250],
                "Building Cost": 50,
                "Group": Group.BROWN
            },
        "Baltic Avenue" : 
            {
                "Position": 3,
                "Price": 60,
                "Rent": [4, 20, 60, 180, 320, 450],
                "Building Cost": 50,
                "Group": Group.BROWN
            },
        "Oriental Avenue" : 
            {
                "Position": 6,
                "Price": 100,
                "Rent": [6, 30, 90, 270, 400, 550],
                "Building Cost": 50,
                "Group": Group.LIGHT_BLUE
            },
        "Vermont Avenue" : 
            {
                "Position": 8,
                "Price": 100,
                "Rent": [6, 30, 90, 270, 400, 550],
                "Building Cost": 50,
                "Group": Group.LIGHT_BLUE
            },
        "Connecticut Avenue" : 
            {
                "Position": 9,
                "Price": 120,
                "Rent": [8, 40, 100, 300, 450, 600],
                "Building Cost": 50,
                "Group": Group.LIGHT_BLUE
            },
        "St. Charles Place" : 
            {
                "Position": 11,
                "Price": 140,
                "Rent": [10, 50, 150, 450, 625, 750],
                "Building Cost": 100,
                "Group": Group.PINK
            },
        "States Avenue" : 
            {
                "Position": 13,
                "Price": 140,
                "Rent": [10, 50, 150, 450, 625, 750],
                "Building Cost": 100,
                "Group": Group.PINK
            },
        "Virginia Avenue" : 
            {
                "Position": 14,
                "Price": 160,
                "Rent": [12, 60, 180, 500, 700, 900],
                "Building Cost": 100,
                "Group": Group.PINK
            },
        "St. James Place" : 
            {
                "Position": 16,
                "Price": 180,
                "Rent": [14, 70, 200, 550, 750, 950],
                "Building Cost": 100,
                "Group": Group.ORANGE
            },
        "Tennessee Avenue" : 
            {
                "Position": 18,
                "Price": 180,
                "Rent": [14, 70, 200, 550, 750, 950],
                "Building Cost": 100,
                "Group": Group.ORANGE
            },
        "New York Avenue" : 
            {
                "Position": 19,
                "Price": 200,
                "Rent": [16, 80, 220, 600, 800, 1000],
                "Building Cost": 100,
                "Group": Group.ORANGE
            },
        "Kentucky Avenue" : 
            {
                "Position": 21,
                "Price": 220,
                "Rent": [18, 90, 250, 700, 875, 1050],
                "Building Cost": 150,
                "Group": Group.RED
            },
        "Indiana Avenue" : 
            {
                "Position": 23,
                "Price": 220,
                "Rent": [18, 90, 250, 700, 875, 1050],
                "Building Cost": 150,
                "Group": Group.RED
            },
        "Illinois Avenue" : 
            {
                "Position": 24,
                "Price": 240,
                "Rent": [20, 100, 300, 750, 925, 1100],
                "Building Cost": 150,
                "Group": Group.RED
            },
        "Atlantic Avenue" : 
            {
                "Position": 26,
                "Price": 260,
                "Rent": [22, 110, 330, 800, 975, 1150],
                "Building Cost": 150,
                "Group": Group.YELLOW
            },
        "Ventnor Avenue" : 
            {
                "Position": 27,
                "Price": 260,
                "Rent": [22, 110, 330, 800, 975, 1150],
                "Building Cost": 150,
                "Group": Group.YELLOW
            },
        "Marvin Gardens" : 
            {
                "Position": 29,
                "Price": 280,
                "Rent": [24, 120, 360, 850, 1025, 1200],
                "Building Cost": 150,
                "Group": Group.YELLOW
            },
        "Pacific Avenue" : 
            {
                "Position": 31,
                "Price": 300,
                "Rent": [26, 130, 390, 900, 1100, 1275],
                "Building Cost": 200,
                "Group": Group.GREEN
            },
        "North Carolina Avenue" : 
            {
                "Position": 32,
                "Price": 300,
                "Rent": [26, 130, 390, 900, 1100, 1275],
                "Building Cost": 200,
                "Group": Group.GREEN
            },
        "Pennsylvania Avenue" : 
            {
                "Position": 34,
                "Price": 320,
                "Rent": [28, 150, 450, 1000, 1200, 1400],
                "Building Cost": 200,
                "Group": Group.GREEN
            },
        "Park Place" : 
            {
                "Position": 37,
                "Price": 350,
                "Rent": [35, 175, 500, 1100, 1300, 1500],
                "Building Cost": 200,
                "Group": Group.DARK_BLUE
            },
        "Boardwalk" : 
            {
                "Position": 39,
                "Price": 400,
                "Rent": [50, 200, 600, 1400, 1700, 2000],
                "Building Cost": 200,
                "Group": Group.DARK_BLUE
            }
    }
    # Add streets to board
    for street_name, street_info in street_dict.items():
        street = Street(street_name, street_info["Position"], street_info["Price"], street_info["Rent"], street_info["Building Cost"], street_info["Group"])
        board.add_space(street)
    
    # Railroad information
    railroad_dict = {
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
    # Add railroads to board
    for railroad_name, railroad_info in railroad_dict.items():
        railroad = Railroad(railroad_name, railroad_info["Position"], railroad_info["Price"], railroad_info["Rent"])
        board.add_space(railroad)

    # Utility information
    utility_dict = {
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
    # Add utilities to board
    for utility_name, utility_info in utility_dict.items():
        utility = Utility(utility_name, utility_info["Position"], utility_info["Price"])
        board.add_space(utility)

    # Tax information
    tax_dict = {
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
    # Add taxes to board
    for tax_name, tax_info in tax_dict.items():
        tax = Tax(tax_name, tax_info["Position"], tax_info["Amount"])
        board.add_space(tax)
    
    # Card information
    card_dict = {
        "Chance" :
            {
                "Positions": [7, 22, 36],
            },
        "Community Chest" :
            {
                "Positions": [2, 17, 33]
            }
    }
    # Add cards to board
    for card_name, card_info in card_dict.items():
        for position in card_info["Positions"]:
            card = Card(card_name, position, card_name)
            board.add_space(card)

    # Neutral information
    neutral_dict = {
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
    # Add neutrals to board
    for neutral_name, neutral_info in neutral_dict.items():
        neutral = Neutral(neutral_name, neutral_info["Position"])
        board.add_space(neutral)
    
    # Add players to board
    for i in range(1, PLAYERS + 1):
        player = Player(i)
        board.add_player(player)

# Game loop
def main():
    board = Board()
    initialize_board(board)
    for turn in range(TURNS):
        logging.info(f"Turn {turn + 1}")
        for player in board.players:
            if player.status == "Active":
                player.take_turn(board)
    return {board.spaces[key].name: board.spaces[key].count for key,_ in board.spaces.items()}

if __name__ == "__main__":
    results_dict = {}
    for i in range(REPLICATIONS):
        result = main()
        for key, value in result.items():
            if key not in results_dict:
                results_dict[key] = []
            results_dict[key].append(value)
    df = pd.DataFrame.from_dict(results_dict, orient='index')
    df.columns = [f"Replication {i+1}" for i in range(REPLICATIONS)]
    df.to_excel('SpaceFrequencyResults.xlsx', sheet_name='Frequency Results')