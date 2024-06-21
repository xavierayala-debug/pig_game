'''
This is a competetive dice game intended for 2+ players.
Each player will start off with a score of 0 in. Each member 
(starting with player 1) will have a chance to roll the dice to
reach desired max score. The person with the closest score wins, yay! 
But if your dice rolls a 1 you score is erased and your turn is over!!

'''

import random


def player_amount(players):

    list = {}

    for i in range(1, players + 1):
        list["player_" + str(i)] = 0

    return list

def roll_dice ():

    return random.randint(1,6)

def add(list, dice, num):

    player = "player_" + str(num)

    player_value = list[player]

    value = dice + player_value

    if dice == 1:
        list.update({player: 0})
    else:
        list.update({player:value})

    return  list

def winner(list, score):

    winner = None

    MAX = 0


    for player,value in list.items():
        if value <= score:
            if value > MAX:
                MAX = value
                winner = player

    if winner is not None:
        winner_statement = "\nThe winner is " + winner
    else:
        winner_statement = "\nNo winner yet."

    print(winner_statement)

    return winner


        

def main():

    done = False

    while not done:
        players = int(input("\nHow many players will there be? "))

        score = int(input("\nWhat do you want the winning score to be? "))

        player_scores = player_amount(players)

        for num in range(1, players +1):
            player = "\nPlayer " + str(num) 
            print(str(player) + " score is 0")

            playing = True

            while playing == True:
                roll_dice_input = input("\nDo you want to roll (y/n)? ").lower()

                if roll_dice_input == "y":
                    dice = roll_dice()

                    print("\n" + str(player) + " rolled a " + str(dice))

                    if dice == 1:
                        player_scores = add(player_scores, dice, num)
                        print ("\n" + str(player) + " new score: " + str(player_scores["player_" + str(num)]))
                        break
                    else:
                        player_scores = add(player_scores, dice, num)
                        print ("\n" + str(player) + " new score: " + str(player_scores["player_" + str(num)]))

                elif roll_dice_input == "n":
                    playing = False
                else:
                    print("\nNot a valid input")

        winner(player_scores, score)
        
        while 1:
            retry = input("\nRetry (y/n): ").lower()
            if retry == "y":
                break
            elif retry == "n":
                done = True
                break
            else:
                print("\nNot a valid character\n")
                        

main()