noOfContest = int(input())
count = 0
for i in range(noOfContest):
    p,v,t = map(int,input().split())
    summ = p+v+t
    if summ >1:
        count += 1
print(count)
