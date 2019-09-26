lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
pattern = lines[0]
new_line = []
for line in lines[1:]:
    if pattern in line:
        new_line.append(line)
        
print(new_line[-1])