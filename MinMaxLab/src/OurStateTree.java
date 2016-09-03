import java.util.ArrayList;

public class OurStateTree extends StateTree implements Cloneable {
	
	public OurStateTree(int r, int c, int w, int t, boolean p1, boolean p2, StateTree p) {
		super(r, c, w, t, p1, p2, p);
	}
	
	//returns an ArrayList of all valid moves on the board, does not include pops right now
	public ArrayList<Move> getMoves() {
		ArrayList<Move> moves = new ArrayList<Move>();
		for(int i = 0; i < this.columns; i++) {
			for(int j = this.rows - 1; j > 0; j--) {
				if(this.boardMatrix[j][i] == 0) {
					moves.add(new Move(false, i));
					break;
				}
			}
		}
		return moves;
	}
	
	public ArrayList<OurStateTree> generateChildStates() {
		ArrayList<OurStateTree> states = new ArrayList<OurStateTree>();
		for(Move m : this.getMoves()) {
			OurStateTree newState = OurStateTree.copy(this);
			newState.makeMove(m);
			states.add(newState);
		}
		return states;
	}
	
	public static OurStateTree copy(OurStateTree state) {
		OurStateTree newState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state.parent);
		for(int i = 0; i < newState.rows; i++) {
			for(int j = 0; j < newState.columns; j++) {
				newState.boardMatrix[i][j] = state.boardMatrix[i][j];
			}
		}
		return newState;
	}
}
