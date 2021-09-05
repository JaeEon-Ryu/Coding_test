class Main {
    public String solution(String s) {
        s += '#';
        String answer = "";
        // 0이 연속적으로 붙어있을때는 아무것도 하지 않도록 함
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '0' && s.charAt(i + 1) != '0')
                answer += "0";
            else if (s.charAt(i) == '1')
                answer += "1";
        }
        return answer;
    }

    // 아래는 테스트케이스 출력을 해보기 위한 main 메소드입니다. main 메소드는 잘못된 부분이 없으니, solution 메소드만
    // 수정하세요.
    public static void main(String[] args) {
        Main sol = new Main();
        String s = "101100011100";
        String ret = sol.solution(s);

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("solution 메소드의 반환 값은 \"" + ret + "\" 입니다.");
    }
}
