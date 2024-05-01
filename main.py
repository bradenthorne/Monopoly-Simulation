import logging

import pandas as pd
from tqdm import tqdm

from board import Board
from player import Player
from space import Street, Railroad, Utility, Tax, Card, Neutral

logging.basicConfig(filename='monopoly_log.log', level=logging.INFO, format='%(message)s', filemode='w')

REPLICATIONS = 1000
TURNS = 50
PLAYERS = 4
TRACK_SPACES = False
TRACK_ROI = False

def initialize_board(board):

    # Add streets to board
    street_dict = board.street_dict
    for street_name, street_info in street_dict.items():
        street = Street(street_name, street_info["Position"], street_info["Price"], street_info["Rent"], street_info["Building Cost"], street_info["Group"])
        board.add_space(street)
    
    # Add railroads to board
    railroad_dict = board.railroad_dict
    for railroad_name, railroad_info in railroad_dict.items():
        railroad = Railroad(railroad_name, railroad_info["Position"], railroad_info["Price"], railroad_info["Rent"])
        board.add_space(railroad)

    # Add utilities to board
    utility_dict = board.utility_dict
    for utility_name, utility_info in utility_dict.items():
        utility = Utility(utility_name, utility_info["Position"], utility_info["Price"])
        board.add_space(utility)

    # Add taxes to board
    tax_dict = board.tax_dict
    for tax_name, tax_info in tax_dict.items():
        tax = Tax(tax_name, tax_info["Position"], tax_info["Amount"])
        board.add_space(tax)
    
    # Add cards to board
    card_dict = board.card_dict
    for deck, card_info in card_dict.items():
        for position in card_info["Positions"]:
            card = Card(deck, position)
            board.add_space(card)

    # Add neutrals to board
    neutral_dict = board.neutral_dict
    for neutral_name, neutral_info in neutral_dict.items():
        neutral = Neutral(neutral_name, neutral_info["Position"])
        board.add_space(neutral)
    
    # Initialize monopoly_dict and monopoly_count
    for _, space in board.spaces.items():
        if space.is_property:
            if space.group not in board.monopoly_dict.keys():
                board.monopoly_dict[space.group] = [space]
            else:
                board.monopoly_dict[space.group].append(space)
    
    for group, property_list in board.monopoly_dict.items():
        board.monopoly_counts[group] = len(property_list)

    # Add players to board
    for i in range(1, PLAYERS + 1):
        player = Player(i, 0.5) # Change risk tolerance values here
        board.add_player(player)

# Game loop
def main():
    board = Board()
    initialize_board(board)
    for turn in range(TURNS):
        if len(board.get_active_players()) == 1:
            break
        logging.info(f"Turn {turn + 1}")
        for player in board.players:
            if player.status == "Active":
                player.take_turn(board)
        board.log_player_info()
    if TRACK_SPACES:
        return {board.spaces[key].name: board.spaces[key].count for key,_ in board.spaces.items()}
    if TRACK_ROI:
        return {board.spaces[key].name: {"Money Invested": board.spaces[key].money_invested, "Rent Collected": board.spaces[key].rent_collected} for key,_ in board.spaces.items() if board.spaces[key].is_property}


if __name__ == "__main__":
    results_dict = {}
    investment_dict = {}
    rent_dict = {}
    for i in tqdm (range(REPLICATIONS), desc="Running..."):
        if TRACK_SPACES:
            result = main()
            for key, value in result.items():
                if key not in results_dict:
                    results_dict[key] = []
                results_dict[key].append(value)
            df = pd.DataFrame.from_dict(results_dict, orient='index')
            df.columns = [f"Replication {i+1}" for i in range(REPLICATIONS)]
            df.to_excel('SpaceFrequencyResults.xlsx', sheet_name='Frequency Results')
        elif TRACK_ROI:
            result = main()
            for key, value in result.items():
                if key not in investment_dict:
                    investment_dict[key] = []
                    rent_dict[key] = []
                investment_dict[key].append(value["Money Invested"])
                rent_dict[key].append(value["Rent Collected"])
            investment_df = pd.DataFrame.from_dict(investment_dict, orient='index')
            rent_df = pd.DataFrame.from_dict(rent_dict, orient='index')
            writer = pd.ExcelWriter('ROI_Results.xlsx', engine='xlsxwriter')
            investment_df.to_excel(writer, sheet_name='Money Invested')
            rent_df.to_excel(writer, sheet_name='Rent Collected')
            writer.close()
        else:
            main()