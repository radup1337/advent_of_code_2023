import os

from base_solution import BaseSolution


class Solution(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        total: int = 0
        for line in inputs:
            all_ints: list[str] = [char for char in line.strip() if char.isdigit()]
            joint_number = int(all_ints[0] + all_ints[-1])
            total += joint_number
        return total


if __name__ == "__main__":
    Solution(os.path.abspath(__file__))
