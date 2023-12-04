import os

from base_solution import BaseSolution


class SolutionPart1(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        # Hardcoded symbols, had to first parse the input to see what symbols were used but that's trivial
        all_symbols = {"%", "#", "@", "*", "&", "-", "$", "=", "/", "+"}
        indexes_found = []
        total: int = 0
        for i, line in enumerate(inputs):
            line = line.strip()
            for j, char in enumerate(line):
                # Get rid of \n and spaces
                char = char.strip()
                if char not in all_symbols:
                    continue
                # Go through all the neighbours
                for k in range(-1, 2):
                    # Check if we are at the edge vertically
                    if (i == 0 and k == -1) or (i == len(inputs) - 1 and k == 1):
                        continue
                    for l in range(-1, 2):
                        # Check if we are at the edge horizontally
                        if (j == 0 and l == -1) or (j == len(line) - 1 and l == 1):
                            continue
                        pos_i = i + k
                        pos_j = j + l
                        if not inputs[pos_i][pos_j].isdigit():
                            continue
                        # Construct the number by going backwards and forwards
                        create_number = inputs[pos_i][pos_j]
                        # Keep track of the indexes we have already seen to not double count
                        indexes_found.append((pos_i, pos_j))
                        found_before = False
                        # Parse backwards
                        for x in range(pos_j - 1, 0 - 1, -1):
                            if (pos_i, x) in indexes_found:
                                found_before = True
                                break
                            dig = inputs[pos_i][x]
                            if dig.isdigit():
                                create_number = dig + create_number
                                indexes_found.append((pos_i, x))
                            else:
                                break
                        # Parse forwards
                        for x in range(pos_j + 1, len(inputs[pos_i])):
                            if (pos_i, x) in indexes_found:
                                found_before = True
                                break
                            dig = inputs[pos_i][x]
                            if dig.isdigit():
                                create_number = create_number + dig
                                indexes_found.append((pos_i, x))
                            else:
                                break
                        # If we have already seen this number, skip it
                        if found_before:
                            continue
                        # Add the number to the total
                        total += int(create_number)
        return total


class SolutionPart2(BaseSolution):
    def solve(self, inputs: list[str]) -> int:
        # For the most part very similar to part 1
        indexes_found: list[tuple[int, int]] = []
        total: int = 0
        for i, line in enumerate(inputs):
            line = line.strip()
            for j, char in enumerate(line):
                char = char.strip()
                if char != "*":
                    continue
                # Have to keep track of part numbers found
                numbers_found = []
                for k in range(-1, 2):
                    if (i == 0 and k == -1) or (i == len(inputs) - 1 and k == 1):
                        continue
                    for l in range(-1, 2):
                        if (j == 0 and l == -1) or (j == len(line) - 1 and l == 1):
                            continue
                        pos_i = i + k
                        pos_j = j + l
                        if not inputs[pos_i][pos_j].isdigit():
                            continue
                        create_number = inputs[pos_i][pos_j]
                        indexes_found.append((pos_i, pos_j))
                        found_before = False
                        for x in range(pos_j - 1, 0 - 1, -1):
                            if (pos_i, x) in indexes_found:
                                found_before = True
                                break
                            dig = inputs[pos_i][x]
                            if dig.isdigit():
                                create_number = dig + create_number
                                indexes_found.append((pos_i, x))
                            else:
                                break
                        for x in range(pos_j + 1, len(inputs[pos_i])):
                            if (pos_i, x) in indexes_found:
                                found_before = True
                                break
                            dig = inputs[pos_i][x]
                            if dig.isdigit():
                                create_number = create_number + dig
                                indexes_found.append((pos_i, x))
                            else:
                                break
                        if found_before:
                            continue
                        numbers_found.append(int(create_number))
                # If we found exactly 2 part numbers, calculate gear ratio and add it to the total
                if len(numbers_found) == 2:
                    gear_ratio = numbers_found[0] * numbers_found[1]
                    total += gear_ratio
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
