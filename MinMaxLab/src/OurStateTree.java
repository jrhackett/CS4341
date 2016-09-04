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
			newState.startingMove = m;
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
	
	public int eval() {
		int heur = 0;
		for(int i = 1; i <= this.winNumber; i++){
			int numCon = 0;
			numCon = checkConnect(this, i);
			heur += (numCon * i);
		}
		return heur;	
	}

	// This counts how many n-in-a-rows each player has
	public static int checkConnect(StateTree board, int n)
	{
		int winner = 0;
		int[] count = new int[4];
		int winTotal = 0;
		for(int i=0; i<board.rows; i++)
		{
			for(int j=0; j<board.columns; j++)
			{
				if(board.boardMatrix[i][j] == 0)
				{
					winner = 0;
					for(int x=0; x<4; x++)
					{
						count[x] = 0;
					}
				}
				else
				{
					winner = board.boardMatrix[i][j];
					for(int x=0; x<n; x++)
					{
						if((j+x < board.columns) && (board.boardMatrix[i][j+x] == winner))
							count[0]++;
						else
							count[0] = 0;
						if((i+x < board.rows) && (board.boardMatrix[i+x][j] == winner))
							count[1]++;
						else
							count[1] = 0;
						if((i+x < board.rows) && (j+x < board.columns) && (board.boardMatrix[i+x][j+x] == winner))
							count[2]++;
						else
							count[2] = 0;
						if((i-x >= 0) && (j+x < board.columns) && (board.boardMatrix[i-x][j+x] == winner))
							count[3]++;
						else
							count[3] = 0;
					}
				}
				for(int x=0; x<4; x++)
				{
					if(count[x] == n)
					{
						if(winner == 1)
							winTotal++;
						else if(winner == 2)
							winTotal--;
					}
					count[x] = 0;
				}
				winner = 0;
			}
		}
		return winTotal;
	}
	
	public boolean checkFullColumn(int n) {
		if(this.boardMatrix[0][n] != 0) {
			return true;
		}
		return false;
	}
}