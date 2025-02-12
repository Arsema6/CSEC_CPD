def calories(s):
    count = 0
    for c in s:
        if c=='1':
            count+=c1
        elif c=='2':
            count+=c2
        elif c=='3':
            count+= c3
        elif c== '4':
            count += c4
    print(count)
c1,c2,c3,c4 = map(int,input().split())
s = input("")
calories(s)
