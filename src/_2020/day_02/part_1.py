def run(input_data):
    """
    393
    """
    result = 0
    for data in input_data:
        temp = 0

        policy_rules, password = data.split(': ')
        policy_range, policy_target = policy_rules.split(' ')
        start, end = [int(i) for i in policy_range.split('-')]

        temp += password.count(policy_target)

        if temp in range(start, end + 1):
            result += 1

    return result
