#read file
#for each line
#split values at , (elf1 & elf2)
#split elf values at - (elf1Start, elf1End, elf2Start, elf2End)
#if elf1start is kleiner of gelijk aan elf2start
#zo ja, if elf1end is groter of gelijk aan elf2end
#zo ja, up counter met 1

a = open('values.txt').read()

total_part_1 = 0
total_part_2 = 0

for line in a.splitlines():
    # x, y are two sets created by splitting the line at ',' and taking the '-' separated numbers for range
    x = set(range(int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])+1))
    y = set(range(int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])+1))

    if x.issubset(y) or y.issubset(x):
        total_part_1 += 1

    if len(x.intersection(y)) > 0:
        total_part_2 += 1

print("Answer to puzzle 1: " + str(total_part_1))
print("Answer to puzzle 2: " + str(total_part_2))