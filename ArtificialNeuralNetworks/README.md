# Artificial Neural Network

This is an artificial neural network written in Python. It trains on any data such that the 
data is in the format [inputArray] [outputArray] and that these arrays are of each length 
to the number of input nodes and output nodes.

## Requirements
Python 2.7.10
Numpy
sys
getopt
random

## Usage

python ann.py <inputFilePath> <numberOfHiddenNodes> <holdOutPercent>

## Results

Results of our several experiments can be seen in the results folder. These experiments are detailed
in the project writeup. We essentially ran tests and changed the holdout percent and number of hidden
nodes to observe the results that would have on the percent of correct predictions.

## Credits

Jacob Hackett
Trevor Rocks

We also references several resources to help understand Neural Networks. We would like to
give thanks and credits to the following sources. Neural Networks are not the easiest thing
to wrap our heads around and these sources helped a lot while making the complex topic seem
so simple.

https://www.youtube.com/watch?v=DG5-UyRBQD4
https://en.wikipedia.org/wiki/Backpropagation
https://en.wikipedia.org/wiki/Feedforward_neural_network
https://databoys.github.io/Feedforward/
http://www.solver.com/training-artificial-neural-network-intro
