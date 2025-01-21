class Solution:
    def __init__(self):
        self.d = 3
        self.safe = 0

    def is_desc(self, arr):
        for i in range(len(arr)-1):
            if arr[i] - self.d > arr[i+1]:
                return False
        return True

    def is_asc(self, arr):
        for i in range(len(arr)-1):
            if arr[i] + self.d < arr[i+1]:
                return False
        return True

    def is_safe(self, list):
        self.safe = 0
        for arr in list:
            if self.is_desc(arr) or self.is_asc(arr):
                self.safe += 1
        return self.safe


def main():
    solution = Solution()

    # Read the input from 'input.txt'
    with open("day2.txt", "r") as file:
        lines = file.readlines()

    # Parse the input lines into a list of lists
    input_data = []
    for line in lines:
        # Convert the line into a list of integers
        input_data.append(list(map(int, line.strip().split())))
    # Pass the parsed data to the is_safe method
    solution.is_safe(input_data)

    # Print the result
    print("Safe arrays:", solution.safe)


main()
