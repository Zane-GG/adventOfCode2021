# Open input file
file = open("example.txt")

# Establish initial variables
o2 = ""
c02 = ""
data = []
o2List = []
co2List = []
firstLine = True
count = 0
zeroC = 0
oneC = 0
hCount = 0

# For each line in the file strip new lines
for line in file:
    line = line.strip('\n')
    o2List.append(line)
    co2List.append(line)
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
        # print(x[count])

        if count < len(x) - 1:
            print(i)
            count += 1

            if i == "0":
                zeroC += 1

            else:
                oneC += 1

        else:
            print("Zeros =", zeroC)
            print("Ones =", oneC)
            print("END OF LIST")

            if zeroC > oneC:
                for a in o2List:

                    if a[hCount] == "1":
                        o2List.pop(0)
                        # print(o2List)
                # hCount += 1

            elif zeroC < oneC:
                for a in o2List:

                    if a[hCount] == "0":
                        o2List.pop(0)
                        # print(o2List)
                # hCount += 1

            count = 0
            zeroC = 0
            oneC = 0
            hCount += 1

    print(o2List)




print(data)
print(o2List)
print(co2List)



