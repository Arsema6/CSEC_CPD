def winner(n, s):
    CA = CD = 0
    for i in range(n):
        if s[i] == "A":
            CA += 1
        else:
            CD += 1
    if CA > CD:
        print("Anton")
    elif CA < CD:
        print("Danik")
    else:
        print("Friendship")

n = int(input())
s = str(input())
winner(n, s)
