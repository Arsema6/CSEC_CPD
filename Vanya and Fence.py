def validHeight(Height, sn):
    Width = 0
    for i in sn:
        if i > Height:
            Width += 2
        else:
            Width += 1
    return Width

n, Height = map(int, input().split())
sn = list(map(int, input().split()))
print(validHeight(Height, sn))
