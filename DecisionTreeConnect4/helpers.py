# Jacob Hackett
# CS4341 A16 Project 3

import csv, math
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

# calculates entropy based on p and q
def entropy(p):
   return -p * math.log(p, 2) - (1 - p) * math.log((1 - p), 2)
