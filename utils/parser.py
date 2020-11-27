# handling input

def input_parser(path):
    with open(path, 'r') as file:
        return file.readlines()


def formatter(raw_data):
    return [i.rstrip() for i in raw_data]
