import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# animate_guide: https://www.geeksforgeeks.org/conways-game-life-python-implementation/
def create_grid(grid):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            grid[i, j] = 0
    return grid


# randomized grid
def randomize_grid(grid):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            grid[i, j] = int(np.random.randint(0, 2))
    return grid


def check_neighbours(grid, x, y):

    new_grid = np.copy(grid)

    count = 0

    # count_neighbours

    # control x edges
    if x == 0:
        # left edge
        x_range = range(x, x + 2)
    elif x == grid.shape[0] - 1:
        # right edge
        x_range = range(x - 1, x + 1)
    else:
        # default
        x_range = range(x - 1, x + 2)

    print(x_range)

    # control y edges
    if y == 0:
        # left edge
        y_range = range(y, y + 2)
    elif y == grid.shape[1] - 1:
        # right edge
        y_range = range(y - 1, y + 1)
    else:
        # default
        y_range = range(y - 1, y + 2)

    for i in x_range:
        for j in y_range:
            if grid[i, j] == 1:
                count += 1

    # dont count self
    if grid[x, y] == 1:
        count -= 1

    # apply rules
    # set for new_grid
    print(count)

    # if cell is on (1) and count<2 turn off (0)
    if grid[x, y] == 1 and count < 2:
        new_grid[x, y] = 0
    # if cell is on (1) and count>3 turn off (0)
    elif grid[x, y] == 1 and count > 3:
        new_grid[x, y] = 0
    # else stay alive (1)
    elif grid[x, y] == 1:
        new_grid[x, y] = 1
    # if cell in off (0) and count==3 run on (1)
    elif grid[x, y] == 0 and count == 3:
        new_grid[x, y] = 1

    return new_grid[x, y]


def update(i):
    new_grid = np.copy(grid)

    print(grid)
    print(type(grid))

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            new_grid[i, j] = check_neighbours(grid, i, j)

    # update data
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,


grid_dimensions = (100, 100)

iterations = 1000

grid = create_grid(np.zeros(grid_dimensions))

grid = randomize_grid(grid)

fig, ax = plt.subplots()
# change color with cmap setting
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, update,
                              frames=iterations,
                              interval=100,
                              save_count=50, repeat=False)

plt.show()
