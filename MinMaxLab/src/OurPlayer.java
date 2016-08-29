import java.util.ArrayList;

public class OurPlayer extends Player {

	public OurPlayer(String n, int t, int l)
	{
		super(n, t, l);
	}
	
	
	public Move getMove(StateTree state) {
		
		//using custom state so we have better methods available to us, initializing using the RefereeBoard
		OurStateTree betterState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state.parent);
		
		//get the best move
		OurMove move = minimax(betterState, 2, this.turn);
		
		//return Move to the Referee
		return new Move(move.pop, move.column);
	}
	
	private OurMove minimax(OurStateTree state, int depth, int t) {
			
		//variable declaration for best score, move, and column
		int bestScore = t % 2 == 0 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
		OurMove bestMove = new OurMove(false, -1, 0);
		int bestCol = -1;
		
		//variable to store which player has the next turn so we can swap between minimizing and maximizing nodes
		int next = t % 2 == 0 ? 1 : 2;
		
		//an arraylist of all valid moves (right now it doesn't include pops)
		ArrayList<Move> moves = state.getMoves();
		
		//current score and move variables
		int score = 0;
		OurMove thisMove = new OurMove(false, -1, 0);
		
		//if we have no more moves or have reached the depth, eval the score
		if(moves.isEmpty() || depth == 0) {
			bestScore = eval();
		}
		else {
			//go through all valid moves
			for(Move move : moves) {
				//get move and score of next players move recursively
				thisMove = minimax(state, depth - 1, next);
				score = thisMove.score;
				//if maximizing and this score is better, store values
				if(t == 1 && score > bestScore) {
					bestMove = thisMove;
					bestScore = score;
					bestCol = thisMove.column;
				}
				//if minimizing and this score is better, store values
				else if(t == 2 && score < bestScore) {
					bestMove = thisMove;
					bestScore = score;
					bestCol = thisMove.column;
				}
			}
		}
		//return our move
		return new OurMove(false, bestCol, bestScore);	//TODO fix pop
	}
	
	private int eval() {
		return 0;	//TODO fix this
	}

}
