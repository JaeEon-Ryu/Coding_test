
public class Lv1_자연수_뒤집어_배열로_만들기 {

	public Lv1_자연수_뒤집어_배열로_만들기() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int length = Long.toString(n).length();
        int[] answer = new int[length];
        int index = 0;
        
        while(n > 0){
            answer[index] = (int)(n%10);
            
            n /= 10;
            index ++;
        }
        
        System.out.println(answer);
        return answer;
	}

}
