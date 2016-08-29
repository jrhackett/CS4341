
public class OurMove extends Move {

	int score;
	
	//OurMove also includes a score
	public OurMove(boolean p, int c, int s) {
		super(p, c);
		this.score = s;
	}
}
