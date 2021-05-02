'''
각 판매원의 이름을 담은 배열 enroll
각 판매원을 다단계 조직에 참여시킨 다른 판매원의 이름을 담은 배열 referral
판매량 집계 데이터의 판매원 이름을 나열한 배열 seller
판매량 집계 데이터의 판매 수량을 나열한 배열 amount
["john", "mary", "edward", "sam   ", "emily", "jaimie", "tod   ", "young"]
["-   ", "-   ", "mary  ", "edward", "mary ", "mary  ", "jaimie", "edward"]
["young", "john", "tod", "emily", "mary"]
[12     ,      4,     2,       5,     10] -> 판매 수량 ( 개당 100원 )
[360, 958, 108, 0, 450, 18, 180, 1080] -> enroll에 대한 판매 수량
'''


def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]

    mapper = {} # 시간 복잡도를 줄일 수 있도록 해쉬 활용
    for i,(e,r) in enumerate(zip(enroll,referral)):
        mapper[e] = [r,i] # 판매원 이름(enroll)에 대해 상위 판매원 이름 (referral)과 인덱스 저장

    for i,quantity in enumerate(amount): # 각 판매수량에 대한 계산
        price = quantity * 100
        seller_name = seller[i]

        while True: # do-while 형식
            next_price = int(price*0.1) # 10% 를 계산할 때에는 원 단위에서 절사
            parents_name,seller_idx = mapper[seller_name] # seller 이름에 대한 해쉬값 ( 상위 이름, 판매자 인덱스 )
            answer[seller_idx] += price - next_price
            price = next_price

            if parents_name == "-": # 상위 노드가 root
                break

            seller_name = parents_name

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
["young", "john", "tod", "emily", "mary"],
[12,4,2,5,10]))