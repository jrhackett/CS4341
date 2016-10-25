# Bayes Networks Option B

This program constructs a Bayesian Network based on an input file describing nodes,
their parents, and their CPT. It also takes in the status of each node and uses
rejection sampling and likelihood weighting sampling to calculate the probability
associated with the query node. Note that this program fulfills the requirements
of option B.


## Installation & Usage

This program expects you have Python 2.7. Please do not try to run this program 
on Python 3 or newer. This program also uses the standard Python Random library. 
You can simply run the following command to run the program:

python main.py <nodesFile.txt> <queryFile.txt> <number of samples>


## Output

Output for this project will be in the format:
rejection sampling value: 0.217
likelihood weighting sampling value: 0.1300445

where the numbers will change depending on the network and the number of samples.

## Credits

Jacob Hackett

Russell and Norvig for pseudocode on the algorithms used in this program
