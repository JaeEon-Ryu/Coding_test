
// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Main {
    public int solution(int n) {
        int answer = 0;
        int[][] swirl = makeSwirl(n);

        // 대각선 합 구하기
        for (int i = 0; i < n; i++)
            answer += swirl[i][i];

        return answer;
    }

    // 소용돌이 모양의 배열 만들기
    public int[][] makeSwirl(int N) {
        int[][] arr = new int[N][N];
        int[][] visited = new int[N][N];

        int[] dx = { 0, 1, 0, -1 }, dy = { 1, 0, -1, 0 };
        int dir = 0, x = 0, y = -1;
        int num = 1;

        while (num <= N * N) {
            int newX = x + dx[dir], newY = y + dy[dir];

            // 다음 x,y 가 범위 안에 있고 방문하지 않은 곳이라면 방문
            if ((-1 < newX && newX < N) && (-1 < newY && newY < N) && (visited[newX][newY] == 0)) {
                arr[newX][newY] = num++;
                visited[newX][newY] = 1;
                x = newX;
                y = newY;
            } else { // 방향 바꾸기
                dir = (dir + 1) % 4;
            }
        }

        return arr;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Main sol = new Main();
        int n1 = 3;
        int ret1 = sol.solution(n1);
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret1 + " 입니다.");

        int n2 = 2;
        int ret2 = sol.solution(n2);
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret2 + " 입니다.");
    }
}