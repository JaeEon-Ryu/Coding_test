import java.util.*;

public class pre_test1차_java {

	static int size;
	static List isExplored = new ArrayList();
	static List sizeOfArea = new ArrayList();
	
	private static void solution(int sizeOfMatrix, int[][] matrix) {
	    // TODO: 이곳에 코드를 작성하세요.
		
		for(int i=0; i<matrix.length; i++) {
			for(int j=0; j<matrix[i].length; j++) {
				if (matrix[i][j] == 1) {
					if (!isExplored.contains(Integer.toString(i) + Integer.toString(j))){
						size = 1;
		                isExplored.add(Integer.toString(i) + Integer.toString(j));
		                findInFourDirection(matrix, i, j);
		                sizeOfArea.add(Integer.toString(size));
					}
				}
			}
		}
		if(sizeOfArea.size()>0) {
			
			Collections.sort(sizeOfArea);
			System.out.println(sizeOfArea.size());
		    String area_str = String.join(" ", sizeOfArea);
		    System.out.println(area_str);
		    
		}
		   
		else{
			System.out.println(0);
		}
	}
	
	private static void findInFourDirection(int[][] matrix, int r, int c) {
		
		int rSize = matrix.length;
		int cSize = matrix[0].length;
		
		if (rSize > r+1) {
			if (matrix[r+1][c] == 1) {
				if (!isExplored.contains(Integer.toString(r+1) + Integer.toString(c))) {
	                isExplored.add(Integer.toString(r+1) + Integer.toString(c));
	                size += 1;
	                findInFourDirection(matrix, r+1, c);
				}
			}
		}
		
		
		if(r-1>0) {
			if (matrix[r-1][c] == 1) {
				if (!isExplored.contains(Integer.toString(r-1) + Integer.toString(c))) {
	                isExplored.add(Integer.toString(r-1) + Integer.toString(c));
	                size += 1;
	                findInFourDirection(matrix, r-1, c);
				}
			}
		}
		
		if(cSize > c+1) {
			if (matrix[r][c+1] == 1) {
				if (!isExplored.contains(Integer.toString(r) + Integer.toString(c+1))) {
	                isExplored.add(Integer.toString(r) + Integer.toString(c+1));
	                size += 1;
	                findInFourDirection(matrix, r, c+1);
				}
			}
		} 
		
		
		if (c-1>0) {
			if (matrix[r][c-1] == 1) {
				if (!isExplored.contains(Integer.toString(r) + Integer.toString(c-1))) {
	                isExplored.add(Integer.toString(r) + Integer.toString(c-1));
	                size += 1;
	                findInFourDirection(matrix, r, c-1);
				}
			}
		}
			
		
	}
	  
	private static class InputData {
		int sizeOfMatrix;
		int[][] matrix;
	}
	
	public static void main(String[] args) throws Exception {
	    InputData inputData = processStdin();

	    solution(inputData.sizeOfMatrix, inputData.matrix);
	  }
	
	private static InputData processStdin() {
	    InputData inputData = new InputData();

	    try (Scanner scanner = new Scanner(System.in)) {
	      inputData.sizeOfMatrix = Integer.parseInt(scanner.nextLine().replaceAll("\\s+", ""));      
	      inputData.matrix = new int[inputData.sizeOfMatrix][inputData.sizeOfMatrix];
	      
	      for (int i = 0; i < inputData.sizeOfMatrix; i++) {
	        String[] buf = scanner.nextLine().trim().replaceAll("\\s+", " ").split(" ");
	        for (int j = 0; j < inputData.sizeOfMatrix; j++) {
	          inputData.matrix[i][j] = Integer.parseInt(buf[j]);
	        }
	      }
	    } catch (Exception e) {
	      throw e;
	    }

	    return inputData;
	  }


}
