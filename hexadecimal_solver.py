import argparse
import sys
import re

def is_hex_string(s):
    # Accepts strings with or without 0x prefix, case-insensitive
    s = s.strip()
    if s.lower().startswith('0x'):
        s = s[2:]
    return bool(re.fullmatch(r'[0-9a-fA-F]+', s))

def hex_to_base10(s):
    s = s.strip()
    if s.lower().startswith('0x'):
        s = s[2:]
    return int(s, 16)

def main():
    parser = argparse.ArgumentParser(description="Hexadecimal to Base10 converter.")
    parser.add_argument('-t', '--text', type=str, help='Input string to check/convert (if not provided, will prompt)')
    args = parser.parse_args()

    if args.text:
        input_str = args.text
    else:
        input_str = input("Enter a string: ")

    if is_hex_string(input_str):
        base10 = hex_to_base10(input_str)
        print(f"Hexadecimal '{input_str}' is {base10} in base 10.")
    else:
        print(f"'{input_str}' is not a valid hexadecimal string.")

if __name__ == "__main__":
    main()
