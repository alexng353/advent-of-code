file = open("../inputs/3.txt", "r")


# split into groups of 3, list of list

lines = [line for line in file]
newlines = []
SUM = 0

for i in range(len(lines)//3):
    newlines.append([lines[i*3], lines[i*3+1], lines[i*3+2]])


for i in newlines:
    ascii_values = [ord(i) for i in list(
        set([j for j in i[0] if j in i[1] and j in i[2] and j != "\n"]))]

    for i in ascii_values:
        if i >= 65 and i <= 90:
            ascii_values[ascii_values.index(i)] = i - 38
        elif i >= 97 and i <= 122:
            ascii_values[ascii_values.index(i)] = i - 96

    # add all the ascii values together

    SUM += sum(ascii_values)

print(SUM)
