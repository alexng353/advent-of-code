# read 1.txt

file = open("../inputs/1.txt", "r")

# iterate by line
MAX = 0
SECOND = 0
THIRD = 0
TOTAL = 0
CURRENT = 0
for line in file:
    if line != "\n":
        CURRENT += int(line)
    else:
        if CURRENT > MAX:
            THIRD = SECOND
            SECOND = MAX
            MAX = CURRENT
        elif CURRENT > SECOND:
            THIRD = SECOND
            SECOND = CURRENT
        elif CURRENT > THIRD:
            THIRD = CURRENT
        CURRENT = 0

TOTAL = MAX + SECOND + THIRD
print(TOTAL)
