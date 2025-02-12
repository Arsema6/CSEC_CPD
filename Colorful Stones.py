s = input().strip()
t = input().strip()
position = 0
for instruction in t:
    if s[position] == instruction:
        position += 1
    if position == len(s):
        break
print(position + 1)
