
// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Main {
    public int solution(String pos) {
        int answer = 0;
        int[][] arr = new int[8][8];
        int x, y;
        x = 8 - (int) (pos.charAt(1) - '0'); // 최초x
        y = (int) pos.charAt(0) - 65; // 최초y

        // 나아갈 방향들
        int[][] dxy = { { 1, 2 }, { -1, 2 }, { 1, -2 }, { -1, -2 }, { 2, 1 }, { -2, 1 }, { 2, -1 }, { -2, -1 } };

        int dx, dy, newX, newY;
        for (int i = 0; i < 8; i++) {
            dx = dxy[i][0]; // 방향 x
            dy = dxy[i][1]; // 방향 y

            newX = x + dx; // 해당 방향으로 이동한 x
            newY = y + dy; // 해당 방향으로 이동한 y
            if ((-1 < newX && newX < 8) && (-1 < newY && newY < 8)) { // 격자 안에 있다면
                answer++;
            }
        }

        return answer;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Main sol = new Main();
        String pos = "A7";
        int ret = sol.solution(pos);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
    }
}