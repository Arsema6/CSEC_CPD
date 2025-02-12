def hero(s):
    ss = set(s)
    if len(ss)%2 != 0:
        print("IGNORE HIM!") 
    else:
        print("CHAT WITH HER!")
s = input("")
hero(s)
