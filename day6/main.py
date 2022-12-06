import collections

file1 = open('values.txt').read()

for line in file1.splitlines(): 
    inputString = line

def findMarker(stringLength):
    marker = ""
    count = 0
    for i in range(0, len(inputString)):
        print("i = " + str(i))
        print("before if/else marker is: " + marker)
        if len(marker) < stringLength:
            print("marker is korter dan 4")
            marker = marker + (inputString[i])
            print("marker is korter dan 4 en is nu: " + marker)
        else:
            print("marker is langer dan 4")
            marker = marker[1:]
            print("marker met eerste char er af is: " + marker)
            marker = marker + (inputString[i])
            print("marker is langer dan 4 en is nu: " + marker)
            counterMarker = collections.Counter(marker)
            print("counter = " + str(counterMarker))
            if (len(list(set(list(counterMarker.values())))) == 1) and (list(counterMarker.values())[0] == 1):
                count = i+1
                break
    return count

print("Answer to puzzle 1: " + str(findMarker(4)))
print("Answer to puzzle 2: " + str(findMarker(14)))