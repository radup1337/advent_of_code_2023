import os

from base_solution import BaseSolution

# Hated today, not my solution for part 2


class SolutionPart1(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        total: int = 0
        for card in inputs:
            points = 1 / 2
            numbers = card.split(":")[1]
            win, mine = numbers.strip().split("|")
            winning_numbers = [x for x in win.split(" ") if x.isnumeric()]
            my_numbers = [x for x in mine.split(" ") if x.isnumeric()]

            for number in my_numbers:
                if number in winning_numbers:
                    points *= 2
            total += int(points)

        return total


class SolutionPart2(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        cards: list[int] = [1] * len(inputs)
        for index, card in enumerate(inputs):
            _, numbers = card.split(":")
            win, mine = numbers.strip().split("|")
            winning_numbers: list[str] = [x for x in win.split(" ") if x.isnumeric()]
            my_numbers: list[str] = [x for x in mine.split(" ") if x.isnumeric()]

            winning_cards: int = len(set(winning_numbers) & set(my_numbers))
            for i in range(winning_cards):
                cards[index + i + 1] += cards[index]

        return sum(cards)


if __name__ == "__main__":
    current_path: str = os.path.abspath(__file__)
    # ---------------------------------- Part 1 ---------------------------------- #
    part1 = SolutionPart1(current_path, part=1)
    part1.test()
    part1.get_solution()
    # # ---------------------------------- Part 2 ---------------------------------- #
    part2 = SolutionPart2(current_path, part=2)
    part2.test()
    part2.get_solution()
