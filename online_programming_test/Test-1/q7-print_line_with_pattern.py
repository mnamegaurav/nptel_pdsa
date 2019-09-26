lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
pattern = lines[0]
for line in lines[1:]:
    if pattern in line:
        print(line)