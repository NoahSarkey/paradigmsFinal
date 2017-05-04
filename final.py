#!/usr/bin/env python3

# Sam Mustipher, Noah Sarkey
# Programming Paradigms Final Project
# May 10, 2017

import pygame

# Global Variables
turn = 1

#############################################################








#############################################################

def endGameScreen(self, winner):
	# this function will end the game and leave the screen up with the end game being shown

#############################################################

# Game AI which determines whether or not someone has won (needs to be determined how we will make use of the variables)
def checkWin(self, board):
	# Checks Column
	i = 0
	j = 0
	while j < 3:
		kill = 0
		sum = 0
		while i < 3:
			if board[i][j] == 0:
				kill = 1
			sum = sum + board[i][j]
			i = i + 1
		if kill == 0 and (sum == 3 or sum == 6):
			if sum == 3:
				print("Player 1 WIN!")
				return 1
			else:
				print("Player 2 WIN!")
				return 2
		j = j + 1
	# Checks Row
	i = 0
	j = 0
	while i < 3:
		kill = 0
		sum = 0
		while j < 3:
			if board[i][j] == 0:
				kill = 1
			sum = sum + board[i][j]
			j = j + 1
		if kill == 0 and (sum == 3 or sum == 6):
			if sum == 3:
				print("Player 1 WIN!")
				return 1
			else:
				print("Player 2 WIN!")
				return 2
		i = i + 1
	# Check Diagonals (Top left to bottom right)
	kill = 0
	k = 0
	while k < 3:
		sum = 0
		if board[k][k] == 0:
			kill = 1
		sum = sum + board[k][k]
		k = k + 1
		if kill == 0 and (sum == 3 or sum == 6):
			if sum == 3:
				print("Player 1 WIN!")
				return 1
			else:
				print("Player 2 WIN!")
				return 2
	# Check Diagonals (Bottom left to top right)
	k = 2
	kill = 0
	while k >= 0:
		sum = 0
		if board[k][k] == 0:
			kill = 1
		sum = sum + board[k][k]
		k = k - 1
		if kill == 0 and (sum == 3 or sum == 6):
			if sum == 3:
				print("Player 1 WIN!")
				return 1
			else:
				print("Player 2 WIN!")
				return 2
	return 0	# nobody has won yet

################################################################

def boardChecking(self, player, row, column):
	# Check if the desired spot on the board is filled
	if board[row - 1][column - 1] == 0:
		board[row - 1][column - 1] = player
	else:
		print("INVALID ENTRY PICK AGAIN!")

	# Take care of determining whose turn it is
	global turn
	if turn == 1:
		turn = 2
	else:
		turn = 1

################################################################

# The main playing space for the final game
def Game(self):
	pygame.init()
	winner = 0


	# keep running the gamer until we have a winner
	while !winner:
		arr = boardChecking()
		winner = checkWin()
		pygame.display.update()


	# provide the user with the end game screen
	endGameScreen(winner)

################################################################

if __name__ == "__main__":
	Game()
