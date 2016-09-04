import java.util.ArrayList;

public class OurStateTree extends StateTree implements Cloneable {
	
	Move startingMove;
	int bestValue;
	ArrayList<OurStateTree> childrenStates;
	
	public OurStateTree(int r, int c, int w, int t, boolean p1, boolean p2, StateTree p) {
		super(r, c, w, t, p1, p2, p);
		startingMove = new Move(false, -1);
		childrenStates = new ArrayList<OurStateTree>();
		bestValue = t == 1 ? -1000000 : 1000000;
	}
	
	//returns an ArrayList of all valid moves on the board, does not include pops right now
	public ArrayList<Move> getMoves() {
		ArrayList<Move> moves = new ArrayList<Move>();
		for(int i = 0; i < this.columns; i++) {
			for(int j = this.rows - 1; j > 0; j--) {
				if(this.boardMatrix[j][i] == 0) {
					moves.add(new Move(false, i)); 
//					System.out.println("adding move col: " + i);
					break;
				}
			}
		}
		
		//this will add in pops to our list of available moves. however, our minimax is not ready for it yet
 		if(this.turn == 1) {
 			if(this.pop1 == false) {
 				moves.addAll(this.getPopMoves());
 			}
 		}
 		else {
 			if(this.pop2 == false) {
 				moves.addAll(this.getPopMoves());
 			}
 		}
		return moves;
	}
	
	//helper for getting pop moves, need to edit minimax so this can work
 	private ArrayList<Move> getPopMoves() {
 		ArrayList<Move> moves = new ArrayList<Move>();
 		for(int i = 0; i < this.columns; i++) {
 			if(this.boardMatrix[this.rows - 1][i] == this.turn) {
 				moves.add(new Move(true, i));
 			}
 		}
 		return moves;
 	}
	
	public void initChildren() {
		this.childrenStates = generateChildStates();
	}
	
	public ArrayList<OurStateTree> generateChildStates() {
		ArrayList<OurStateTree> states = new ArrayList<OurStateTree>();
		for(Move m : this.getMoves()) {
			OurStateTree newState = OurStateTree.copy(this);
			newState.makeMove(m);
			newState.bestValue = newState.turn == 1 ? -1000000 : 1000000;
			startingMove = m;
			states.add(newState);
		}
		return states;
	}
	
	public static OurStateTree copy(OurStateTree state) {
		OurStateTree newState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state);
		for(int i = 0; i < newState.rows; i++) {
			for(int j = 0; j < newState.columns; j++) {
				newState.boardMatrix[i][j] = state.boardMatrix[i][j];
			}
		}
		return newState;
	}
	
	public boolean checkFullColumn(int col) {
		for(int i = 0; i < this.columns; i++) {
			if(this.boardMatrix[i][col] == 0) {
				return true;
			}
		}
		return false;
	}
}