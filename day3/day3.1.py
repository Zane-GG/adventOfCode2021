# Open input file
file = open("input.txt")

# Establish initial variables
gamma = ""
epsilon = ""
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
        if a == "0":
            zeroC += 1
        else:
            oneC += 1

    # If their are more ones then append 1 to the gamma rate otherwise append 0
    if oneC > zeroC:
        gamma = gamma + "1"
    else:
        gamma = gamma + "0"

    # Reset the counts for next vertical list
    oneC = 0
    zeroC = 0

# For each of the new vertical lists (gamma rate)
for f in data:

    # For each element in the new lists increment the zeros and ones count
    for e in f:

        if e == "0":
            zeroC += 1
        else:
            oneC += 1

    # If their are less ones then append 1 to the epsilon rate otherwise append 0
    if oneC < zeroC:
        epsilon = epsilon + "1"
    else:
        epsilon = epsilon + "0"

    # Reset the counts for next vertical list
    oneC = 0
    zeroC = 0


print("\ngamma rate =", gamma)
print("epsilon rate =", epsilon)
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma, "x", epsilon, "=", gamma * epsilon)



