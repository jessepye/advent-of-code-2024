import ipdb

inputFile = "input.txt"
# inputFile = "example.txt"
with open(inputFile, "r") as file:
    diskMap = file.read().strip()

print(f"initial diskMap:{diskMap}")

blocks = []

# create the blocks using the diskMap

id = 0
fileMode = True
for c in diskMap:
    if fileMode:
        for i in range(int(c)):
            blocks.append(id)
        id += 1
    else:
        for i in range(int(c)):
            blocks.append(None)
    fileMode = not fileMode

# we need this so that we can start at the last ID and iterate backwards
lastId = id - 1

print(f"blocks before defragging:{blocks}")

# we probably don't need this anymore
def findNextFreeBlockIndex(blocks, current) -> int:
    for i in range(len(blocks)):
        if blocks[i] == None:
            return i

def findInBlocks(blocks, target):
    start = None
    try:
        start = blocks.index(target)
    except ValueError:
        return None
    for i in range(start, len(blocks)):
        if blocks[i] != target:
            return start, i
    return start, len(blocks)

def findOpening(blocks, size):
    currentSize = 0
    for i in range(len(blocks)):
        if blocks[i] == None:
            currentSize += 1
            if currentSize >= size:
                return i - currentSize + 1
        else:
            currentSize = 0
    return None

# Start at the last id, iterate backwards
for i in range(lastId, -1, -1):
    print(f"i: {i}")
    start, end = findInBlocks(blocks, i)
    size = end - start
    openingIndex = findOpening(blocks, size)
    # ipdb.set_trace()
    if openingIndex != None and openingIndex < start:
        dataIndex = start
        for j in range(openingIndex, openingIndex + size):
            blocks[j], blocks[dataIndex] = blocks[dataIndex], blocks[j]
            dataIndex += 1

# calculate checksum:
checkSum = 0
for i in range(len(blocks)):
    if blocks[i] == None:
        continue
    checkSum += i*blocks[i]

print(f"defragged blocks: {blocks}")
print(f"checkSum: {checkSum}")
