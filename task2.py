f = open("inputAoC2.txt")
lines = f.readlines()
line = lines[0].strip().split(",")
print(line)
invalid_ids = []
for entry in line:
    entry = entry.split("-")
    start = int(entry[0])
    end = int(entry[1])
    for i in range(start, end + 1):
        s = str(i)
        L = len(s)
        for block_size in range(1, L):
            if L % block_size != 0:
                continue
            block = s[:block_size]
            if block * (L // block_size) == s:
                print(i)
                invalid_ids.append(i)
                break

total = 0
for line in invalid_ids:
    total += int(line)

print(total)

# For the first star:
"""
f = open("inputAoC2.txt")
lines = f.readlines()
line = lines[0].strip().split(",")
print(line)
invalid_ids = []
for entry in line:
    entry = entry.split("-")
    start = int(entry[0])
    end = int(entry[1])
    for i in range(start, end + 1):
        length_i = len(str(i))
        if(length_i%2 != 0):
            continue
        else:
            half = length_i // 2
            if(str(i)[:half] == str(i)[half:]):
                print(i)
                invalid_ids.append(i)
total = 0
for line in invalid_ids:
    total += int(line)

print(total)
"""