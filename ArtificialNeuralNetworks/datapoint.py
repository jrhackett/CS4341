
class DataPoint:
	def __init__(self, x, y, label):
		self.x = x
		self.y = y
		self.label = label

	def __str__(self):
		return self.x + " " + self.y + " " + self.label

	def __repr__(self):
		return self.x + " " + self.y + " " + self.label

	def __getitem__(self, index):
		if index == 0:
			return [self.x, self.y]
		elif index == 1:
			return [self.label]
