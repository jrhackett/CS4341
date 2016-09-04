
public class OurPlayer extends Player {

	public OurPlayer(String n, int t, int l)
	{
		super(n, t, l);
	}


	public Move getMove(StateTree state) {
		//using custom state so we have better methods available to us, initializing using the RefereeBoard
		OurStateTree betterState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state.parent);

		//get the best move
		int move = minimax(betterState, 0, -1000000, 1000000);
		
		System.out.println("move: " + move);
		
		for(OurStateTree s : betterState.childrenStates) {
			System.out.println(s.bestValue + " col: " + s.startingMove.column);
		}
		
		for(OurStateTree s : betterState.childrenStates) {
			if(s.bestValue == move) {
				return s.startingMove;
			}
		}
		
		return new Move(false, -1);
	}

	private int minimax(OurStateTree state, int depth, int alpha, int beta) {
		
		if(depth == 7) {
			state.bestValue = this.eval(state);
			return state.bestValue;
		}
		
		state.initChildren();
		
		if(state.turn == 1) {
			for(OurStateTree s : state.childrenStates) {
				int current = minimax(s, depth + 1, alpha, beta);
//				System.out.println("Comparing: " + state.bestValue + " " + current + " " + state.turn);
				if(current > state.bestValue) {
//					System.out.println("I changed: " + state.bestValue + " " + current);
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
//					System.out.println("I changed: " + state.bestValue + " " + current);
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

	private int eval(OurStateTree state) {
		int heur = 0;
		for(int i = 0; i < state.winNumber; i++){
			int numCon = 0;
			numCon = checkConnect(state, i);
			heur += (numCon * i);
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