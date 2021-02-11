'''
heap 자료구조 관련 문제인데, heap을 쓰지 않았음에도 정답으로 나와 당황했다.
그래서 파이썬 레퍼런스를 찾아보니 max()와 min() 함수는 다음의 두가지 함수
heapq.nlargest(1, iterable, key=keyfunc) 와
heapq.nsmallest(1, iterable, key=keyfunc) 에 일관성을 유지한다고 나와있다.
따라서 max(), min()을 썼음에도 수행시간이 nlogn으로 유지되었던 것 같다.

---------------------------------------------------------------

heap은 우선순위 큐를 위하여 만들어진 자료구조이다.
우선순위큐 : 데이터들이 우선순위를 가지고 있고 우선순위가 높은 데이터가 먼저 나간다.

삭제되는 요소
스택 : 가장 최근에 들어온 데이터 삭제
큐 : 가장 먼저 들어온 데이터 삭제
우선순위 큐 : 가장 우선순위가 높은 데이터 삭제

우선순위 큐는 배열, 연결리스트, 힙으로 구현이 가능하며 이 중에서 힙으로 구현하는 것이 가장 효율적이다.
( 힙은 삽입 그리고 삭제면에서 nlogn의 수행시간을 갖고 있다. )

힙은 완전 이진 트리의 일종으로 우선순위 큐를 위하여 만들어진 자료구조이다.
-> 여러 개의 값들 중에서 최댓값이나 최솟값을 빠르게 찾아내도록 만들어진 자료구조이다.
부모 노드의 키 값이 자식 노드의 키값보다 항상 큰 이진트리이다.

힙을 저장하는 표준적인 자료구조는 배열이다.
힙의 추가 : 일단 힙에 새로운 요소가 들어오면, 이 새로운 노드를 힙의 마지막 노드에 이어서 삽입하고
새로운 노드를 부모 노드들과 비교, 교환하여 힙의 성질을 만족시킨다.
힙의 삭제 : 삭제된 자리에 힙의 마지막 노드를 가져오고 다시 부모노드, 자식노드와 비교, 교환하며 힙의 성질을 만족시킨다.

참고 : https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html

---------------------------------------------------------------------

파이썬에는 외장 함수 heapq 가 있으며 데이터를 추가할 때 heapq.heappush(리스트,변수),
데이터를 삭제할 때 heapq.heappop(리스트) 등을 통하여 문제를 풀 수 있다.
'''


def solution(operations):
    queue = []

    for op in operations:
        if op[0] == 'I':
            queue.append(int(op[2:]))
        else:
            if queue:
                if op[2] == '-':
                    del queue[queue.index(min(queue))]
                else:
                    del queue[queue.index(max(queue))]

    if queue:
        return [max(queue),min(queue)]
    else:
        return [0,0]

operations = ['I 7','I 5','I -5','D -1']
print(solution(operations))