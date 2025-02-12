def shovel(k, r):
    for i in range(1, 10):
        if (k * i) % 10 == 0 or (k * i) % 10 == r:
            return i
    return 10
k ,r = map(int,input().split())
print(shovel(k, r))
