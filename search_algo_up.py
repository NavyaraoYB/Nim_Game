#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 18:32:14 2023

@author: shyam
"""

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


# def next_move(state):
#     n_visits = set()
#     resist = []
    
#     for i in range(len(state)):
#         for m in range(1, state[i] + 1):
#             temp_val_move = list(state[:])
#             temp_val_move[i] -= m
#             new_order = tuple(sorted(temp_val_move))
#             if new_order not in n_visits:
#                 resist.append(temp_val_move)
#                 n_visits.add(new_order)  
#     return resist


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
