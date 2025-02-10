def read_input(file_path):
    """
    Reads a single line of numbers from the given file and converts it to a list of integers.
    """
    with open(file_path, "r") as file:
        return [int(x) for x in file.readline().strip()]


def calculate_sum(values):
    """
    Processes the list of values based on the given logic and returns the computed sum.
    """
    total_sum = 0
    block_count = 0
    last_index = len(values) - 1

    for i, value in enumerate(values):
        if i % 2 == 0:
            for _ in range(value):
                total_sum += (i // 2) * block_count
                block_count += 1
        elif last_index > i:
            for _ in range(value):
                while last_index > i and values[last_index] == 0:
                    last_index -= 2
                if last_index <= i:
                    break
                total_sum += (last_index // 2) * block_count
                block_count += 1
                values[last_index] -= 1

    return total_sum


def parse_disk_data(disk_data):
    """Parse the input string into a list of disk blocks."""
    disk_blocks = []
    for i, size in enumerate(disk_data):
        if i % 2 == 0:
            disk_blocks.append((i // 2, size))
        else:
            disk_blocks.append((-1, size))
    return disk_blocks


def find_suitable_space(disk_blocks, current_index, block_size):
    """Find a suitable free space for the current block."""
    for j in range(current_index):
        free_id, free_size = disk_blocks[j]
        if free_id == -1 and free_size >= block_size:
            return j
    return -1


def rearrange_blocks(disk_blocks, current_index, new_index, block_id, block_size):
    """Rearrange blocks to fit the current block into the found free space."""
    _, remaining_free_space = disk_blocks[new_index]
    return (
        disk_blocks[:new_index]
        + [(block_id, block_size), (-1, remaining_free_space - block_size)]
        + disk_blocks[new_index + 1:current_index]
        + [(-1, block_size)]
        + disk_blocks[current_index + 1:]
    )


def optimize_disk_layout(disk_blocks):
    """Rearrange blocks to optimize disk space."""
    current_index = len(disk_blocks) - 1
    while current_index > 0:
        block_id, block_size = disk_blocks[current_index]
        if block_id == -1:
            current_index -= 1
            continue

        new_index = find_suitable_space(disk_blocks, current_index, block_size)
        if new_index == -1:
            current_index -= 1
            continue

        disk_blocks = rearrange_blocks(
            disk_blocks, current_index, new_index, block_id, block_size)

    return disk_blocks


def calculate_total_sum(disk_blocks):
    """Calculate the final result based on rearranged blocks."""
    total_sum = 0
    accumulated_free_space = 0

    for block_id, block_size in disk_blocks:
        if block_id == -1:
            accumulated_free_space += block_size
            continue

        for _ in range(block_size):
            total_sum += accumulated_free_space * block_id
            accumulated_free_space += 1

    return total_sum


def main():
    file_path = r"d:\adventofcode\day9.txt"
    values = read_input(file_path)
    result = calculate_sum(values)
    print(result)

    data = read_input(file_path)
    disk_blocks = parse_disk_data(data)
    optimized_blocks = optimize_disk_layout(disk_blocks)
    result = calculate_total_sum(optimized_blocks)
    print(result)


if __name__ == "__main__":
    main()
