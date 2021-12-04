# Open input file
file = open("input.txt")

# Establish variables & lists
count = 0
pos = 0
dep = 0
aim = 0
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

    # If keyword is forward increase pos by X and increase
    # dep by aim * X
    if i[0] == 'forward':
        pos += int(i[1])
        dep += aim * int(i[1])

    # If keyword is down then increase aim
    elif i[0] == 'down':
        aim += int(i[1])

    # If keyword is up then decrease aim
    else:
        aim -= int(i[1])

    count += 1

# Print results
print("\nPosition is", str(pos))
print("Depth is", str(dep))
print("Aim is", str(aim))
print(str(pos), "x", str(dep), "=", pos * dep)
