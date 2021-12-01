# Open input file
file = open('input.txt')

# Establish lists and variables
measurements = []
sums = []
c = 3
larger = 0

# For each line in the file strip blanks lines and append to list
for line in file:
    line = line.strip('\n')
    measurements.append(int(line))

print(measurements)

# Print initial measurement
sums.append(measurements[2] + measurements[1] + measurements[0])
print(sums[0], "(N/A - no previous sum)")


# For each element from the 3rd element append the sum of three numbers
for i in measurements[3:]:

    sums.append(measurements[c-2] + measurements[c-1] + measurements[c])

    # If the the 2nd sum is bigger than the 1st sum then print 'increased'
    if sums[-1] > sums[-2]:
        print(sums[-1], "(increased)")
        larger += 1

    # If 2nd and 1st sum is same than print 'no change'
    elif sums[-1] == sums[-2]:
        print(sums[-1], "(no change)")

    # Otherwise the sum has decreased
    else:
        print(sums[-1], "(decreased)")

    # Increment counter
    c += 1

# Print the total amount of larger numbers
print("There are", larger, "sums larger than the previous measurement")
