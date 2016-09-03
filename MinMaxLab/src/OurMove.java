
public class OurMove extends Move {

	int score;
	
	//OurMove also includes a score
	public OurMove(boolean p, int c, int s) {
		super(p, c);
		this.score = s;
	}
	
	public String toString() {
		return "Pop: " + this.pop + " Col: " + this.column + " Score: " + this.score;
	}
}
