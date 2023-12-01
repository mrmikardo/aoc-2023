import os
import re


INPUT_FILENAME = "input"
CURRENT_DIR = os.getcwd()
DIR_NAME = "day_one"

PART_1_RE = re.compile(r"\d")

# Use a lookahead in order to capture overlapping matches i.e. 'eighthree' should return '8' and '3'.
PART_2_RE = re.compile(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))")


def part_1():
    calibration_values = []
    with open(os.path.join(CURRENT_DIR, DIR_NAME, INPUT_FILENAME), "r") as fp:
        obfuscated_calibration_values = fp.read().splitlines()
        for value in obfuscated_calibration_values:
            digits = PART_1_RE.findall(value)
            calibration_value = int(digits[0] + digits[-1])
            calibration_values.append(calibration_value)
    print(f"The sum of all calibration values is: {sum(calibration_values)}")


STRINGS_TO_INTS = {
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


def to_int(v: str) -> str:
    if v.isdigit():
        return v
    else:
        return STRINGS_TO_INTS[v]


def part_2():
    calibration_values = []
    with open(os.path.join(CURRENT_DIR, DIR_NAME, INPUT_FILENAME), "r") as fp:
        obfuscated_calibration_values = fp.read().splitlines()
        for ix, value in enumerate(obfuscated_calibration_values):
            matches = PART_2_RE.finditer(value)
            digits = list(map(to_int, [match.group(1) for match in matches]))
            calibration_value = int(f"{digits[0]}{digits[-1]}")
            calibration_values.append(calibration_value)
    print(f"The sum of all calibration values is: {sum(calibration_values)}")
