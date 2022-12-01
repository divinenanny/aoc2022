# read file
# read lines
# add lines until you reach blank line
# write totals to list
# get highest value from list

file1 = open("list.txt", "r")
elfs = []
count = 0

for line in file1:
    if line.strip():
        count += int(line)
    else:
        elfs.append(count)
        count = 0

elfs.sort(reverse = True)
topThree = elfs[0]+elfs[1]+elfs[2]

print("Answer to puzzle 1: " + str(elfs[0]))
print("Answer to puzzle 2: " + str(topThree))