#Input python3 game.py to start. 

from maze_map import create_map, display_map, Player

def move_player(grid, player, cmd):
    # Move method
    if cmd == 'w':
        dx, dy = 0, -1
    elif cmd == 's':
        dx, dy = 0, 1
    elif cmd == 'a':
        dx, dy = -1, 0
    elif cmd == 'd':
        dx, dy = 1, 0
    else:
        return False

    nx = player.x + dx
    ny = player.y + dy
    # Cannot touch boundary
    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
        return False
    # Cannot touch wall
    if grid[ny][nx] == '#':
        return False
    # Push box
    if grid[ny][nx] == 'C':
        bx = nx + dx
        by = ny + dy
        if bx < 0 or bx >= len(grid) or by < 0 or by >= len(grid[0]):
            return False
        if grid[by][bx] == '#' or grid[by][bx] == 'C':
            return False
        grid[by][bx] = 'C'
    #Player move
    grid[player.y][player.x] = ' '
    player.x = nx
    player.y = ny
    grid[player.y][player.x] = 'P'
    return True


def main():
    size = 12
    initial_grid = create_map(size)
    # Remember the position of destination
    targets = []
    for y in range(size):
        for x in range(size):
            if initial_grid[y][x] == 'G':
                targets.append((x, y))

    # create a initial map
    grid = []
    for row in initial_grid:
        new_row = []
        for cell in row:
            new_row.append(cell)
        grid.append(new_row)

    player = Player(1, 1)
    steps = 0
    best_threshold = 90
    bad_threshold = 130
    game_over = False

    # Instruction manual
    display_map(grid)
    print("Welcome to box pushing game, you can control your character's actions through WASD.")
    print("You can press H to reset the game at any time, and press Q to exit the game.")

    while True:
        cmd = input('Enter (w/a/s/d | map | status | h | q): ').strip().lower()

        if cmd == 'q':
            #Quit game
            print('Exiting game.')
            break

        if cmd == 'h':
            # Restart game
            grid = []
            for row in initial_grid:
                new_row = []
                for cell in row:
                    new_row.append(cell)
                grid.append(new_row)
            player = Player(1, 1)
            steps = 0
            game_over = False
            print('Game reset to initial state.')
            display_map(grid)
            continue

        if game_over:
            print('Game is over. Press H to restart or Q to quit.')
            continue

        if cmd == 'map':
            display_map(grid)

        elif cmd == 'status':
            print(f'Position: ({player.x},{player.y}) Steps: {steps}')

        elif cmd in ('w', 'a', 's', 'd'):
            moved = move_player(grid, player, cmd)
            if moved:
                #remember step
                steps += 1
                # If destination change to '','target' will make '' to be 'G'
                for tx, ty in targets:
                    if grid[ty][tx] == ' ':
                        grid[ty][tx] = 'G'
                display_map(grid)
                # How to win
                all_covered = True
                for tx, ty in targets:
                    if grid[ty][tx] != 'C':
                        all_covered = False
                        break
                if all_covered:
                    if steps <= best_threshold:
                        print(f'Your IQ is already over 99% of the people')
                    elif steps > bad_threshold:
                        print('菜（cai）！')
                    else:
                        print(f'Congratulations! Completed in {steps} steps.')
                    game_over = True
            else:
                print("Can't move")

        else:
            print('Invalid command')

if __name__ == '__main__':
    main()
