from abc import abstractmethod
import os
from typing import Any


class BaseSolution:
    def __init__(self, current_path: str, part: int, test_solution: str) -> None:
        self.__current_folder: str = os.path.dirname(current_path)
        self.__input_path: str = os.path.join(self.__current_folder, "input.txt")
        self.__test_input_path: str = os.path.join(self.__current_folder, f"test_input_{part}.txt")
        self.__test_solution: str = test_solution
        self.__part: int = part

    def __process_inputs(self, input_path: str) -> list[str]:
        with open(input_path, "r", encoding="utf-8") as file:
            inputs = file.readlines()
            return inputs

    def get_solution(self) -> None:
        inputs: list[str] = self.__process_inputs(self.__input_path)
        # Solve
        solution = str(self.solve(inputs))
        print(f"Solution: {solution}")
        # Writing the solution to solution.txt
        solution_path: str = os.path.join(self.__current_folder, f"solution_{self.__part}.txt")
        with open(solution_path, "w") as file:
            file.write(solution)

    def test(self) -> None:
        inputs: list[str] = self.__process_inputs(self.__test_input_path)
        solution = str(self.solve(inputs))
        assert solution == self.__test_solution, f"Expected {self.__test_solution}, got {solution}"

    @abstractmethod
    def solve(self, inputs: list[str]) -> Any:
        ...
