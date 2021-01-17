
def steps(x, y):
    steps = 0
    while (y != x):
        if y % 2 != 0:
            y += 1
            steps += 1
        if y / 2 >= x:
            y /= 2
            steps += 1
        elif y / 2 < x:
            y += 1
            steps += 1
    return steps
print(steps(4,10))