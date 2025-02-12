def comp(f,s):
    fl = f.lower()
    sl = s.lower()
    if fl < sl:
        return -1
    elif fl == sl:
        return 0
    else:
        return 1
f = input("")
s = input("")
print(comp(f,s))
