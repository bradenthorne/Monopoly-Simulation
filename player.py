import random
import logging

class Player:
    def __init__(self, player_number, risk_tolerance):
        self.player_number = player_number
        self.risk_tolerance = risk_tolerance
        self.position = 0
        self.properties = []
        self.property_count = {}
        self.monopolies = []
        self.money = 1500
        self.in_jail = False
        self.turns_in_jail = 0
        self.get_out_of_jail_inv = 0
        self.status = "Active"
        self.doubles_count = 0
        self.turn_active = False

    # Core Gameplay Functions
    def take_turn(self, board):
        self.turn_active = True
        logging.info(f"Player {self.player_number}'s turn!")
        self.propose_trade(board)
        self.build_houses(board)
        while self.turn_active:
            roll1, roll2, doubles = self.roll_dice()
            logging.info(f"Player {self.player_number} rolled {roll1} and {roll2}")
            if doubles:
                logging.info("It's doubles!")
                self.doubles_count += 1
                if self.doubles_count == 3:
                    self.go_to_jail(board)
                else:
                    self.move(roll1 + roll2, board)
            else:
                self.move(roll1 + roll2, board)
                self.end_turn(board)

    def roll_dice(self):
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        return (roll1, roll2, (roll1 == roll2))
  
    def move(self, steps, board):
        if self.passed_go(steps):
            self.receive_money(200)
        self.position = (self.position + steps) % 40
        self.log_position(board)
        self.space_event(self.position, board)

    def space_event(self, position, board):
        current_space = board.spaces[position]
        match current_space.type:
            case "Street" | "Railroad" | "Utility":
                if current_space.owner == self:
                    return
                elif current_space.owner == None:
                    if (current_space.price / self.money) <= self.risk_tolerance:
                        self.buy_property(current_space)
                else:
                    self.pay_rent(current_space)
            case 'Tax':
                self.pay_tax(current_space)
            case 'Card':
                self.pull_card(position, board)
            case 'Neutral':
                if position == 30:
                    self.go_to_jail(board)

    def pull_card(self, position, board):
        if position in [7, 22, 36]:
            card = board.chance_cards.pop(0)
            board.chance_cards.append(card)
        else:
            card = board.community_chest_cards.pop(0)
            board.community_chest_cards.append(card)
        self.card_event(card, board)
    
    def card_event(self, card, board):
        self.log_card(card)
        match card['action']:
            case 'move':
                self.teleport(card['destination'], board)
            case 'receive money':
                self.receive_money(card['amount'])
            case 'pay money':
                self.pay_money(card['amount'])
            case 'get out of jail':
                self.get_out_of_jail_inv += 1
            case 'go to jail':
                self.go_to_jail(board)
            case 'go back three spaces':
                self.position = (self.position - 3) % 40
            case 'railroad':
                if self.position == 7:
                    self.teleport(15, board)
                if self.position == 22:
                    self.teleport(25, board)
                if self.position == 36:
                    self.receive_money(200)
                    self.teleport(5, board)
            case 'utility':
                if self.position == 7 | 36:
                    self.teleport(12, board)
                if self.position == 22:
                    self.teleport(28, board)
    
    def eliminate_player(self, other=None):
        self.status = 'Eliminated'
        self.turn_active = False
        if other is not None:
            for property in self.properties:
                property.set_owner(other)
                other.properties.append(property)
            other.monopolies.extend(self.monopolies)
            for key, value in self.property_count.items():
                other.property_count[key] = other.property_count.get(key, 0) + value
            self.clear_properties()
        else:
            for property in self.properties:
                property.clear_owner()
            self.clear_properties()
            logging.info(f"Player {other.player_number} now has {[property.name for property in other.properties]}")
        logging.info(f"Player {self.player_number} has been eliminated")

    def end_turn(self, board):
        self.turn_active = False
        self.doubles_count = 0
        self.update_monopolies(board)

    # Special Movement Functions
    def teleport(self, target, board):
        self.position = target
        self.log_position(board)
        self.space_event(target, board)

    def go_to_jail(self, board):
        self.position = 10
        self.in_jail = True
        self.end_turn(board)

    # Financial Transactions
    def pay_money(self, amount, other=None):
        self.money -= amount
        if other is not None:
            other.money += amount
    
    def receive_money(self, amount):
        self.money += amount

    def buy_property(self, property):
        self.pay_money(property.price)
        self.properties.append(property)
        property.set_owner(self)
        if property.group in self.property_count.keys():
            self.property_count[property.group] += 1
        else:
            self.property_count[property.group] = 1
        self.log_purchase(property)
    
    def pay_rent(self, property):
        owner = property.owner
        exchange_balance = min(property.current_rent, self.money)
        self.pay_money(exchange_balance, owner)
        self.log_rent_payment(owner, exchange_balance)
        if self.money == 0:
            self.eliminate_player(owner)

    def pay_tax(self, space):
        self.pay_money(space.amount)
        self.log_tax(space.amount)
    
    def build_houses(self, board):
        buildable_monopolies = [group for group in self.monopolies if board.monopoly_dict[group][0].can_buy_houses]
        if len(buildable_monopolies) == 0:
            return
        else:
            target_monopoly = random.choice(buildable_monopolies)
            property_list = board.monopoly_dict[target_monopoly]
            if property_list[0].houses == 5:
                return
            total_building_cost = property_list[0].building_cost * len(property_list)
            if total_building_cost / self.money <= self.risk_tolerance:
                for property in property_list:
                    property.add_houses(1)
                self.log_house_purchase(target_monopoly)


    # Trading
    def propose_trade(self, board):
        for property_group, count in self.property_count.items():
            if count == board.monopoly_counts[property_group] - 1:
                for player in board.players:
                    if player != self:
                        if property_group in player.property_count.keys():
                            target_property = [property for property in player.properties if property.group == property_group][0]
                            if ((target_property.price * 2) / self.money) <= self.risk_tolerance:
                                self.make_trade(player, target_property)
    
    def make_trade(self, other, property):
        self.pay_money(property.price * 2, other)
        property.set_owner(self)
        self.properties.append(property)
        other.properties.remove(property)
        del other.property_count[property.group]
        self.property_count[property.group] += 1
        logging.info(f"Player {other.player_number} traded {property.name} to Player {self.player_number} for $ {property.price * 2}")

    # Logging and Helper Functions
    def log_position(self, board):
        logging.info(f"Player {self.player_number} is now at position {self.position}, {board.spaces[self.position].name}")
        board.spaces[self.position].count += 1
    
    def log_card(self, card):
        logging.info(f"The card says: {card['description']}")
    
    def log_purchase(self, property):
        logging.info(f"Player {self.player_number} purchased {property.name} for $ {property.price}")
        logging.info(f"Player {self.player_number} now has $ {self.money}")
        #logging.info(f"Their property group count is {self.property_count}")

    def log_rent_payment(self, other, amount):
        logging.info(f"Player {self.player_number} paid $ {amount} in rent to Player {other.player_number}")
        logging.info(f"Player {self.player_number} now has $ {self.money}")
        logging.info(f"Player {other.player_number} now has $ {other.money}")

    def log_tax(self, amount):
        logging.info(f"Player {self.player_number} paid $ {amount} in taxes")
        logging.info(f"Player {self.player_number} now has $ {self.money}")
    
    def log_house_purchase(self, group):
        logging.info(f"Player {self.player_number} purchased houses on the {group} group")

    def passed_go(self, steps):
        return (self.position + steps >= 40)
    
    def update_monopolies(self, board):
        for property_group, count in self.property_count.items():
            if count == board.monopoly_counts[property_group]:
                if property_group not in self.monopolies:
                    self.monopolies.append(property_group)
    
    def clear_properties(self):
        self.properties = []
        self.property_count = {}