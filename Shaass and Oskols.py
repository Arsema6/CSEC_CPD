noWire = int(input())
wires = list(map(int,input().split()))
shots = int(input())
for i in range(shots):
    wir, position = map(int, input().split())
    wir -= 1
    if wir - 1 >= 0:
        wires[wir - 1] += position - 1
    if wir + 1 < noWire:
        wires[wir + 1] += wires[wir] - position
    wires[wir] = 0
for wire in wires:
    print(wire)
