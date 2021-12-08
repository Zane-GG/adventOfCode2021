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

        if firstLine:
            data.append([i])

        else:
            data[count].append(i)
            count += 1

    firstLine = False
    count = 0

    for x in data:
        for i in x:
            print(i)



print(data)



