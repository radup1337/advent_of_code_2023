from abc import abstractmethod
import os
from typing import Any


class BaseSolution:
    def __init__(self, current_path: str) -> None:
        self.__current_folder: str = os.path.dirname(current_path)
        self.__input_path: str = os.path.join(self.__current_folder, "input.txt")
        self.__get_solution()

    def __process_inputs(self) -> list[str]:
        with open(self.__input_path, "r", encoding="utf-8") as file:
            inputs = file.readlines()
            return inputs

    def __get_solution(self) -> None:
        inputs: list[str] = self.__process_inputs()

        # Solve
        solution = str(self.solve(inputs))

        # Writing the solution to solution.txt
        solution_path: str = os.path.join(self.__current_folder, "solution.txt")
        with open(solution_path, "w") as file:
            file.write(solution)

    @abstractmethod
    def solve(self, inputs: list[str]) -> Any:
        ...
