n = int(input())
cards =list(map(int,input().split()))
sumS = sumD = 0
l,r = 0,n-1
turn = True
while(l<=r):
    if cards[l]>cards[r]:
        if turn:
            sumS+=cards[l]
        else:
            sumD+=cards[l]
        l+=1
    else:
        if turn:
            sumS+=cards[r]
        else:
            sumD+=cards[r]
        r-=1
    turn = not turn
print(sumS,sumD)
