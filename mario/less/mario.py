from cs50 import get_int

h = get_int("Height: ")

while True:
    if h > 0 and h < 9:
        break
    else:
        h = int(input("Height: "))
block = 1
for space in range(h, 0, -1):
    print(" " * (space - 1), end="#" * block)
    print()
    block += 1
