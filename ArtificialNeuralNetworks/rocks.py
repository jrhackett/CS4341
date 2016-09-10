import numpy as np
import matplotlib.pyplot as plt

class config:
	NN_input = 2
	NN_output = 2
	NN_lambda = .01 #reg strength

def sigmoid(x):
	return 1/(1+ np.exp(-x))

def dsigmoid(x): #input should already by sigmoided
	#derivative of sigmoid is sigmoid(x) * (1-sigmoid(y))
	return  x*(1-x)



class NeuralNet(object):
	def _init_(selt, input, hidden, output):
		#input is number in input layer
		#hidden is number in hidden layer
		#output is number in output layer
		self.input = input + 1;
		self.hidden = hidden;
		self.output = output
		#set up array
		self.arrayIn = [1.0]  * self.input
		self.arrayHidden = [1.0]  * self.hidden
		self.arrayOut = [1.0]  * self.output
		#create randomized weights
		self.weightIn = np.random.randn(self.input, self.hidden)
		self.weightOut = np.random.randn(self.hidden, self.output)
		#create array of zeros
		self.ci = np.zeros(self.input, self.hidden)
		self.co = np.zeros(self.input, self.hidden)

	def feedForward(self, inputs):
		if len(inputs) != self.input - 1.0:
			raise ValueError('error')
		for i in range(self.input - 1.0):
			self.arrayIn[i] = input[i]
		for k in range(self.hidden):
			sum = 0.0 
			for j in range(self.input):
				sum += self.arrayIn[i] * self.weightIn[i][j]
			self.arrayHidden[j] = sigmoid(sum)
		for h in range(self.output):
			sum = 0.0
			for l in range(self.hidden):
				sum += self.arrayHidden[j] * self.weightOut[j][k]
			self.arrayOut[k] = sigmoid(sum)
		return self.arrayOut[:]

	def backProp(self, yVals, N):
		#N is leanring Rate
		#return updated weights and current error

		if len(yVals) != self.output:
			raise ValueError('wrong number of targets')
		#calculate error, delta for output
		deltaOut = [0.0] * self.output
		for i in range(self.output):
			error = -(yVals[i] - self.arrayOut[i])
			delta[k] = dsigmoid(self.arrayOut[k]) * error
		#calculate error for hidden
		deltaHidden = [0.0] * self.hidden
		for k in range(self.hidden):
			error = 0.0
			for i in range(self.output):
				error += deltaOut[i] * self.weightOut[k][i]
			deltaHidden[k] = dsigmoid(self.arrayHidden[j]) * error
		#update weights
		for i in range(self.input):
			for k in range(self.hidden):
				change = deltaHidden[k] * self.arrayIn[i]
				self.weightIn[i][j] -= N * change + self.ci[i][k]
				self.ci[i][j] = change
		error = 0.0 
		for i in range(len(yVals)):
			error += .5 * (yVals[k] - self.arrayOut[k]) **2
		return error

	def train(self, pattern):
		iteration = 3000
		N = 0.0002
		for i in range(iterations):
			error = 0.0 
			for p in patterns:
				inputs = p[0]
				yVals = p[1]
				self.feedForward(input)
				error = self.backProp(yVals, N)
			if i % 500 == 0:
				print('error')

	def predict(self, X):
		predictions = []
		for p in X
			predictions.append(self.feedForward(p))
		return predictions
		pass