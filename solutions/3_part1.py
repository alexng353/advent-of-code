file = open("../inputs/3.txt", "r")


# get first line in file
SUM = 0
for line in file:
    print(line)

    # split into 2 parts by middle

    section_1 = line[:len(line)//2]
    section_2 = line[len(line)//2:]

    # compare and get matching characters

    matching_chars = [i for i in section_1 if i in section_2]

    print(matching_chars)

    # dedupe

    matching_chars = list(set(matching_chars))

    # get the ascii values of the matching characters

    ascii_values = [ord(i) for i in matching_chars]

    print(ascii_values)

    for i in ascii_values:
        if i >= 65 and i <= 90:
            # replace with i - 64

            ascii_values[ascii_values.index(i)] = i - 38

        elif i >= 97 and i <= 122:
            # replace with i - 96

            ascii_values[ascii_values.index(i)] = i - 96

    print(ascii_values)

    # add all the ascii values together

    SUM += sum(ascii_values)

print(SUM)
