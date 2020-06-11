def solution(bridge_length, weight, truck_weights):
    queue = [0]*bridge_length
    time = 0
    i = 0
    Sum = 0
    while queue:
        time += 1
        Sum -= queue.pop(0)
        if i < len(truck_weights):
            if truck_weights[i]+Sum <= weight:
                Sum += truck_weights[i]
                queue.append(truck_weights[i])
                i += 1
            else:
                queue.append(0)
        else:
            time += bridge_length-1
            break
    return time




def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0] * bridge_length
    on_bridge_weight = 0
    truck_weights = truck_weights[::-1]
    while truck_weights : # 1초 사용
        answer += 1 # 다리에서 빠진다.
        on_bridge_weight -= on_bridge.pop(0) # (무게체크) 다리에 트럭이 올라갈수 있다.
        if weight >= on_bridge_weight + truck_weights[-1]: # 다리에 트럭하나가 들어온다.
            truck = truck_weights.pop()
            on_bridge.append(truck)
            on_bridge_weight += truck # 다리에 트럭을 올릴수 없다.
        else: # 트럭 왼쪽으로 이동 (=우측에 0값 넣기)
            on_bridge.append(0) # 입구에 남은 트럭이있기때문에 bridge_length를 더해준다.
    return answer + bridge_length
# print(solution(5, 10, [7, 2, 3, 1, 8, 5]))
# print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
