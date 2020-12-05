import argparse


def z_fill(value):
    return value.zfill(2)


def input_loader(path):
    with open(path, 'r') as file:
        return file.readlines()


def format_data(raw_data):
    return [i.rstrip() for i in raw_data]


def get_args():
    parser_object = argparse.ArgumentParser(description='Advent of Code')
    parser_object.add_argument('year', type=str, help='Input year')
    parser_object.add_argument('day', type=z_fill, help='Input day')
    parser_object.add_argument('part', type=str, help='Input part')

    return parser_object.parse_args()
