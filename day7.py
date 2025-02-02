from typing import List


def check(target: int, candidates: List[int], current: int, idx: int) -> bool:
    if current > target:
        return False
    if idx == len(candidates):
        return current == target
    return check(target, candidates, current + candidates[idx], idx + 1) or check(target, candidates, current * candidates[idx], idx + 1)


def check2(target: int, candidates: List[int], current: int, idx: int) -> bool:
    if current > target:
        return False
    if idx == len(candidates):
        return current == target
    num = candidates[idx]
    return check2(target, candidates, current + num, idx + 1) or check2(target, candidates, current * num, idx + 1) or check2(target, candidates, int(str(current) + str(num)), idx + 1)


def main():

    with open(r'd:\adventofcode\day7.txt', 'r') as file:
        res = 0
        for line in file:
            parts = line.strip().split(':')
            target = int(parts[0])
            candidates = [int(x) for x in parts[1].split()]

            if (check2(target, candidates, candidates[0], 1)):
                res += target

        print(res)


if __name__ == "__main__":
    main()
