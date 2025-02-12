def prob():
    Y, W = map(int, input().split())
    probability = ["", "1/1", "5/6", "2/3", "1/2", "1/3", "1/6"]
    D = max(Y, W)
    print(probability[D])
prob()
