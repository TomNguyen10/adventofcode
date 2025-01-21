from typing import List
from collections import Counter


def calculate(a: List[int], b: List[int]) -> int:
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += abs(a[i] - b[i])
    return res


def similarity(a: List[int], b: List[int]) -> int:
    freqA = Counter(a)
    freqB = Counter(b)
    res = 0
    for num in freqA:
        res += num * freqB[num]
    return res


def main():
    a = []
    b = []
    with open(r'd:\adventofcode\day1.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            num1, num2 = map(int, line.strip().split())
            a.append(num1)
            b.append(num2)

    result1 = calculate(a, b)
    result2 = similarity(a, b)
    print(result2)


if __name__ == "__main__":
    main()
