import ipaddress
import json
import os
import random
import socket


def main():
    print('Success')


def load_config():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'config.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


if __name__ == '__main__':
    main()
