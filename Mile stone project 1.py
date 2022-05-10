from dataclasses import replace
from turtle import position


def select_position(boar,marker,position):
    position = int(input('Choose any number from 1-9: '))
    while position not in range(1-9):
        position = int(input('Choose any number from 1-9: '))
    if position in range(1-9):
    board[position] = marker

def player_win():
    possible_1 = board[7] == board[8] == board[9]
    possible_2 = board[4] == board[5] == board[6]
    possible_3 = board[1] == board[2] == board[3]
    possible_4 = board[7] == board[4] == board[1]
    possible_5 = board[8] == board[5] == board[2]
    possible_6 = board[9] == board[6] == board[3]
    possible_7 = board[1] == board[5] == board[9]
    possible_8 = board[7] == board[5] == board[3]
    while (possible_1 == True or possible_2 == True or possible_3 == True or possible_4 = True or possible_5 == True or possible_6 == True or possible_7 == True or possible_8 == True):
        print('player win')
    if (possible_1 == False and possible_2 == False and possible_3 == False and possible_4 = False and possible_5 == False and possible_6 == False and possible_7 == False and possible_8 == False):
        print('match draw')
    elif:
        return player_input
