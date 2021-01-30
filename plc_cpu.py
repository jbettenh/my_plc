import json
import os
import random
import socket


def main():
    ip = "192.168.2.2"

    print(f'{ip:<15} | {valid_ip4_addr(ip)}')


def load_config():
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, 'config.json')

    if not os.path.exists(filename):
        return {}

    with open(filename, 'r', encoding='utf-8') as fin:
        return json.load(fin)


def valid_ip4_addr(ip: str) -> bool:
    try:
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except socket.error:
        return False


if __name__ == '__main__':
    main()
