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


def is_loop(matrix, startX, startY):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    idx = 0
    dirX, dirY = directions[idx]
    visited = set()
    currX, currY = startX, startY

    while (currX, currY, idx) not in visited:
        visited.add((currX, currY, idx))
        nextX, nextY = currX + dirX, currY + dirY

        if nextX < 0 or nextX >= len(matrix) or nextY < 0 or nextY >= len(matrix[0]) or matrix[nextX][nextY] == "#":
            idx = (idx + 1) % 4  # Turn 90 degrees clockwise
            dirX, dirY = directions[idx]
        else:
            currX, currY = nextX, nextY

        if (currX, currY) == (startX, startY) and idx == 0:
            return True  # Return to the start position with the same direction

    return False


def find_obstruction_positions(matrix, startX, startY):
    valid_positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == ".":
                # Temporarily place an obstruction
                matrix[i][j] = "O"
                if is_loop(matrix, startX, startY):
                    valid_positions.append((i, j))
                # Remove the obstruction
                matrix[i][j] = "."

    return valid_positions


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
    # print(res)
    valid_positions = find_obstruction_positions(matrix, currX, currY)
    print("Number of possible obstruction positions:", len(valid_positions))
    for pos in valid_positions:
        print("Possible obstruction at:", pos)


if __name__ == "__main__":
    main()
