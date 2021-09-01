
// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Main {
    public int[] solution(int N, int[] votes) {

        int voteCounter[] = new int[11];
        // 번호에 대한 cnt 배열
        for (int i = 0; i < votes.length; i++) {
            voteCounter[votes[i]] += 1;
        }

        int maxVal = 0;
        int cnt = 0;
        for (int i = 1; i <= N; i++) {
            if (maxVal < voteCounter[i]) { // 최대 cnt 찾기
                maxVal = voteCounter[i];
                cnt = 1;
            } else if (maxVal == voteCounter[i]) { // 최대 cnt가 같다면 정답 추가
                cnt += 1;
            }
        }
        int answer[] = new int[cnt];
        for (int i = 1, idx = 0; i <= N; i++) { // 최대 cnt개수만큼
            if (voteCounter[i] == maxVal) {
                answer[idx] = i;
                idx += 1;
            }
        }
        return answer;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Main sol = new Main();
        int N1 = 5;
        int[] votes1 = { 1, 5, 4, 3, 2, 5, 2, 5, 5, 4 };
        int[] ret1 = sol.solution(N1, votes1);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + Arrays.toString(ret1) + " 입니다.");

        int N2 = 4;
        int[] votes2 = { 1, 3, 2, 3, 2 };
        int[] ret2 = sol.solution(N2, votes2);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + Arrays.toString(ret2) + " 입니다.");
    }
}