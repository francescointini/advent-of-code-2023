import os
import re
from typing import List, Tuple


def get_file_path(filename: str) -> str:
    return os.path.join(os.path.dirname(__file__), "inputs", filename)


def find_candidate_indices(
    line: str, spelled_numbers: List[str]
) -> Tuple[Tuple[str, int], Tuple[str, int]]:
    candidate_first = ("", float("inf"))
    candidate_last = ("", -1)

    for sub in filter(lambda x: x in line, spelled_numbers):
        sub_indexes = [idx for idx in range(len(line)) if line.startswith(sub, idx)]
        for idx in sub_indexes:
            if idx < candidate_first[1]:
                candidate_first = (sub, idx)
            if idx > candidate_last[1]:
                candidate_last = (sub, idx)

    return candidate_first, candidate_last


def main() -> None:
    result: int = 0
    spelled_numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    with open(get_file_path("1.txt"), "r") as f:
        for line in f:
            calibration: str = ""

            candidate_first, candidate_last = find_candidate_indices(
                line, spelled_numbers
            )

            if first_match := re.search(r"\d", line):
                number_match = first_match.group()
                calibration += (
                    str(spelled_numbers.index(candidate_first[0]) + 1)
                    if candidate_first[1] < line.index(number_match)
                    else number_match
                )
            else:
                calibration += str(spelled_numbers.index(candidate_first[0]) + 1)

            if last_match := re.search(r"\d(?=[^\d]*$)", line):
                number_match = last_match.group()
                last_index = len(line) - line[::-1].index(number_match) - 1
                calibration += (
                    str(spelled_numbers.index(candidate_last[0]) + 1)
                    if candidate_last[1] > last_index
                    else number_match
                )
            else:
                calibration += str(spelled_numbers.index(candidate_last[0]) + 1)

            result += int(calibration)

    print("Result:", result)


if __name__ == "__main__":
    main()
