from typing import Dict

FILENAME = "input.txt"
MAGIC_COLOR = "shiny gold"

class Bag_Color:
    def __init__(self, name):
        self.name = name
        self.contains = dict()

    def get_name(self):
        return self.name

    def add_bag(self, color_name, quantity):
        self.contains[color_name] = quantity

    def get_bag_num(self, color_name):
        return self.contains.get(color_name, 0)

    def get_bags(self):
        return self.contains.keys()

    def get_all_items(self):
        return self.contains.items()

def get_input() -> Dict[str, Bag_Color]:
    """Read the file and generate a dictionary of bag color name and
        its Bag_Color object

    Returns:
        Dict[str, Bag_Color]: "Graph" of bags
    """

    bags = dict()

    with open(FILENAME) as f:
        for line in f.readlines():
            line = line.strip()
            container, contains = line.split(" bags contain ")
            container.strip()

            bag_color_obj = Bag_Color(container)

            try: # If ValueError occurs, it will be on very first iteration. So no side effect expected.
                for contain in contains.split(','):
                    contain = contain.split()

                    color_name = " ".join(contain[1:-1]).strip()
                    bag_num = int(contain[0])

                    bag_color_obj.add_bag(color_name, bag_num)

            except ValueError:
                pass

            finally:
                bags[container] = bag_color_obj

    return bags

def has_shiny_gold(
        bag_obj: Bag_Color,
        bag_graph: Dict[str, Bag_Color],
        dp: Dict[str, bool]
    ) -> bool:
    """Check if the bag eventually contains shiny gold (MAGIC_COLOR) bag.
    Used the Dynamic Programming approach.

    Args:
        bag_obj (Bag_Color): Bag to check if it eventually contains shiny gold
        bag_graph (Dict[str, Bag_Color]): Graph of bags
        dp (Dict[str, bool]): Dict of previous results

    Returns:
        bool: True if it eventually contains the shiny gold, otherwise False
    """

    if not bag_obj:
        return False

    if bag_obj.get_name() == MAGIC_COLOR:
        return True

    if bag_obj.get_name() not in dp:
        dp[bag_obj.get_name()] = \
            any( has_shiny_gold(bag_graph[c], bag_graph, dp) for c in bag_obj.get_bags())

    return dp[bag_obj.get_name()]

def part_1():
    bags = get_input()

    shiny_gold_dp = dict()
    count = 0

    for bag_color_obj in bags.values():
        if bag_color_obj.get_name() == MAGIC_COLOR:
            continue

        if has_shiny_gold(bag_color_obj, bags, shiny_gold_dp):
            count += 1

    print(f"There are {count} bags that eventually contain at least one shiny gold bag.")

def part_2():
    bags = get_input()
    total = -1 # shiny gold bag will be counted once

    query = [(1, MAGIC_COLOR)]

    while query:
        num, bag_color_name = query.pop()

        total += num

        for color_name, num_color_bag in bags[bag_color_name].get_all_items():
            query.append((num*num_color_bag, color_name))

    print(f"There are {total} individual bags inside the single shiny gold bag.")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
