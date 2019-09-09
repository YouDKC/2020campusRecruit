# 4
# 6 5 3 4
# 4 3 5 6
from collections import defaultdict
count= int(input().strip())
robots = [int(i) for i in input().strip().split(' ')][::-1]
times = defaultdict(int)
if len(robots)==1:
    print(1)
for i in range(len(robots)-1):
    flag = robots[i]
    for j in range(i+1,len(robots)):
        if robots[j]>robots[i]:
            times[robots[j]]+=1
            break
        elif robots[j]==robots[i]:
            times[robots[j]] += 1
        else:
            times[robots[j]] += 0
res = times[robots[0]]
m = -1
for robot in robots[1:]:
    if times[robot]>m:
        m =times[robot]
        res = robot
print(res)