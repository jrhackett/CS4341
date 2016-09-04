import java.util.ArrayList;




public class OurPlayer extends Player {

	public OurPlayer(String n, int t, int l)
	{
		super(n, t, l);
	}


	public Move getMove(StateTree state) {
		System.out.println("Hi");
		//using custom state so we have better methods available to us, initializing using the RefereeBoard
		OurStateTree betterState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state.parent);

		//get the best move
		Move move = new Move(false, minimax2(betterState, Integer.MIN_VALUE, betterState.columns, 1));

		//return Move to the Referee
		return move;
	}


	private int minimax2(OurStateTree state, int alpha, int depth, int t){
		int bestCol = 0;
		int bestVal = alpha;
		int player = t == 1 ? 2 : 1;
		
		if(OurStateTree.checkForWinner(state) != 0) {
			if(player == 1) {
				bestVal = Integer.MAX_VALUE - depth;
			}
			else {
				bestVal = Integer.MIN_VALUE + depth;
			}
		}
		else if(OurStateTree.checkFull(state)) {
			bestVal = 0;
		}
		else if(depth == 0) {
			int m = this.eval(state);
			bestVal = m == 0 ? m : m - depth;
		}
		else {
			ArrayList<OurStateTree> newStates = state.generateChildStates();
			if(depth > 0) {
				for(OurStateTree newState : newStates) {
					int a = minimax2(newState, Integer.MIN_VALUE, depth - 1, player);
					if(a > bestVal) {
						bestCol = newState.newCol;
						bestVal = a;
					}
				}
			}
		}
		
		if(depth == 0) {
			return bestCol;
		}
		else {
			return bestVal;
		}
	}

	private int eval(OurStateTree state) {
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
