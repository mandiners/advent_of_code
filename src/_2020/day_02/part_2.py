def run(input_data):
    """
    690
    """
    result = 0
    for data in input_data:
        policy_rules, password = data.split(': ')
        policy_range, policy_target = policy_rules.split(' ')
        first_index, second_index = [int(i) - 1 for i in policy_range.split('-')]

        target_characters = {password[first_index], password[second_index]}

        if policy_target in target_characters and len(target_characters) == 2:
            result += 1

    return result
