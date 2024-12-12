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

print(f"blocks before defragging:{blocks}")

# find the first free block:
def findNextFreeBlockIndex(blocks, current) -> int:
    for i in range(len(blocks)):
        if blocks[i] == None:
            return i

freeBlockIndex = findNextFreeBlockIndex(blocks, 0)

print(f"Found first free block at index {freeBlockIndex}")

# Start at the last element, iterate backwards
for i in range(len(blocks) - 1, -1, -1):
    print(f"i: {i}, freeBlockIndex: {freeBlockIndex}")
    # make sure we're moving real data
    if blocks[i] == None:
        continue
    # break if finished
    if freeBlockIndex >= i:
        break
    # Move the data to the first free block
    blocks[i], blocks[freeBlockIndex] = blocks[freeBlockIndex], blocks[i]
    freeBlockIndex = findNextFreeBlockIndex(blocks, freeBlockIndex)

# calculate checksum:
checkSum = 0
for i in range(len(blocks)):
    if blocks[i] == None:
        break
    checkSum += i*blocks[i]

print(f"defragged blocks: {blocks}")
print(f"checkSum: {checkSum}")
