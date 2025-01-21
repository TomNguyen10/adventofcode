from typing import List


def checkSafe(matrix: List[List[int]]) -> int:
    count = 0
    for level in matrix:
        safe = True
        prev = None
        for i in range(1, len(level)):
            diff = level[i] - level[i - 1]
            if abs(diff) < 1 or abs(diff) > 3:
                safe = False
                break
            if prev and diff * prev < 0:
                safe = False
                break
            prev = diff
        if safe:
            count += 1
    return count


def checkSafe2(matrix: List[List[int]]) -> int:
    count = 0
    for level in matrix:
        prev = None
        damper = 0
        for i in range(1, len(level)):
            diff = level[i] - level[i - 1]
            if abs(diff) < 1 or abs(diff) > 3:
                damper += 1
            if prev and diff * prev < 0:
                damper += 1
            prev = diff
        if damper < 2:
            count += 1
    return count


def main():
    report = []
    with open(r'd:\adventofcode\day2.txt', 'r') as file:
        for line in file:
            levels = list(map(int, line.strip().split()))
            report.append(levels)
    res = checkSafe(report)
    print(res)


main()
