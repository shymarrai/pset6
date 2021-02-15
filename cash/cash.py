from cs50 import get_float
while True:
    owed = get_float("Change owed:")
    if owed >= 0:
        break
    else:
        continue
owed = round(owed * 100)

count = 0

while owed >= 25:
    count += 1
    owed -= 25

while owed >= 10:
    count += 1
    owed -= 10

while owed >= 5:
    count += 1
    owed -= 5

while owed > 0.00:
    owed -= 1
    count += 1

print(f"{count}")

