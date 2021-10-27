# 0:north, 1: east, 2: south, 3:west
b, h, x, y = map(int, input().split(' '))
pos = 0
field = [['.' for _ in range(b)] for _ in range(h)]

field[y][x] = '#'  # harvest initial field


# min_x = max_x = x  # maintain max seen field


for inst in input():
    # harvest current pos
    """
    print(x, y)
    print(f'pos: {pos}')
    print(f'min_x: {min_x}, max_x: {max_x}')
    print(f'min_y: {min_y}, max_y: {max_y}')
    print()
    """

    if inst == '^':
        # move forward and harvest
        if pos == 0:
            y -= 1
            #min_y = min(min_y, y)
        elif pos == 1:
            x += 1
            #max_x = max(max_x, x)
        elif pos == 2:
            y += 1
            #max_y = max(max_y, y)
        elif pos == 3:
            x -= 1
            #min_x = min(min_x, x)

    elif inst == '>':
        # update pos to the right
        pos = (pos + 1) % 4
    elif inst == '<':
        # update pos to the left
        pos = (pos - 1) % 4

    field[y][x] = '#'

    if inst == '^':
        for row in field:
            print(row)
        print(x, y)
        print()

for row in field:
    print(row)
print()
