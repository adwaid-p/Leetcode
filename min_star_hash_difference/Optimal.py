str = input()

hash = 0
star = 0

for char in str:
    if char == '#':
        hash += 1
    elif char == '*':
        star += 1

print(star - hash)