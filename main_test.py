#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:43:40 2023

@author: shyam
"""

import sys
 
# total arguments
n = len(sys.argv)
# Using argparse module
list_ap=[]
for i in range(1, 3):
#    print(i)
    args=sys.argv[i]
    list_ap.append(int(args))
    
first_player=sys.argv[3]
#print(first_player)
depth=sys.argv[4]




def minimax(state, alpha, beta, MaximumTurn, depth):
    if depth == 0 or sum(state) == 1 or sum(state) == 0:
        if sum(state) == 1 and MaximumTurn:
            return (-1, [state])
        elif sum(state) == 1 and not MaximumTurn:
            return (1, [state])
        elif sum(state) == 0 and MaximumTurn:
            return (1, [state])
        elif sum(state) == 0 and not MaximumTurn:
            return (-1, [state])
    if MaximumTurn:
        resist_max = -float('inf')
        resist = []
        for i in next_move(state):
            val_move, temp_val_move = minimax(i, alpha, beta, not MaximumTurn, depth-1)
            if val_move > resist_max:
                resist_max = val_move
                resist = temp_val_move
            alpha = max(alpha, val_move)
            if alpha >= beta:
                break
        return resist_max, [state] + resist
    else:
        resist_min = float('inf')
        resist = []
        for i in next_move(state):
            val_move, temp_val_move = minimax(i, alpha, beta, not MaximumTurn, depth-1)
            if val_move < resist_min:
                resist_min = val_move
                resist = temp_val_move
            beta = min(beta, val_move)
            if alpha >= beta:
                break
        return resist_min, [state] + resist




def next_move(state):
    n_visits = set()
    resist = []
    
    for i, val in enumerate(state):
        for m in range(1, val):
            temp_state = state[:]
            temp_state[i] -= m
            new_order = tuple(sorted(temp_state))
            if new_order not in n_visits:
                resist.append(temp_state)
                n_visits.add(new_order)  
                
    return resist


from search_algo_up import minimax
class beam(object):
    def __init__(self, beam):
        self.beam = beam

    def update(self, piles, num):
        self.beam[piles] -= num

    def computethink(self,depth):
        self.beam = minimax(self.beam, -float('inf'), float('inf'), True,depth)[1][1]

def Ischeck(remove, beam):
    if not remove or len(remove) != 2: 
        return False
    if remove[0] > 0 and remove[1] >= 0:
        return True

if __name__ == "__main__":

    print("Starting Game Nim.. Get ready!")
    #print("first_player",first_player)

    game = beam(list_ap)
    print("Which colour do you choose?")
    player_win = True
    while True:
        # player's turn
        if first_player=='human':
            user = str(input("Player turn: "))
            player_color=user
            marble_cnt=[1]
            player_remove=[]
            player_remove.extend(marble_cnt)
            if player_color=='red':
                player_remove.append(0)
            elif player_color=='blue':
                player_remove.append(1)
            while not Ischeck(player_remove, game.beam):
                print("Invalid move! Please input again.")
                user = str(input("Player turn: "))
                player_color=user
                marble_cnt=[1]
                player_remove=[]
                player_remove.extend(marble_cnt)
                if player_color=='red':
                    player_remove.append(0)
                if player_color=='blue':
                    player_remove.append(1)
#            player_remove = [int(i) for i in user.split(' ')]
        
            game.update(player_remove[1], player_remove[0])
            print("Player Pile state %s" % (game.beam))
            if sum(game.beam) == 0:
                player_win = False
                break
            elif sum(game.beam) == 1:
                break
            print("Computer turn")
            game.computethink(int(depth))
            vals=player_remove
        #print("vals",vals)
#            updated_vals=(abs(vals[0]-list_ap[0]),abs(vals[1]-list_ap[1]))
#            updated_val=list(updated_vals)
            print("Computer Pile state %s" % (game.beam))
            if sum(game.beam) == 0:
                break
            elif sum(game.beam) == 1:
                player_win = False
                break
        else:
            game.computethink(int(depth))
            print("Computer Pile state %s" % (game.beam))
            if sum(game.beam) == 0:
                break
            elif sum(game.beam) == 1:
                player_win = False
                break
            user = str(input("Player turn: "))
            player_color=user
            marble_cnt=[1]
            player_remove=[]
            player_remove.extend(marble_cnt)
            if player_color=='red':
                player_remove.append(0)
            else:
                player_remove.append(1)
            while not Ischeck(player_remove, game.beam):
                 print("Invalid move! Please input again.")
                 user = str(input("Player turn: "))
                 player_color=user
                 marble_cnt=[1]
                 player_remove=[]
                 player_remove.extend(marble_cnt)
                 if player_color=='red':
                     player_remove.append(0)
                 if player_color=='blue':
                     player_remove.append(1)
 #            player_remove = [int(i) for i in user.split(' ')]
         
            game.update(player_remove[1], player_remove[0])
            print("Player Pile state %s" % (game.beam))
            if sum(game.beam) == 0:
                player_win = False
                break
            elif sum(game.beam) == 1:
                break

        
    if player_win:
        points_blue=(game.beam[1])*3
        points_red=(game.beam[0])*2
        score=points_red+points_blue
        print("You won score",score)
    else:
        points_blue=(game.beam[1])*3
        points_red=(game.beam[0])*2
        score=points_red+points_blue
        print("computer won score", score)

