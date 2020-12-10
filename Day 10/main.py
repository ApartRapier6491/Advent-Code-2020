from typing import List, Set
from collections import defaultdict

FILENAME = "input.txt"

def get_input() -> List[int]:
    lines = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            lines.append(int(line))

    return lines

def part_1():
    jolt_set = set(get_input())
    jolt_difference_1_count = 0
    jolt_difference_3_count = 1 # Counted one for the difference between device and highest-rated adapter
    curr_num = 0

    while jolt_set:
        if curr_num+1 in jolt_set:
            jolt_difference_1_count += 1
            jolt_set.remove(curr_num + 1)
            curr_num += 1

        elif curr_num+2 in jolt_set:
            jolt_set.remove(curr_num + 2)
            curr_num += 2

        elif curr_num+3 in jolt_set:
            jolt_difference_3_count += 1
            jolt_set.remove(curr_num + 3)
            curr_num += 3

        else:
            print("This is impossible!")
            return

    print("The number of 1-jolt differences multiplied by the number of 3-jolt differences is "
        f"{jolt_difference_1_count * jolt_difference_3_count}")

def dp_part_2(n: int, jolt_set: Set[int], dp: List[int]) -> int:
    if n not in jolt_set:
        return 0

    if n not in dp:
        dp[n] = dp_part_2(n+1, jolt_set, dp) + \
            dp_part_2(n+2, jolt_set, dp) + \
            dp_part_2(n+3, jolt_set, dp)

    return dp[n]

def part_2():
    jolt_set = set(get_input())
    dp = defaultdict(int)

    jolt_set.add(0)
    dp[max(jolt_set)] = 1

    dp_part_2(0, jolt_set, dp)

    print(f"The total number of distinct ways you can arrange the adapters is {dp[0]}")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
