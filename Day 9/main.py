from typing import List

FILENAME = "input.txt"

def get_input() -> List[int]:
    lines = list()

    with open(FILENAME) as f:
        for line in f.readlines():
            lines.append(int(line))

    return lines

def part_1():
    nums = get_input()

    xmas = set(nums[:25])

    count = 0

    for i in range(25, len(nums)):
        for xn in xmas:
            if nums[i]-xn in xmas:
                break

        else:
            print(f"The first number that does not have this property is {nums[i]}")
            return

        xmas.remove(nums[i-25])
        xmas.add(nums[i])

    print("Something went wrong!")

def part_2():
    nums = get_input()

    goal_num = 21806024 # Answer obtained from part 1

    sub_sum = 0
    i, j = 0, 0

    while j < len(nums):
        if sub_sum < goal_num:
            sub_sum += nums[j]
            j += 1

        elif sub_sum > goal_num:
            sub_sum -= nums[i]
            i += 1

        else:
            min_sub_nums = min(nums[i:j])
            max_sub_nums = max(nums[i:j])

            print(f"The encryption weakness in your XMAS-encrypted list of numbers is {min_sub_nums + max_sub_nums}")
            return

    print("Something went wrong!")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
