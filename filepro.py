
f = open("fruit.txt", "r")

lines = []

for line in f:
    lines.append(line.strip())

f.close()

print("Contents of the list:")
print(lines)
