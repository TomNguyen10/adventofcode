def findInvalid(nums, i, rule):
    v = nums[i]
    if v not in rule:
        return -1
    for j in range(i):
        if nums[j] in rule[v]:
            return j
    return -1


def mySort(nums, rule, step=0):
    p = -1
    for i in range(len(nums)):
        p = findInvalid(nums, i, rule)
        if p != -1:
            nums = nums[:p] + [nums[i]] + nums[p:i] + nums[i+1:]
            break
    if p == -1:
        return nums
    return mySort(nums, rule, step+1)


def process(nums, rule):
    read = set()
    for n in nums:
        if n in rule and len(rule[n].intersection(read)) > 0:
            return 0
        read.add(n)
    return nums[len(nums) // 2]


def main():
    rule = {}

    with open("day5.txt", "r") as file:
        lines = file.readlines()

    index = 0
    while index < len(lines) and lines[index].strip():
        a, b = map(int, lines[index].strip().split("|"))
        if a not in rule:
            rule[a] = set()
        rule[a].add(b)
        index += 1

    index += 1
    total_sum = 0

    while index < len(lines):
        nums = list(map(int, lines[index].strip().split(",")))
        points = process(nums, rule)
        if points != 0:
            index += 1
            continue
        nums = mySort(nums, rule)
        total_sum += process(nums, rule)
        index += 1

    print(total_sum)


if __name__ == "__main__":
    main()
