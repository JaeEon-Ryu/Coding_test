
// 다음과 같이 import를 사용할 수 있습니다.
import java.util.*;

class Main {
    public long solution(long num) {
        String strNum = Long.toString(num);
        String answer = "";

        // 주어진 숫자 뒤부터 탐색
        for (int i = strNum.length() - 1; i > -1; i--) {
            String digit = "" + strNum.charAt(i);

            if (digit.equals("9")) { // 9일 때 1로
                answer = "1" + answer;
                if (i == 0) { // 맨 앞의 숫자가 9인데 반복문이 끝난다면
                    answer = "1" + answer;
                }
            } else { // 9가 아니라면 나머지 숫자들 더하기
                digit = "" + (Integer.parseInt(digit) + 1);
                answer = strNum.substring(0, i) + digit + answer;
                break;
            }
        }

        return Long.parseLong(answer);
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다.
    public static void main(String[] args) {
        Main sol = new Main();
        long num = 9949999;
        long ret = sol.solution(num);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 " + ret + " 입니다.");
    }
}