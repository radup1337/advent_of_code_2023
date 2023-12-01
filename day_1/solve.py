import os

from base_solution import BaseSolution


class SolutionPart1(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        total: int = 0
        for line in inputs:
            all_ints: list[str] = [char for char in line.strip() if char.isdigit()]
            joint_number = int(all_ints[0] + all_ints[-1])
            total += joint_number
        return total


class SolutionPart2(BaseSolution):
    def __init__(self, current_path: str, part: int, test_solution: str) -> None:
        super().__init__(current_path, part, test_solution)
        self.word_to_int = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }

    def solve(self, inputs: list[str]) -> int:
        total: int = 0
        for line in inputs:
            number = self.find_numbers(line.strip())
            total += int(number)
        return total

    def find_numbers(self, line: str) -> int:
        first_number = self.search(line, 1)
        last_number = self.search(line[::-1], -1)
        assert first_number and last_number
        return int(first_number + last_number)

    def search(self, line: str, reverse: int) -> str | None:
        i: int = 0
        search_line: str = ""
        while i < len(line):
            if line[i].isdigit():
                return line[i]
            search_line += line[i]
            for word in self.word_to_int:
                if word in search_line[::reverse]:
                    return self.word_to_int[word]
            i += 1
        return None


if __name__ == "__main__":
    path = os.path.abspath(__file__)
    # ---------------------------------- Part 1 ---------------------------------- #
    part1 = SolutionPart1(current_path=path, part=1, test_solution="142")
    part1.test()
    part1.get_solution()
    # ---------------------------------- Part 2 ---------------------------------- #
    part2 = SolutionPart2(current_path=path, part=2, test_solution="281")
    part2.test()
    part2.get_solution()
