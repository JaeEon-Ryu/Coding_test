
// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Main {
    public int solution(int[] arr) {
        // 여기에 코드를 작성해주세요.
        int cnt = 1, maxCnt = 0;
        int prev = 1000001;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < prev || i == arr.length - 1) { // 감소하거나 배열의 끝인 경우 maxCnt 계산
                maxCnt = Math.max(maxCnt, cnt);
                cnt = 1;
            } else if (arr[i] > prev) {
                cnt++;
            }
            prev = arr[i];
        }

        return maxCnt;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Main sol = new Main();
        int[] arr = { 3, 1, 2, 4, 5, 1, 2, 2, 3, 4 };
        int ret = sol.solution(arr);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
    }
}
