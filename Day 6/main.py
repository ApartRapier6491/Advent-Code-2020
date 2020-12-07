from typing import List

FILENAME = "input.txt"

def get_input() -> List[List[str]]:
    """ Read the file and generate a list of seat strings

    Returns:
        [List[str]]: A list of seat strings
    """
    groups = list()
    questions = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            if not line.strip():
                groups.append(questions)
                questions = list()

            else:
                questions.append(line.strip())

    groups.append(questions)

    return groups

def part_1():
    groups = get_input()
    count = 0

    for group in groups:
        count += len(set("".join(group)))

    print(f"The sum of those counts is {count}")

def part_2():
    groups = get_input()
    count = 0

    for group in groups:
        question_set = set(group[0])

        for questions in group[1:]:
            question_set = question_set.intersection(set(questions))

        count += len(question_set)

    print(f"The sum of those counts is {count}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
