
import csv
import numpy as np
from board import Board

def readData(inputFile):
	boardStates = []
	with open(inputFile, "rb") as f:
		reader = csv.reader(f, delimiter='\t')
		for row in reader:
			l = list(row)
			w = l.pop()
			m = np.mat(l)
			boardStates.append(Board(l, w))
	return boardStates
