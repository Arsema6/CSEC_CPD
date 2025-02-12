def gravityFlip(box):
    flipped = sorted(box,reverse = False)
    return ' '.join(map(str,flipped))
n = int(input())
box = list(map(int,input().split()))
print(gravityFlip(box))
