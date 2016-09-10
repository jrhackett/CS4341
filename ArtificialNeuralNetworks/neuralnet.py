
import numpy as np
import random


def sigmoid(x):
	return 1/(1+ np.exp(-x))

def dsigmoid(x): #input should already by sigmoided
	#derivative of sigmoid is sigmoid(x) * (1-sigmoid(y))
	return  x*(1-x)

class NeuralNet:

	def __init__(self, input, hidden, output, iterations, learning, momentum, decay):
		
		# initializing some variables to be used later
		self.iterations = iterations
		self.learning = learning
		self.momentum = momentum
		self.decay = decay

		#input is number in input layer
		#hidden is number in hidden layer
		#output is number in output layer
		self.input = input + 1
		self.hidden = hidden
		self.output = output
		#set up array
		self.arrayIn = [1.0]  * self.input
		self.arrayHidden = [1.0]  * self.hidden
		self.arrayOut = [1.0]  * self.output
		#create randomized weights to be updated -- we want them to be bad estimates first round through
		self.weightIn = np.random.randn(self.input, self.hidden)
		self.weightOut = np.random.randn(self.hidden, self.output)
		#create array of zeros
		self.ci = np.zeros((self.input, self.hidden))
		self.co = np.zeros((self.input, self.hidden))

	# sums the outputs of each layer so we can figure out the error and adjust weights in backprop
	def feedForward(self, inputs):
		# error check to prevent incorrect input
		if len(inputs) != self.input - 1:
			raise ValueError('error')

		#activate input layer
		for i in range(self.input - 1):
			self.arrayIn[i] = inputs[i]

		#activate hidden layer
		for i in range(self.hidden):
			sum = 0.0 
			for j in range(self.input):
				sum += float(self.arrayIn[j]) * float(self.weightIn[j][i])
			self.arrayHidden[i] = sigmoid(sum)

		# activate output layer
		for i in range(self.output):
			sum = 0.0
			for j in range(self.hidden):
				sum += self.arrayHidden[j] * self.weightOut[j][i]
			self.arrayOut[i] = sigmoid(sum)

		return self.arrayOut[:]

	# calculates the errors between our desired output and the output we received
	# uses sigmoid to figure out how much we need to change the weights
	# updates the weights between every node to compensate for this error
	def backProp(self, target):
		#return updated weights and current error

		# error checks
		if len(target) != self.output:
			raise ValueError('Wrong number of targets')

		# calculate error for output nodes
		deltaOut = [0.0] * self.output
		for i in range(self.output):
			error = -(float(target[i]) - float(self.arrayOut[i]))
			deltaOut[i] = dsigmoid(self.arrayOut[i]) * error

		# calculate error for hidden nodes
		deltaHidden = [0.0] * self.hidden
		for i in range(self.hidden):
			error = 0.0
			for j in range(self.output):
				error += deltaOut[j] * self.weightOut[i][j]
			deltaHidden[i] = dsigmoid(self.arrayHidden[i]) * error

		# update weights based on the error from above
		for i in range(self.input):
			for j in range(self.hidden):
				change = deltaHidden[j] * self.arrayIn[i]
				self.weightIn[i][j] -= float(self.learning) * float(change) + float(self.ci[i][j]) * float(self.momentum)
				self.ci[i][j] = change

		# calculate error
		error = 0.0 
		for i in range(len(target)):
			error += 0.5 * (target[i] - self.arrayOut[i]) ** 2
		return error

	def round(self, n):
		if n[0] >= 0.5:
			return 1
		elif n[0] < 0.5:
			return 0

	# train the neural network
	def train(self, pattern):
		print 'Starting Training'
		print 'Errors shown below:'
		for i in range(self.iterations):
			error = 0.0 
			# shuffle the pattern for randomness
			random.shuffle(pattern)
			# feed forward and backProp all of our data
			for p in pattern:
				inputs = p[0]
				target = p[1]
				self.feedForward(inputs)
				error += self.backProp(target)
			#printing errors to stdout
			print 'error %-.5f' % error
			#update learning rate due to decay
			self.learning = self.learning * (self.learning / (self.learning + (self.learning * self.decay)))

	def test(self, pattern):
		print 'Starting Testing'
		print 'True value -> Rounded Prediction from Unrounded Prediction'
		total = 0.0
		correct = 0.0
		for p in pattern:
			prediction = self.feedForward(p[0])
			rounded = self.round(prediction)
			print int(p[1][0]), '->', rounded, 'from', prediction
			if(int(p[1][0]) == rounded):
				correct += 1.0
			total += 1.0
		print 'Percent correct:', (correct / total) * 100

	# generate predictions for any set of input data
	def predict(self, data):
		predictions = []
		for p in data:
			predictions.append(self.round(self.feedForward(p)))
		return predictions	