def years(l,b):
    count = 0
    while l<=b:
        count += 1
        l = 3*l
        b = 2*b
    return count
a,b = map(int,input().split())
print(years(a,b))
