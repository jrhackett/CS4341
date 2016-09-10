from datapoint import DataPoint

def readData(file):
	a = []
	with open(file, 'r') as f:
		for line in f:
			l = line.split()
			a.append(DataPoint(float(l[0]), float(l[1]), float(l[2])))
	return a
