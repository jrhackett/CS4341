
public class OurPlayer extends Player {

	//OurPlayer is just our implementation of the Player class
	public OurPlayer(String n, int t, int l) {
		super(n, t, l);
	}

	//getMove returns a Move to the Referee
	public Move getMove(StateTree state) {
		//make our betterState object
		OurStateTree betterState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state.parent, state.boardMatrix);

		//run minimax and get our int value
		int move = minimax(betterState, 0, -1000000, 1000000);
		
		//circle through this states direct children and see which one has the same value as what minimax just returned
		for(OurStateTree s : betterState.childrenStates) {
			if(s.bestValue == move) {
				return s.startingMove;
			}
		}
		//dumby move
		return new Move(false, -1);
	}

	//minimax is a recursive function that returns a bestValue int
	private int minimax(OurStateTree state, int depth, int alpha, int beta) {
		
		//if at arbitrary max depth, return the heuristic
		if(depth == 7) {
			return state.eval();
		}
		
		//initialize the children of the current state
		state.initChildren();
		
		//if maxing
		if(state.turn == 1) {
			//cycle through the children states
			for(OurStateTree s : state.childrenStates) {
				//run minimax with a depth + 1 
				int current = minimax(s, depth + 1, alpha, beta);
				//if minimax gave a better value than we've observed before, replace it
				if(current > state.bestValue) {
					state.bestValue = current;
				}
				//if minimax returned a better value than alpha has seen so far, replace alpha
				if(current > alpha) {
					alpha = current;
				}
				
				//beta cut off
				if(alpha >= beta) {
					break;
				}
			}
			//return this states best value
			return state.bestValue;
		}
		//if mining
		else {
			//cycle through the children states
			for(OurStateTree s : state.childrenStates) {
				//run minimax with a depth + 1
				int current = minimax(s, depth + 1, alpha, beta);
				//if minimax gave a better value than we've observed before, replace it
				if(current < state.bestValue) {
					state.bestValue = current;
				}	
				//if minimax returned a better value than beta has seen so far, replace beta
				if(current < beta) {
					beta = current;
				}
				//alpha cutoff
				if(beta <= alpha) {
					break;
				}
			}
			//return this states best value
			return state.bestValue;
		}
	}

}