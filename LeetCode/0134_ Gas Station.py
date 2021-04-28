'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost,
return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
If there exists a solution, it is guaranteed to be unique
'''

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        len_gas = len(gas)

        for starting_point in range(len_gas): # starting_point번째 index 부터 시작
            accumulated_gas = 0

            for next_index in range(len_gas): # starting으로부터 한바퀴 돌기
                idx = (starting_point + next_index) % len_gas
                accumulated_gas += gas[idx] - cost[idx]
                if accumulated_gas < 0:
                    break
            else: # for-else구문 ( for문이 break에 걸리지 않고 정상적으로 모두 수행되었다면 정답 반환 )
                return starting_point

        return -1



