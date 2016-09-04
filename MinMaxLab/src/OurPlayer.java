
public class OurPlayer extends Player {

	public OurPlayer(String n, int t, int l)
	{
		super(n, t, l);
	}


	public Move getMove(StateTree state) {
		OurStateTree betterState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state.parent);
		
		//get the best move
		int move = minimax(betterState, 0, -1000000, 1000000);
		
		for(OurStateTree s : betterState.childrenStates) {
			System.out.println(s.bestValue + " col: " + s.startingMove.column);
		}
		
		for(OurStateTree s : betterState.childrenStates) {
			if(s.bestValue == move && !betterState.checkFullColumn(s.startingMove.column)) {
				return s.startingMove;
			}
		}
		
		return new Move(false, -1);
	}

	private int minimax(OurStateTree state, int depth, int alpha, int beta) {
		
		if(depth == 5) {
			state.bestValue = state.eval();
			return state.bestValue;
		}
		
		state.initChildren();
		
		if(state.turn == 1) {
			for(OurStateTree s : state.childrenStates) {
				int current = minimax(s, depth + 1, alpha, beta);
//				System.out.println("Comparing: " + state.bestValue + " " + current + " " + state.turn);
				if(current > state.bestValue) {
//					System.out.println("I changed: " + state.bestValue + " to " + current + " at: " + depth + " move: " + s.startingMove.column);
					state.bestValue = current;
				}
//				if(current > alpha) {
//					alpha = current;
//				}
//				
//				if(alpha >= beta) {
//					break;
//				}
			}
			return state.bestValue;
		}
		
		else {
			for(OurStateTree s : state.childrenStates) {
				int current = minimax(s, depth + 1, alpha, beta);

//				System.out.println("Comparing: " + state.bestValue + " " + current + " " + state.turn);
				if(current < state.bestValue) {
//					System.out.println("I changed: " + state.bestValue + " to " + current + " at: " + depth);
					state.bestValue = current;
				}			
//				if(current < beta) {
//					beta = current;
//				}
//				
//				if(beta <= alpha) {
//					break;
//				}
			}
			return state.bestValue;
		}
	}

}