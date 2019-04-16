import random

E = 1
H = 2
T = 3
J = 4

board = [E,E,J,H,E,T,E, J, E, T, E, E, H, T, J, H, E, J]
initial_position = 0
initial_money = 1000
hotel_worth = 200
hotel_rent = 50
jail_fine = 150
treasure_value = 200

num_of_players = int(input("Enter num of players: "))

players = []

for i in range(num_of_players):
    players.append([initial_position,initial_money,i]) # every index of players array is a player with array as 2 values first is position on board and second is money in hand
                                        # i is the player number startinf from zero
final_position = len(board)-1

players_completed_game = 0

turn = -1

while(players_completed_game == num_of_players):
    turn =+ 1
    if players[turn][0] == final_position: # player reached final position
        players_completed_game += 1
        continue

    while(True): # this will keep on generating dice move unless a valid move
        # like in ludo when player is on 99 and want to get just 1 to reach 100
        dice_move = random.randint(2,12) # generate random number from 2 to 12

        if players[turn][0]+dice_move > final_position:
            continue

    players[turn][0] += dice_move
    player_position = players[turn][0]

    if board[player_position] == E:
        pass # do nothing
    elif  board[player_position] == H: # reached hotel
        players[turn][1] = players[turn][1] + hotel_worth - hotel_rent
    elif board[player_position] == J: # reached jail
        players[turn][1] = players[turn][1] - jail_fine
    else: # reached treasure
        players[turn][1] = players[turn][1] + 200 


# sort player according to money they have

players.sort(key=lambda x:x[1])

for player in players:
    print('Player-{} has total worth {}'.format(player[2], player[1]))