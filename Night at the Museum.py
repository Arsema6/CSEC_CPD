def minRotation(nameOfExihibit):
    position = 'a'
    rotation = 0
    for name in nameOfExihibit:
        clockwiseDistance = (ord(name)-ord(position))%26
        counterClockwiseDistance = (ord(position) -ord(name))%26
        rotation += min(clockwiseDistance,counterClockwiseDistance)
        position = name
    print(rotation)
nameOfExihibit = input("")
minRotation(nameOfExihibit)
