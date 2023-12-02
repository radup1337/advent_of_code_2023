import os

from base_solution import BaseSolution


class SolutionPart1(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        total: int = 0
        rules: dict[str, int] = {"red": 12, "green": 13, "blue": 14}
        for game in inputs:
            is_possible: bool = True
            game_info, cube_info = game.split(":")
            # Get game ID
            game_id = int(game_info.split(" ")[1])
            # Parse cube sets
            cube_sets = cube_info.split(";")
            for cube_set in cube_sets:
                # Parse each number, colour in cube set
                pairs = cube_set.split(",")
                for pair in pairs:
                    number, colour = pair.strip().split(" ")
                    if int(number) > rules[colour]:
                        is_possible = False
                        break
            if is_possible:
                total += game_id
        return total


class SolutionPart2(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        total: int = 0
        # Find max of each in each cube set
        for game in inputs:
            min_cubes: dict[str, int] = {"red": 0, "green": 0, "blue": 0}
            _, cube_info = game.split(":")
            cube_sets: list[str] = cube_info.split(";")
            for cube_set in cube_sets:
                pairs: list[str] = cube_set.split(",")
                for pair in pairs:
                    number, colour = pair.strip().split(" ")
                    if int(number) > min_cubes[colour]:
                        min_cubes[colour] = int(number)

            power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
            total += power

        return total


if __name__ == "__main__":
    current_path: str = os.path.abspath(__file__)
    # ---------------------------------- Part 1 ---------------------------------- #
    part1 = SolutionPart1(current_path, part=1)
    part1.test()
    part1.get_solution()
    # ---------------------------------- Part 2 ---------------------------------- #
    part2 = SolutionPart2(current_path, part=2)
    part2.test()
    part2.get_solution()
