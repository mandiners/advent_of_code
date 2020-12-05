def run(input_data):
    """
    393
    """
    results = 0
    for data in input_data:
        policy_rules, password = [i for i in data.split(': ')]
        policy_range, policy_target = policy_rules.split(' ')
        policy_range = policy_range.split('-')
        temp = 0
        for char in password:
            if policy_target == char:
                temp += 1

        if temp in range(int(policy_range[0]), int(policy_range[1]) + 1):
            results += 1

    return results
