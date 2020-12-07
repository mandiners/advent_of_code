def run(input_lines):
    """
    7027
    """
    counts = 0
    group_answers = set()
    lines = input_lines if input_lines[-1] is None else [*input_lines, *[None]]

    for form in lines:
        if form:
            for answer in form:
                group_answers.add(answer)
        else:
            counts += len(group_answers)
            group_answers = set()

    return counts
