def solution(record):
    answer = []

    in_and_out = []
    user_info = dict()

    for sentence in record:
        situation = list(sentence.split())

        position = situation[0]
        user_id = situation[1]

        if position != 'Leave':
            user_info[user_id] = situation[2]

        if position != 'Change':
            in_and_out.append([position,user_id])

    for info in in_and_out:
        say = ''
        if info[0] == 'Enter' :
            say = "들어왔습니다."
        else :
            say = "나갔습니다."
        answer.append(str(user_info[info[1]]) + "님이 " + say  )

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))