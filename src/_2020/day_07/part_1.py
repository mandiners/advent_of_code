import re
from . import SHINY_GOLD_BAG


def collect_bags(bags, results=None):
    if not results:
        results = set()
    temp = len(results)

    for bag_name, sub_bags in bags.items():
        for sub_bag in sub_bags:
            if sub_bag in results or sub_bag == SHINY_GOLD_BAG:
                results.add(bag_name)
                break

    if temp < len(results):
        return collect_bags(bags, results)
    else:
        return results


def run(input_lines):
    """
    326
    """
    bags = {}

    for line in input_lines:
        bag = re.search("\\w+ \\w+", line).group()
        sub_bags = [i[1] for i in re.findall("(\\d+|no) (\\w+ \\w+|\\w+)", line)]
        bags[bag] = sub_bags

    bar = collect_bags(bags)

    return len(bar)
