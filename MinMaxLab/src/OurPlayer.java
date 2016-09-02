import java.util.ArrayList;




public class OurPlayer extends Player {

	private Referee referee;

	public OurPlayer(String n, int t, int l)
	{
		super(n, t, l);
	}


	public Move getMove(StateTree state) {

		//using custom state so we have better methods available to us, initializing using the RefereeBoard
		OurStateTree betterState = new OurStateTree(state.rows, state.columns, state.winNumber, state.turn, state.pop1, state.pop2, state.parent);

		//get the best move
		OurMove move = minimax(betterState, betterState.columns, this.turn);

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
			bestScore = eval(state);
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
