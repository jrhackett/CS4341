import java.util.ArrayList;




public class OurPlayer extends Player {

	private Referee referee;

	public OurPlayer(String n, int t, int l)
	{
		super(n, t, l);
	}


	public Move getMove(StateTree state) {
		System.out.println("Hi");
		//using custom state so we have better methods available to us, initializing using the RefereeBoard
		OurStateTree betterState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state.parent);

		//get the best move
		OurMove move = minimax(betterState, betterState.columns, this.turn, -1, false, Integer.MIN_VALUE, Integer.MAX_VALUE);

		//return Move to the Referee
		return new Move(move.pop, move.column);
	}

	// minimax function with alpha beta pruning
	private OurMove minimax(OurStateTree state, int depth, int t, int col, boolean pop, int alpha, int beta) {
		
		//if we're at the end of our tree or the board is full, return the heuristic
		if(depth == 0 || state.getMoves().isEmpty()) {
			return new OurMove(pop, col, this.eval(state));
		}
		
		//get all children board states
		ArrayList<OurStateTree> childStates = state.generateChildStates();
		
		//if maximizing
		if(t == 1) {
			//init some values
			int bestValue = Integer.MIN_VALUE;
			//currently not using these two
			int bestCol = -1;
			boolean bestPop = false;
			
			//for every child state
			for(OurStateTree s : childStates) {
				//recurse through minimax with current state, one less depth, player2 turn, and current values for move and alpha/beta
				OurMove current = minimax(s, depth - 1, 2, col, pop, alpha, beta);
				//if that score is better, replace it
				if(current.score > bestValue) {
					bestValue = current.score;
					col = current.column;
					pop = current.pop;
				}
				System.out.println(col);
				
				//if current score is better than current alpha, replace it
				if(current.score > alpha) {
					alpha = current.score;
				}
				
				//beta cutoff
				if(alpha >= beta) {
					break;
				}
			}
			return new OurMove(pop, col, bestValue);
		}
		//else minimizing
		else {
			//init some values
			int bestValue = Integer.MAX_VALUE;
			//currently not using these two
			int bestCol = -1;
			boolean bestPop = false;
			
			//for every child state
			for(OurStateTree s : childStates) {
				//recurse through minimax with current state, one less depth, player2 turn, and current values for move and alpha/beta
				OurMove current = minimax(s, depth - 1, 1, col, pop, alpha, beta);
				//if this score is better than the best value, replace it
				if(current.score < bestValue) {
					bestValue = current.score;
					col = current.column;
					pop = current.pop;
				}
				
				//if this value is better than current beta, replace it
				if(current.score < beta) {
					beta = current.score;
				}
				
				//alpha cutoff
				if(beta <= alpha) {
					break;
				}
			}
			return new OurMove(pop, col, bestValue);
		}
	}

	private int eval(StateTree state) {
		int heur = 0;
		for(int i=0; i < state.winNumber; i++){
			int numCon = 0;
			numCon = checkConnect(state, i);
			heur = (numCon*10)^i;
		}
		return heur;	//TODO fix this
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



}
