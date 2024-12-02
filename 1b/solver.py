file = open("input.txt", "r")
list1 = []
list2dict = {}
for line in file:
    if(len(line.split()) > 1):
        num1 = int(line.split()[0])
        num2 = int(line.split()[1])
        list1.append(num1)
        if num2 in list2dict:
            list2dict[num2] += 1
        else:
            list2dict[num2] = 1
similarityScore = 0
for num in list1:
    if num in list2dict:
        # print("old similarityScore", similarityScore)
        # print("num", num)
        # print("list2dict[num]",list2dict[num])
        similarityScore += num * list2dict[num]
        # print("new similarityScore", similarityScore)
print(similarityScore)

