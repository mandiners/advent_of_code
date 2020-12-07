import functools
from collections import defaultdict


def run(input_lines):
    """
    3579
    """
    lines = input_lines if input_lines[-1] is None else [*input_lines, *[None]]
    counts = []
    group_answers = defaultdict(int)
    persons_in_group = 0

    for form in lines:
        if form:
            persons_in_group += 1
            for answer in form:
                group_answers[answer] += 1
        else:
            total_agreement = 0
            for answers in group_answers.values():
                if answers == persons_in_group:
                    total_agreement += 1
            if total_agreement:
                counts.append(total_agreement)

            group_answers = defaultdict(int)
            persons_in_group = 0

    return functools.reduce(lambda a, b: a + b, counts)
