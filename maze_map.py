class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def create_map(n):
    #Create new map
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(' ')
        grid.append(row)
    # Add boundary wall
    for i in range(n):
        grid[0][i] = '#'
        grid[n-1][i] = '#'
        grid[i][0] = '#'
        grid[i][n-1] = '#'
    # Add wall
    walls = [
        (1,2),(2,2),(3,2),(4,2),(4,3),(4,4),(2,4),
        (6,1),(6,2),(6,3),(6,4),(7,4),(8,4),(9,4),
        (10,3),(10,2),(10,1),(4,6),(5,6),
        (5,7),(5,8),(5,9),(7,7),(8,7),(9,7),
        (7,9),(7,10),(7,11)
    ]
    for x, y in walls:
        grid[y][x] = '#'
    # Player position
    grid[1][1] = 'P'
    # Box position
    grid[2][3] = 'C'
    grid[4][5] = 'C'
    grid[6][6] = 'C'
    # Destination position
    grid[3][10] = 'G'
    grid[5][10] = 'G'
    grid[7][5]  = 'G'
    return grid


def display_map(grid):
    #Display map
    for row in grid:
        line = ''
        for cell in row:
            line += '| ' + cell + ' '
        line += '|'
        print(line)