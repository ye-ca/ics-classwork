import time

dx = 1
size = 1
maximum = 2
for n in range(1000):
    print("*" * size)
    size += dx
    if size == maximum:
        maximum += 1
        dx *= -1
    elif size == 1:
        dx *= -1
    time.sleep(0.05)
