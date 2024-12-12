file = open("input.txt", "r")
list1 = []
list2 = []
for line in file:
    if(len(line.split()) > 1):
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
list1.sort()
list2.sort()
total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])
print(total)
