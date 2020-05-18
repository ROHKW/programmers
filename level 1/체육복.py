def solution(n, lost, reserve):
    new_reserve = set(reserve) - set(lost)
    new_lost = set(lost) - set(reserve)
    for idx in new_reserve:
        if idx-1 in new_lost:
            new_lost.remove(idx-1)
        elif idx+1 in new_lost:
            new_lost.remove(idx+1)
    return n - len(new_lost)
