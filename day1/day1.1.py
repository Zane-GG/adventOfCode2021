# Open input file
file = open('example.txt')

# Establish lists and variables
measurements = []
c = 1
larger = 0

# For each line in the file strip blanks lines and append to list
for line in file:
    line = line.strip('\n')
    measurements.append(int(line))

# Print initial measurement
print(measurements[0], "(N/A - no previous measurement)")

# For each element after the first, check to see if it bigger than previous number
for i in measurements[1:]:
    if measurements[c] > measurements[c-1]:
        print(measurements[c], "(increased)")
        larger += 1

    else:
        print(measurements[c], "(decreased)")

    # Increment counter
    c += 1

# Print the total amount of larger numbers
print("There are", larger, "measurements larger than the previous measurement")
