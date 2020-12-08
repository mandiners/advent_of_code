import functools
import re
from . import SHINY_GOLD_BAG


def collect_bags_in_shiny_gold_bag(bag, bags, results=None, multiplier=1):
    if not results:
        results = []

    for name, value in bag.items():
        result = int(value) * multiplier
        results.append(result)

        if value:
            collect_bags_in_shiny_gold_bag(
                bags[name],
                bags,
                results,
                result
            )

    return results


def run(input_lines):
    """
    5635
    """
    bags = {}

    for line in input_lines:
        bag = re.search("\\w+ \\w+", line).group()
        sub_bags = {i[1]: int(i[0]) if i[0] != 'no' else 0
                    for i in re.findall("(\\d+|no) (\\w+ \\w+|\\w+)", line)}
        bags[bag] = sub_bags

    find_bags = collect_bags_in_shiny_gold_bag(
        bags[SHINY_GOLD_BAG],
        bags
    )

    return functools.reduce(lambda a, b: a + b, find_bags)
