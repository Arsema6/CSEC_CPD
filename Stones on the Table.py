n = int(input())
stones =list(input())
minCount = 0
for i in range(1,n):
    if stones[i]==stones[i-1]:
        minCount+= 1
print(minCount)
