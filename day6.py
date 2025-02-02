from typing import List


def solve(matrix: List[List[str]], currX: int, currY: int) -> int:
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    idx = 0
    dirX, dirY = directions[idx]
    count = 1
    matrix[currX][currY] = "X"
    while True:
        if currX + dirX < 0 or currX + dirX >= len(matrix) or currY + dirY < 0 or currY + dirY >= len(matrix[0]):
            break
        if matrix[currX + dirX][currY + dirY] == "#":
            idx += 1
            dirX, dirY = directions[idx % 4]
        else:
            currX += dirX
            currY += dirY
            if matrix[currX][currY] == ".":
                count += 1
                matrix[currX][currY] = "X"
    return count


def findLoopCount(currRow: int, currCol: int, matrix: List[List[int]],
                  visited: set = None, direction: int = 0, checkLoop: bool = False):
    if visited is None:
        visited = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    nextRow = directions[direction][0]
    nextCol = directions[direction][1]
    count = 0

    while 0 <= currRow < len(matrix) and 0 <= currCol < len(matrix[0]):

        if not checkLoop:
            if 1 <= currRow < len(matrix) - 1 and 1 <= currCol < len(matrix[0]) - 1 and matrix[currRow + nextRow][
                    currCol + nextCol] != "#":
                matrix[currRow + nextRow][currCol + nextCol] = "#"

                alreadyVisited = False
                for currDir in [0, 1, 2, 3]:
                    if (currRow + nextRow, currCol + nextCol, currDir) in visited:
                        alreadyVisited = True

                if not alreadyVisited and findLoopCount(currRow, currCol, matrix, set(), direction, True):
                    count += 1
                matrix[currRow + nextRow][currCol + nextCol] = "."
        else:
            if (currRow, currCol, direction) in visited:
                return True

        visited.add((currRow, currCol, direction))

        # If next position is blocked, change direction and go to the start of the loop without moving
        if 0 <= currRow + nextRow < len(matrix) and 0 <= currCol + nextCol < len(matrix[0]) and \
                matrix[currRow + nextRow][currCol + nextCol] == '#':
            direction = (direction + 1) % 4
            nextRow = directions[direction][0]
            nextCol = directions[direction][1]
            continue

        currRow += nextRow
        currCol += nextCol

    if checkLoop:
        return False

    return str(count)


def main():
    matrix = []
    with open(r'd:\adventofcode\day6.txt', 'r') as file:
        for line in file:
            levels = list(line.strip())
            matrix.append(levels)

    currX, currY = -1, -1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^":
                currX, currY = i, j
                break
    # res = solve(matrix, currX, currY)
    res = findLoopCount(currX, currY, matrix)
    print(res)


if __name__ == "__main__":
    main()
