import random

E = 1
H = 2
T = 3
J = 4


class Board(object):
    # Empty = 1
    # Jail = 2
    # Treasure = 3
    # Hotel = 4

    def __init__(self, board):
        self.board = board

class Game(object):
    def __init__(self, board, num_of_players = 2):
        self.initial_position = 0
        self.initial_money = 1000
        self.hotel_worth = 200
        self.hotel_rent = 50
        self.jail_fine = 150
        self.treasure_value = 200
        self.board = board
        self.players = self.create_players(num_of_players)
        self.num_of_players = num_of_players
        self.final_position = len(self.board) - 1
        self.players_completed_game = 0

    def create_players(self, num_of_players):
        temp = []
        for i in range(num_of_players):
            temp.append(Player(i, self.initial_position, self.initial_money)) # creating player and appending to temp
        return temp

    def start_game(self):
        turn = -1

        while(self.players_completed_game < self.num_of_players):
            turn =+ 1
            if self.players[turn].position == self.final_position: # player reached final position
                self.players_completed_game += 1
                continue

            while(True): # this will keep on generating dice move unless a valid move
                # like in ludo when player is on 99 and want to get just 1 to reach 100
                dice_move = random.randint(1,12) # generate random number from 1 to 12 , 

                if self.players[turn].position+dice_move > self.final_position:
                    continue
                else:
                    break

            self.players[turn].position += dice_move
            current_player_position = self.players[turn].position

            if self.board[current_player_position] == E:
                pass # empty nothin to do
            elif  self.board[current_player_position] == H: # reached hotel
                self.players[turn].money = self.players[turn].money + self.hotel_worth - self.hotel_rent
                self.players[turn].add_hotel()
            elif board[current_player_position] == J: # reached jail
                self.players[turn].money = self.players[turn].money - self.jail_fine
            else: # reached treasure
                self.players[turn].money = self.players[turn].money + self.hotel_worth 

        self.display_result()

    def display_result(self):
        self.players.sort(key=lambda x:x.money, reverse=True)
        for player in self.players:
            print('Player-{} has total worth {} and value of hotel bought : {}'.format(player.name, player.money, player.get_hotels()*self.hotel_worth))


class Player(object):
    def __init__(self, name, position, money):
        self.name = name
        self.position = position
        self.money = money
        self.bought_hotel = 0

    def add_hotel(self):
        self.bought_hotel += 1

    def get_hotels(self):
        return self.bought_hotel



# create board with variable E for empty , J for jail and so on
board = [E,E,J,H,E,T,E, J,H, H, H, H, H, H, H, H, E, T,H, H, H, H, E, E, H, T, H, H, H, H, H, H, J, H, E, H, H, J]
num_of_players = 3 # provide number of players


first_game = Game(board, num_of_players)
first_game.start_game()
