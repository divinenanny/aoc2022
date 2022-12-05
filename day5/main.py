stack1 = ["R", "G", "H", "Q", "S", "B", "T", "N"]
stack2 = ["H", "S", "F", "D", "P", "Z", "J"]
stack3 = ["Z", "H", "V"]
stack4 = ["M", "Z", "J", "F", "G", "H"]
stack5 = ["T", "Z", "C", "D", "L", "M", "S", "R"]
stack6 = ["M", "T", "W", "V", "H", "Z", "J"]
stack7 = ["T", "F", "P", "L", "Z"]
stack8 = ["Q", "V", "W", "S"]
stack9 = ["W", "H", "L", "M", "T", "D", "N", "C"]

file1 = open('values.txt').read()
file2 = open('test.txt').read()

sub1 = "move "
sub2 = " from "
sub3 = " to "

for line in file1.splitlines():
    idx1 = line.index(sub1)
    idx2 = line.index(sub2)
    idx3 = line.index(sub3)
    move = int(line[idx1 + len(sub1): idx2])
    origin = "stack" + (line[idx2 + len(sub2): idx3])
    destination = "stack" + (line[idx3 + len(sub3)])
    for i in range(0, move):
        locals()[destination].append(locals()[origin][-1])
        del locals()[origin][-1]

print("Answer to puzzle 1: " + stack1[-1]+stack2[-1]+stack3[-1]+stack4[-1]+stack5[-1]+stack6[-1]+stack7[-1]+stack8[-1]+stack9[-1])

stack9001_1 = ["R", "G", "H", "Q", "S", "B", "T", "N"]
stack9001_2 = ["H", "S", "F", "D", "P", "Z", "J"]
stack9001_3 = ["Z", "H", "V"]
stack9001_4 = ["M", "Z", "J", "F", "G", "H"]
stack9001_5 = ["T", "Z", "C", "D", "L", "M", "S", "R"]
stack9001_6 = ["M", "T", "W", "V", "H", "Z", "J"]
stack9001_7 = ["T", "F", "P", "L", "Z"]
stack9001_8 = ["Q", "V", "W", "S"]
stack9001_9 = ["W", "H", "L", "M", "T", "D", "N", "C"]

for line in file1.splitlines():
    idx1 = line.index(sub1)
    idx2 = line.index(sub2)
    idx3 = line.index(sub3)
    move = int(line[idx1 + len(sub1): idx2])
    origin = "stack9001_" + (line[idx2 + len(sub2): idx3])
    destination = "stack9001_" + (line[idx3 + len(sub3)])
    store = []
    for i in range(0, move):
        store.append(locals()[origin][-1])
        del locals()[origin][-1:]
    for f in range(0, len(store)):
        locals()[destination].append(store[-1])
        del store[-1:]

print("Answer to puzzle 2: " + stack9001_1[-1]+stack9001_2[-1]+stack9001_3[-1]+stack9001_4[-1]+stack9001_5[-1]+stack9001_6[-1]+stack9001_7[-1]+stack9001_8[-1]+stack9001_9[-1])
