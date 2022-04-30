def solution(statues):
    count = 0
    mini = min(statues)
    maxi = max(statues)
    for i in range(mini, maxi):
        if i in statues:
            continue
        else:
            count += 1
    return count

print(solution(list1))
