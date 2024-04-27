import random
import logging

class Player:
    def __init__(self, player_number):
        self.player_number = player_number
        self.position = 0
        self.properties = []
        self.money = 1500
        self.in_jail = False
        self.turns_in_jail = 0
        self.get_out_of_jail_inv = 0
        self.status = "Active"
        self.doubles_count = 0
        self.turn_active = False

    def roll_dice(self):
        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)
        return (roll1, roll2, (roll1 == roll2))

    
    def move(self, steps, board):
        if (self.position < 40 and self.position + steps >= 40):
            self.receive_money(200)
        self.position = (self.position + steps) % 40
        if self.position in [7, 22, 36]:
            self.pull_card('chance', board)
        if self.position in [2, 17, 33]:
            self.pull_card('community chest', board)
        if self.position == 30:
            self.go_to_jail()
    
    def teleport(self, target):
        self.position = target

    def pull_card(self, type, board):
        if type == 'chance':
            card = board.chance_cards.pop(0)
            board.chance_cards.append(card)
        else:
            card = board.community_chest_cards.pop(0)
            board.community_chest_cards.append(card)
        match card['action']:
            case 'move':
                self.teleport(card['destination'])
            case 'receive money':
                self.receive_money(card['amount'])
            case 'pay money':
                self.pay_money(card['amount'])
            case 'get out of jail':
                self.get_out_of_jail_inv += 1
            case 'jail':
                self.position = 10
                self.in_jail = True
            case 'three spaces':
                self.position = (self.position + 3) % 40
            case 'railroad':
                if self.position == 7:
                    self.teleport(15)
                if self.position == 22:
                    self.teleport(25)
                if self.position == 36:
                    self.receive_money(200)
                    self.teleport(5)
            case 'utility':
                if self.position == 7 | 36:
                    self.position = 12
                if self.position == 22:
                    self.position = 28

    def go_to_jail(self):
        self.position = 10
        self.in_jail = True

    def receive_money(self, amount):
        self.money += amount

    def pay_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        else:
            return False
        
    def buy_property(self, property):
        if self.money >= property.price:
            self.properties.append(property)
            self.money -= property.price
            return True
        else:
            return False
    
    def end_turn(self):
        self.turn_active = False
        self.doubles_count = 0
    
    def take_turn(self, board):
        self.turn_active = True
        logging.info(f"Player {self.player_number}'s turn!")
        while self.turn_active:
            roll1, roll2, doubles = self.roll_dice()
            logging.info(f"Player {self.player_number} rolled {roll1} and {roll2}")

            if doubles:
                logging.info("It's doubles!")
                self.doubles_count += 1
                if self.doubles_count == 3:
                    self.go_to_jail()
                    board.spaces[self.position].count += 1
                    self.end_turn()
                else:
                    self.move(roll1 + roll2, board)
                    board.spaces[self.position].count += 1

            else:
                self.move(roll1 + roll2, board)
                board.spaces[self.position].count += 1
                self.end_turn()
            logging.info(f"Player {self.player_number} is now at position {self.position}, {board.spaces[self.position].name}")
