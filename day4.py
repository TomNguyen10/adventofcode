from typing import List


def part1(maze: List[List[str]], r: int, c: int) -> int:
    count = 0
    if r - 3 >= 0 and maze[r - 1][c] == "M" and maze[r - 2][c] == "A" and maze[r - 3][c] == "S":
        count += 1
    if r + 3 < len(maze) and maze[r + 1][c] == "M" and maze[r + 2][c] == "A" and maze[r + 3][c] == "S":
        count += 1
    if c - 3 >= 0 and maze[r][c - 1] == "M" and maze[r][c - 2] == "A" and maze[r][c - 3] == "S":
        count += 1
    if c + 3 < len(maze[0]) and maze[r][c + 1] == "M" and maze[r][c + 2] == "A" and maze[r][c + 3] == "S":
        count += 1
    if r - 3 >= 0 and c - 3 >= 0 and maze[r - 1][c - 1] == "M" and maze[r - 2][c - 2] == "A" and maze[r - 3][c - 3] == "S":
        count += 1
    if r + 3 < len(maze) and c + 3 < len(maze[0]) and maze[r + 1][c + 1] == "M" and maze[r + 2][c + 2] == "A" and maze[r + 3][c + 3] == "S":
        count += 1
    if r - 3 >= 0 and c + 3 < len(maze[0]) and maze[r - 1][c + 1] == "M" and maze[r - 2][c + 2] == "A" and maze[r - 3][c + 3] == "S":
        count += 1
    if r + 3 < len(maze) and c - 3 >= 0 and maze[r + 1][c - 1] == "M" and maze[r + 2][c - 2] == "A" and maze[r + 3][c - 3] == "S":
        count += 1
    return count


def part2(maze: List[List[str]], r: int, c: int) -> bool:
    bool1 = maze[r-1][c-1] == 'M' and maze[r+1][c -
                                                1] == 'M' and maze[r-1][c+1] == 'S' and maze[r+1][c+1] == 'S'
    bool2 = maze[r-1][c-1] == 'S' and maze[r+1][c -
                                                1] == 'S' and maze[r-1][c+1] == 'M' and maze[r+1][c+1] == 'M'
    bool3 = maze[r-1][c-1] == 'S' and maze[r+1][c -
                                                1] == 'M' and maze[r-1][c+1] == 'S' and maze[r+1][c+1] == 'M'
    bool4 = maze[r-1][c-1] == 'M' and maze[r+1][c -
                                                1] == 'S' and maze[r-1][c+1] == 'M' and maze[r+1][c+1] == 'S'
    return bool1 or bool2 or bool3 or bool4


def main():
    maze = []
    with open(r'd:\adventofcode\day4.txt', 'r') as file:
        for line in file:
            levels = list(line.strip())
            maze.append(levels)
    res = 0
    # for i in range(len(maze)):
    #     for j in range(len(maze[0])):
    #         if maze[i][j] == "X":
    #             res += part1(maze, i, j)

    for i in range(1, len(maze)-1):
        for j in range(1, len(maze[0])-1):
            if maze[i][j] == "A" and part2(maze, i, j):
                res += 1

    print(res)


if __name__ == "__main__":
    main()
