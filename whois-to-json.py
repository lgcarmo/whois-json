#!/usr/bin/env python3

import argparse
import json
import sys

def parse_whois(raw_data):
    whois_data = {}
    lines = raw_data.split('\n')
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            whois_data[key] = value
    return whois_data

def main():
    parser = argparse.ArgumentParser(description='Convert raw WHOIS data to JSON.')
    parser.add_argument('-f', '--file', help='Input file with raw WHOIS data')
    parser.add_argument('-o', '--output', required=True, help='Output file for JSON data')
    
    args = parser.parse_args()

    # Ler dados brutos do WHOIS do arquivo ou da entrada padrão
    if args.file:
        with open(args.file, 'r') as file:
            raw_data = file.read()
    else:
        raw_data = sys.stdin.read()

    # Parsear dados e converter para JSON
    whois_data = parse_whois(raw_data)
    whois_json = json.dumps(whois_data, indent=4)

    # Salvar JSON em um arquivo
    with open(args.output, 'w') as file:
        file.write(whois_json)

    # Imprimir JSON na tela
    print(whois_json)

if __name__ == "__main__":
    main()
