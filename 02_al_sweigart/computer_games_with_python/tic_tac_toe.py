# from https://inventwithpython.com/invent4thed/chapter10.html

# Date written: 2.19.2025
import random

def drawBoard(board):
	# This function prints out the board that it was passed
	# board is a list of 10 strings representing the board
	# ignore index 0

	print(board[7] + '|' + board[8] + '|' + board[9])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[9])
