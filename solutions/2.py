file = open("../inputs/2.txt", "r")


# A = rock
# B = paper
# C = scissors

# X = rock
# Y = paper
# Z = scissors

add_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

win = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}

win_invert = {
    "C": "X",
    "A": "Y",
    "B": "Z"
}

draw = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

draw_invert = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

lose = {
    "X": "B",
    "Y": "C",
    "Z": "A"
}

lose_invert = {
    "B": "X",
    "C": "Y",
    "A": "Z"
}


score = 0

for line in file:
    player1 = line[0]
    player2 = line[2]

    if player2 == "X":
        score += add_score[lose_invert[player1]]
    elif player2 == "Y":
        score += add_score[draw_invert[player1]]
        score += 3
    else:
        score += 6
        score += add_score[win_invert[player1]]

    #     if draw[player2] == player1:
    #         score += 3
    #         score += add_score[player2]

    #     elif win[player2] == player1:
    #         score += 6
    #         score += add_score[player2]

    #     else:
    #         score += add_score[player2]

print(score)
