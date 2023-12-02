import re, os


def main() -> None:
    result: int = 0
    file_path: str = os.path.join(os.path.dirname(__file__)) + "/inputs/1.txt"

    with open(file_path, "r") as f:
        for line in f.readlines():
            calibration: str = ""
            if first_match := re.search(r"\d", line):
                calibration += first_match.group()
            if last_match := re.search(r"\d(?=[^\d]*$)", line):
                calibration += last_match.group()
            result += int(calibration)

    print("Result: ", result)


if __name__ == "__main__":
    main()
