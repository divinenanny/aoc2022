file1 = open("test.txt", "r")
values = []
matchesSingle = 0
matchesThree = 0

def numValue(matchedChar):
    switch={
      'a':1,
      'b':2,
      'c':3,
      'd':4,
      'e':5,
      'f':6,
      'g':7,
      'h':8,
      'i':9,
      'j':10,
      'k':11,
      'l':12,
      'm':13,
      'n':14,
      'o':15,
      'p':16,
      'q':17,
      'r':18,
      's':19,
      't':20,
      'u':21,
      'v':22,
      'w':23,
      'x':24,
      'y':25,
      'z':26,
      'A':27,
      'B':28,
      'C':29,
      'D':30,
      'E':31,
      'F':32,
      'G':33,
      'H':34,
      'I':35,
      'J':36,
      'K':37,
      'L':38,
      'M':39,
      'N':40,
      'O':41,
      'P':42,
      'Q':43,
      'R':44,
      'S':45,
      'T':46,
      'U':47,
      'V':48,
      'W':49,
      'X':50,
      'Y':51,
      'Z':52
      }
    return switch.get(matchedChar,"Invalid input")

for line in file1:
    values.append(line.strip())

for i in range(0, len(values)):
    bothComps = values[i]
    length = len(bothComps)
    half = int((length)/2)
    comp1 = bothComps[0:int(half)]
    comp2 = bothComps[int(half):]
    for t in range(0, half):
        if comp1[t] in comp2:
            matchesSingle += numValue(comp1[t])
            break

for f in range(0, len(values)):
    if f%3 != 0:
        continue
    sacks = []
    sacks.append(values[f])
    sacks.append(values[f+1])
    sacks.append(values[f+2])
    sacks.sort(key=len)
    f += 3
    for g in range(0, len(sacks[0])):
        sack = sacks[0]
        if sack[g] in sacks[1]:
            if sack[g] in sacks[2]:
                matchesThree += numValue(sack[g])
                break

print("Answer to puzzle 1: " + str(matchesSingle))
print("Answer to puzzle 2: " + str(matchesThree))