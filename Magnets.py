n = int(input())
count = 1
magnet = []
for i in range(n):
    magnet.append(int(input()))
for i in range(1,n):
    if magnet[i]!=magnet[i-1]:
        count+=1
print(count)
