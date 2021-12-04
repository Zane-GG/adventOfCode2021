# Open input file
file = open("input.txt")

# Establish variables & lists
count = 0
pos = 0
dep = 0
data = []

# For each line in the file strip newlines and split values based on space
for line in file:
    line = line.strip('\n')
    splitVal = line.split(" ")

    # Append split values to data list
    data.append(splitVal)

# For each command in the data
for i in data:
    print(data[count])

    # If keyword is forward the increase pos
    if i[0] == 'forward':
        pos += int(i[1])

    # If keyword is down then increase dep
    elif i[0] == 'down':
        dep += int(i[1])

    # If keyword is up then decrease dep
    else:
        dep -= int(i[1])

    count += 1

# Print results
print("\nPosition is", str(pos))
print("Depth is", str(dep))
print(str(pos), "x", str(dep), "=", pos * dep)

