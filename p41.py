
import csv

data = {'Name': 'John', 'Age': 19, 'Place': 'Kerala'}

f = open("sample.csv", "w", newline="")
writer = csv.writer(f)

for key, value in data.items():
    writer.writerow([key, value])

f.close()

f = open("sample.csv", "r")
reader = csv.reader(f)

print("Contents of CSV file:")
for row in reader:
    print(row)

f.close()
