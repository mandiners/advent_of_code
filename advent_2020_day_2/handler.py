def password_validator(input_data):
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


def super_password_validator(input_data):
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
