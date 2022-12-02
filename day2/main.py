
# function to determine score
#read file line by line
#score per line add to previous score

# X - 1 - Rock
# Y - 2 - Paper
# Z - 3 - Scissors
# A - Rock
# B - Paper
# C - Scissors
# Lose - 0
# Draw - 3
# Win - 6

# A X - d - 3 + 1 = 4
# A Y - w - 6 + 2 = 8
# A Z - l - 0 + 3 = 3
# B X - l - 0 + 1 = 1
# B Y - d - 3 + 2 = 5
# B Z - w - 6 + 3 = 9
# C X - w - 6 + 1 = 7
# C Y - l - 0 + 2 = 2
# C Z - d - 3 + 3 = 6

file1 = open("values.txt", "r")
scoreTotal = 0
scoreTotalWin = 0

for line in file1:
    opponent = line[0]
    you = line[2]
    score = 0
    scoreWin = 0
    if opponent == "A": # Rock
        if you == "X": #Lose - Scissors  = 0 + 3
            score += 4
            scoreWin += 3
        elif you == "Y": #Draw - Rock = 3 + 1
            score += 8
            scoreWin += 4
        elif you == "Z": #Win - Paper = 6 + 2
            score += 3
            scoreWin += 8
    elif opponent == "B": # Paper
        if you == "X": #Lose - Rock = 0 + 1
            score += 1
            scoreWin += 1
        elif you == "Y": #Draw - Paper = 3 + 2
            score += 5
            scoreWin += 5
        elif you == "Z": #Win - Scissors = 6 + 3
            score += 9
            scoreWin += 9
    elif opponent == "C": # Scissors
        if you == "X": #Lose - Paper = 0 + 2
            score += 7
            scoreWin += 2
        elif you == "Y": #Draw - Scissors = 3 + 3
            score += 2
            scoreWin += 6
        elif you == "Z": #Win - Rock = 6 + 1
            score += 6
            scoreWin += 7
    scoreTotal += score
    scoreTotalWin += scoreWin

print("Answer to puzzle 1: " + str(scoreTotal))
print("Answer to puzzle 2: " + str(scoreTotalWin))