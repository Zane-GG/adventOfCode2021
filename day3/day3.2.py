# Open input file
file = open("example.txt")

# Establish initial variables
o2 = ""
c02 = ""
data = []
firstLine = True
count = 0
zeroC = 0
oneC = 0

# For each line in the file strip new lines
for line in file:
    line = line.strip('\n')
    print(line)

    # For each element in a line
    for i in line:

        # If its the first line then create a list for each element
        if firstLine:
            data.append([i])

        # If its not the first line then append each elements to the each positional list
        else:
            data[count].append(i)
            count += 1

    firstLine = False
    count = 0

# For each of the new vertical lists (gamma rate)
for x in data:
    print(x)

    # For each element in the new lists increment the zeros and ones count
    for a in x:
        pass

    # Reset the counts for next vertical list
    oneC = 0
    zeroC = 0

# For each of the new vertical lists (gamma rate)
for f in data:

    # For each element in the new lists increment the zeros and ones count
    for e in f:

        pass

    # Reset the counts for next vertical list
    oneC = 0
    zeroC = 0



