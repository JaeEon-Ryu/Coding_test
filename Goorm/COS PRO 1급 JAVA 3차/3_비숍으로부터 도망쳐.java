
// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Main {
    public int solution(String[] bishops) {
        int answer = 0;
        int[][] grid = new int[8][8];
        for (int i = 0; i < bishops.length; i++) {
            int bishopX = ('8' - bishops[i].charAt(1));
            int bishopY = (bishops[i].charAt(0) - 'A');
            grid[bishopX][bishopY] = 1;
            makeRoute(bishopX, bishopY, grid);
        }

        answer = cntAnswer(grid);

        return answer;
    }

    // bishop 의 이동경로 표시
    public void makeRoute(int x, int y, int[][] arr) {
        int[] dx = { -1, 1, -1, 1 };
        int[] dy = { -1, -1, 1, 1 };
        int dir = 0;

        int newX = x;
        int newY = y;
        while (dir < 4) {
            newX += dx[dir];
            newY += dy[dir];

            if ((0 <= newX && newX < 8) && (0 <= newY && newY < 8)) {
                arr[newX][newY] = 1;
            } else {
                newX = x;
                newY = y;
                dir++;
            }
        }
    }

    // bishop으로부터 안전한 칸 세기
    public int cntAnswer(int[][] arr) {
        int result = 0;

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (arr[i][j] == 0)
                    result++;
            }
        }

        return result;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Main sol = new Main();
        String[] bishops1 = { new String("D5") };
        int ret1 = sol.solution(bishops1);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret1 + " 입니다.");

        String[] bishops2 = { new String("D5"), new String("E8"), new String("G2") };
        int ret2 = sol.solution(bishops2);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret2 + " 입니다.");
    }
}