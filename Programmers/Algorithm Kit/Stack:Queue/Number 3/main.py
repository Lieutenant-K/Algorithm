from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    n = len(truck_weights)
    passed_truck, current_weight = 0, 0
    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    while passed_truck != n:
        if bridge[0] > 0:
            current_weight -= bridge[0]
            passed_truck += 1
            bridge[0] = 0
        bridge.append(bridge.popleft())
        if len(trucks) > 0 and current_weight + trucks[0] <= weight:
            truck_weight = trucks.popleft()
            bridge[-1] = truck_weight
            current_weight += truck_weight
        answer += 1
    return answer