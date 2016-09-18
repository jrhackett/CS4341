# CS4341 Project 3: Connect 4 Decision Trees

This program takes in a CSV file that describes board states of Connect 4. It then uses five
features, detailed in the writeup, to predict the winner of the game based on that heuristic.
It then creates a decision tree using these five features to try to better model the outcome 
of the game, based on the given state.

Note that I decided to do this entire project in one program, instead of two. This was said 
to be OK over a public Slack channel for the course. Note that the updated board states will
still be printed in the designated output file. The last five numbers represent the predictions
for which player will win the game from each feature.

## Usage

This program expects a couple things. It is able to run on Python 2.7.x. It should not be run
using Python 3, as there were a lot of changes in Python 3 and this code does not account for 
those. It also assumes a few things about the command line arguments. You can run the program 
like this through the terminal:

$ python main.py <inputFile.csv> <outputFile.csv> <holdout percent>

Note that the inputFile.csv and outputFile.csv both must be CSV files. Also, not that the
holdout percent must be a number between 0 and 1. This holdout percent determines how much 
of the data is left out for testing. For example, I could run the program like this:

$ python main.py input.csv output.csv 0.2

## Credits

Jacob Hackett
