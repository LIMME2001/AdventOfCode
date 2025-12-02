f = open("inputAoC1.txt")
lines = f.readlines()
password = 0
count = 50

for line in lines:
    prev_count = count
    line = line.strip()
    if(len(line) == 4):
        password += int(line[1])
        line = line[0] + line[-2:]
    if(line[0] == "R"):
        line = line.strip("R")
        count += int(line)
        if(count >= 100):
            password += 1 
            count = count % 100
    elif(line[0] == "L"):
        line = line.strip("L")
        count -= int(line)
        if(prev_count < 0 and count > 0 or prev_count > 0 and count < 0):
            password += 1
        if(count < 0):
            count = count % 100
        if(count == 0):
            password += 1
    print(count, prev_count, password)
print(password)