import json
import os
import random
import socket
import xml.etree.ElementTree as ET


def main():
    ip = "192.168.2.2"

    print(f'{ip:<15} | {valid_ip4_addr(ip)}')
    create_xml()
    print(f'Writing xml...')


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


def create_xml():
    data = ET.Element('data')
    head = ET.SubElement(data, 'head')
    main_result = ET.SubElement(data, 'main_result')
    part_results = ET.SubElement(main_result, 'part_results')
    measurements = ET.SubElement(part_results, 'measurements')

    head.set('name', 'head')
    main_result.set('name', 'main')
    part_results.set('name', 'part')
    measurements.set('name', 'measurement')

    head.text = 'item1abc'
    main_result.text = 'T_0001'
    part_results.text = '100'
    measurements.text = '1'

    mydata = ET.tostring(data)
    myfile = open('qal_results.xml', 'wb')
    myfile.write(mydata)


if __name__ == '__main__':
    main()
