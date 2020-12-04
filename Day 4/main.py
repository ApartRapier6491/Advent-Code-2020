from typing import List, NamedTuple
import re

FILENAME = "input.txt"

class Height(NamedTuple):
    measurement: int
    unit: str

class Passport():
    def __init__(self,
        byr: int, iyr: int, eyr: int, hgt: Height,
        hcl: str, ecl: str, pid: str
    ):
        self.byr = byr # Birth Year
        self.iyr = iyr # Issue Year
        self.eyr = eyr # Expiration Year
        self.hgt = hgt # Height
        self.hcl = hcl # Hair Color
        self.ecl = ecl # Eye Color
        self.pid = pid # Passport ID

    def is_valid(self) -> bool:
        if not (1920 <= self.byr <= 2002):
            return False

        if not (2010 <= self.iyr <= 2020):
            return False

        if not (2020 <= self.eyr <= 2030):
            return False

        measurement, unit = self.hgt
        if unit == "cm":
            if not (150 <= measurement <= 193):
                return False
        elif unit == "in":
            if not (59 <= measurement <= 76):
                return False
        else:
            return False

        if not re.fullmatch(r"\#[0-9a-f]{6}", self.hcl):
            return False

        if self.ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            return False

        if not re.fullmatch(r"\d{9}", self.pid):
            return False

        return True

def parse_passport(passport_string: str) -> Passport:
    """ Take in string and parse it into Passport object

    Args:
        passport_string (str): A string of single passport

    Raises:
        KeyError: If any field is missing
        ValueError: If any data conversions fails

    Returns:
        Passport: A passport object
    """
    fields = passport_string.split()

    fields_dict = dict()

    for field in fields:
        field_name, field_value = field.split(":")
        fields_dict[field_name] = field_value

    # Check if these key exists If not, throw KeyError. These keys all must exist.
    if not (
        "byr" in fields_dict and \
        "iyr" in fields_dict and \
        "eyr" in fields_dict and \
        "hgt" in fields_dict and \
        "hcl" in fields_dict and \
        "ecl" in fields_dict and \
        "pid" in fields_dict
    ):
        raise KeyError

    # Parse them to Passport class. Throw ValueError if any conversion fails
    return Passport(
        int(fields_dict["byr"]),
        int(fields_dict["iyr"]),
        int(fields_dict["eyr"]),
        Height(int(fields_dict["hgt"][:-2]), fields_dict["hgt"][-2:]),
        fields_dict["hcl"],
        fields_dict["ecl"],
        fields_dict["pid"]
    )

def get_input() -> List[str]:
    """ Read the file and generate a list of passport strings

    Returns:
        [List[str]]: A list of passport strings
    """
    passports = list()

    with open(FILENAME) as f:
        passport = list()

        for line in f.readlines():
            if line == "\n":
                passport_text = " ".join(passport)
                passport = list()

                passports.append(passport_text)

            else:
                passport.append(line.strip())

        passport_text = " ".join(passport)

        passports.append(passport_text)

    return passports

def part_1():
    passport_strings = get_input()
    count = 0

    for passport_string in passport_strings:
        try:
            parse_passport(passport_string)

        except KeyError:
            continue

        except ValueError:
            pass

        count += 1

    print(f"There are {count} valid passport")

def part_2():
    passport_strings = get_input()
    count = 0

    for passport_string in passport_strings:
        try:
            if parse_passport(passport_string).is_valid():
                count += 1

        except (KeyError, ValueError):
            pass

    print(f"There are {count} valid passport")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
