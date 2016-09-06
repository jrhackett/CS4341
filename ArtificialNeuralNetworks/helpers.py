from datapoint import DataPoint

def readData(file):
	a = []
	with open(file, 'r') as f:
		for line in f:
			l = line.split()
			a.append(DataPoint(l[0], l[1], l[2]))
	return a
