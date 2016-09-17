
import csv
import numpy as np
from board import Board

def readData(inputFile):
	boardStates = []
	with open(inputFile, "rb") as f:
		reader = csv.reader(f, delimiter='\t')
		lineNumber = 0
		for row in f:
			if lineNumber == 0:
				lineNumber += 1
			else:
				l = row.split(',')
				state = []
				for i in l:
					state.append(int(i))
				boardStates.append(state)
	return boardStates

# returns which player owns the bottom left piece in the board
# first required feature
def getFeature1(board):
	return board[0]

# returns which player has more pieces in the center 2 rows of the board
# second required feature
def getFeature2(board):
	count = 0
	for i in range(0, 42):
		if(i % 6 == 2 or i % 6 == 3):
			if(board[i] == 1):
				count += 1
			elif(board[i] == 2):
				count -= 1
	return decision(count)


# returns which player has more pieces in the center 3 columns of the board
def getFeature3(board):
	count = 0
	for i in range(12, 29):
		if(board[i] == 1):
			count += 1
		elif(board[i] == 2):
			count -= 1
	return decision(count)

# returns which player has the most pieces on the top of the columns
def getFeature4(board):
	count = 0
	for i in range(0, 7):
		for j in range(0, 6):
			index = 6 * i + j
			if(board[index] == 0):
				if(j == 0):
					break
				else:
					if(board[index - 1] == 1):
						count += 1
					elif(board[index - 1] == 2):
						count -= 1
	return decision(count)

# returns which player has the better position based on the piece's manhattan distance 
# to the center of the board (the bottom center piece -- index 20, as there are two center pieces)
def getFeature5(board):
	count = 0
	for i in range(0, 7): # 3
		for j in range(0, 6): # 2
			index = 6 * i + j
			if(board[index] == 1):
				count += abs(i - 3) + abs(j - 2)
			elif(board[index] == 2):
				count -= abs(i - 3) + abs(j - 2)
	return decision(count)

# returns which player is predicted to win based on the count
def decision(count):
	if(count > 0):
		return 1
	elif(count < 0):
		return 2
	else:
		return 0

