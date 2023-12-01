import os

from base_solution import BaseSolution


class Solution(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        numbers: list[str] = [
            f"{[char for char in line.strip() if char.isdigit()][0]}"
            f"{[char for char in line.strip() if char.isdigit()][-1]}"
            for line in inputs
        ]
        return sum(list(map(int, numbers)))


if __name__ == "__main__":
    Solution(os.path.abspath(__file__))
