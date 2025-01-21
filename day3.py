from typing import List
import re


def calculate(s: str) -> int:
    # Regular expression to match valid mul(X,Y) instructions
    # Matches: mul(digits,digits) where digits are 1-3 characters
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

    # Find all valid matches in the string
    matches = re.finditer(pattern, s)

    total = 0
    for match in matches:
        # Extract the numbers from each valid multiplication
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        # Add the product to the total
        total += num1 * num2

    return total


def main():
    with open(r'd:\adventofcode\day3.txt', 'r') as f:
        mem = f.read()

    mem_clean = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', mem)

    sum_mul = 0
    # for x, y in mem_clean:
    #     sum_mul += int(x) * int(y)

    # print(f'Sum of multiplications: {sum_mul}')

    do_sum = True
    for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', mem):
        match x[0]:
            case 'do()':
                do_sum = True
            case 'don\'t()':
                do_sum = False
            case _:
                if do_sum:
                    sum_mul += int(x[1]) * int(x[2])
    print(f'Sum of multiplications: {sum_mul}')


if __name__ == "__main__":
    main()
