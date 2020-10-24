import java.util.*;

public class Solution {

	
	private static void solution(int numOfAllPlayers, int numOfQuickPlayers, char[] namesOfQuickPlayers, int numOfGames, int[] numOfMovesPerGame){
	    // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
		ArrayList nameOfPlayer = new ArrayList();
		ArrayList numOfCatched = new ArrayList();
		int i;
		
		for(i=0; i<numOfAllPlayers; i++) {
			nameOfPlayer.add((char)('A' + (char)i));
			numOfCatched.add(0);
		}
		
		char tagger = (char)nameOfPlayer.remove(0);
		int taggerNum = (int)numOfCatched.remove(0);
		taggerNum++;
		
		int idx = 0;
		for(i=0; i<numOfGames; i++) {
			idx += numOfMovesPerGame[i];
			boolean isChanged = true;
		
			
			while(!(idx>=0 && idx<nameOfPlayer.size())) {
				if(idx<0) {
					idx = nameOfPlayer.size() + idx ;
				
				}
		
				if(idx >= nameOfPlayer.size() ) {
				
					idx -= nameOfPlayer.size();
				}
			}
			
		
			for(int check=0; check<numOfQuickPlayers; check++) {
				if((char)nameOfPlayer.get(idx) == namesOfQuickPlayers[check]) {
					isChanged = false;
					break;
				}
			}
			
			if(isChanged) {
		
				nameOfPlayer.add(idx+1,tagger);
				numOfCatched.add(idx+1,taggerNum);
				
				tagger = (char)nameOfPlayer.remove(idx);
				taggerNum = (int)numOfCatched.remove(idx);
				taggerNum++;
			}
			else {
			
				taggerNum++;
			}
		}
		
		nameOfPlayer.add(tagger);
		numOfCatched.add(taggerNum);
		
		for(i=0; i<numOfAllPlayers; i++) {
			System.out.printf("%c %d\n",(char)nameOfPlayer.get(i),(int)numOfCatched.get(i));
		}
		
	  }

	
	private static class InputData {
	    int numOfAllPlayers;
	    int numOfQuickPlayers;
	    char[] namesOfQuickPlayers;
	    int numOfGames;
	    int[] numOfMovesPerGame;
	  }
	
	private static InputData processStdin() {
	    InputData inputData = new InputData();

	    try (Scanner scanner = new Scanner(System.in)) {
	      inputData.numOfAllPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));

	      inputData.numOfQuickPlayers = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
	      inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
	      System.arraycopy(scanner.nextLine().trim().replaceAll("\\s+", "").toCharArray(), 0, inputData.namesOfQuickPlayers, 0, inputData.numOfQuickPlayers);

	      inputData.numOfGames = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));
	      inputData.numOfMovesPerGame = new int[inputData.numOfGames];
	      String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
	      for(int i = 0; i < inputData.numOfGames ; i++){
	        inputData.numOfMovesPerGame[i] = Integer.parseInt(buf[i]);
	      }
	    } catch (Exception e) {
	      throw e;
	    }

	    return inputData;
	  }

	public static void main(String[] args) throws Exception {
	    InputData inputData = processStdin();

	    solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
	  }

}
