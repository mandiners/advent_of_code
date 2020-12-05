def run(input_data):
    """
    690
    """
    results = 0
    for data in input_data:
        policy_rules, password = [i for i in data.split(': ')]
        policy_range, policy_target = policy_rules.split(' ')
        first, second = [int(i) - 1 for i in policy_range.split('-')]
        temp = 0
        for char in (password[first], password[second]):
            if char == policy_target:
                temp += 1

        if temp == 1:
            results += 1

    return results
