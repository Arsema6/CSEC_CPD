n = int(input())
events =list(map(int,input().split()))
untreated=police = 0
for i in range(n):
    if events[i] == -1:
        if police>0:
            police -= 1
        else:
            untreated += 1
    else:
        police+=events[i]
print(untreated)
