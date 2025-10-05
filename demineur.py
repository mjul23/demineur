import random

def make_grid(size, num_mines):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    mines = set()
    while len(mines) < num_mines:
        i, j = random.randint(0, size-1), random.randint(0, size-1)
        if (i, j) not in mines:
            mines.add((i, j))
            grid[i][j] = '*'
    # Add numbers
    for i in range(size):
        for j in range(size):
            if grid[i][j] != '*':
                grid[i][j] = str(sum(
                    1 for di in [-1,0,1] for dj in [-1,0,1]
                    if (di,dj)!=(0,0) and 0<=i+di<size and 0<=j+dj<size and grid[i+di][j+dj]=='*'
                ))
    return grid, mines

def print_grid(grid, uncovered):
    size = len(grid)
    print("    " + " ".join(map(str, range(size))))
    for i in range(size):
        row = []
        for j in range(size):
            row.append(grid[i][j] if uncovered[i][j] else '?')
        print(f"{i} | " + " ".join(row))

def main():
    size = 5
    num_mines = 5
    grid, mines = make_grid(size, num_mines)
    uncovered = [[False]*size for _ in range(size)]

    while True:
        print_grid(grid, uncovered)
        row = int(input("Ligne: "))
        col = int(input("Colonne: "))
        if (row, col) in mines:
            print("Boom! Perdu.")
            break
        uncovered[row][col] = True
        # Vérifier la victoire
        if all(uncovered[i][j] or grid[i][j]=='*' for i in range(size) for j in range(size)):
            print("Gagné!")
            break

if __name__ == "__main__":
    main()
