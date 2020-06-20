# 선입선출 형식
# pop(0)으로 뽑아내면 된다.
# 최소걸리는 시간을 쟤야 한다.

def solution(bridge_length, weight, waiting_truck):
    time = 0
    passing_truck = []
    passing_time = []
    number_of_arrived = 0
    number_of_truck = len(waiting_truck)

    passing_truck.append(waiting_truck.pop(0))
    passing_time.append(0)

    while number_of_truck != number_of_arrived:

        if passing_time[0] >= bridge_length:
            passing_truck.pop(0)
            passing_time.pop(0)
            number_of_arrived += 1

        if waiting_truck:
            if sum(passing_truck) + waiting_truck[0] <= weight:
                passing_truck.append(waiting_truck.pop(0))
                passing_time.append(0)

        time += 1
        for i in range(len(passing_time)): passing_time[i] += 1

    return time

# 코드로 치면서 알고리즘을 짰다.
# 트럭이 모두 도착할 때 까지 무한반복을 하도록 했고
# ( 반복 될 때마다 시간 1초씩 증가 )
# 지나가고 있는 차량의 시간을 따로 모두 쟬 수 있도록
# 리스트를 하나 더 생성하였다.
#
# 조건문으로는 지나가고 있는 차량에 추가로
# 다음 차량이 올 경우 무게를 지탱할 수 있는지에 대한 조건
# 그리고 차가 다리를 지나갔을 경우에 대한 조건 등을 넣었다.
