import argparse
import sys
import re
import base64

def is_hex_string(s):
    s = s.strip()
    if s.lower().startswith('0x'):
        s = s[2:]
    return bool(re.fullmatch(r'[0-9a-fA-F]+', s))

def hex_to_base10(s):
    s = s.strip()
    if s.lower().startswith('0x'):
        s = s[2:]
    return int(s, 16)

def base10_to_binary(s):
    try:
        n = int(s)
        return bin(n)[2:]
    except ValueError:
        return None

def base64_to_utf8(s):
    try:
        decoded_bytes = base64.b64decode(s)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return None

def main():
    parser = argparse.ArgumentParser(description="General base converter.")
    parser.add_argument('-m', '--mode', type=str, choices=['hex2dec', 'dec2bin', 'b64tostr'], help='Conversion mode')
    parser.add_argument('-t', '--text', type=str, help='Input string to convert (if not provided, will prompt)')
    args = parser.parse_args()

    if not args.mode:
        print("Select conversion mode:")
        print("1. Hexadecimal to Base10")
        print("2. Base10 to Binary")
        print("3. Base64 to UTF-8 String")
        mode_input = input("Enter 1, 2, or 3: ").strip()
        if mode_input == '1':
            args.mode = 'hex2dec'
        elif mode_input == '2':
            args.mode = 'dec2bin'
        elif mode_input == '3':
            args.mode = 'b64tostr'
        else:
            print("Invalid selection.")
            sys.exit(1)

    if args.text:
        input_str = args.text
    else:
        input_str = input("Enter a string to convert: ")

    if args.mode == 'hex2dec':
        if is_hex_string(input_str):
            base10 = hex_to_base10(input_str)
            print(f"Hexadecimal '{input_str}' is {base10} in base 10.")
        else:
            print(f"'{input_str}' is not a valid hexadecimal string.")
    elif args.mode == 'dec2bin':
        binary = base10_to_binary(input_str)
        if binary is not None:
            print(f"Base10 '{input_str}' is {binary} in binary.")
        else:
            print(f"'{input_str}' is not a valid base10 integer.")
    elif args.mode == 'b64tostr':
        utf8 = base64_to_utf8(input_str)
        if utf8 is not None:
            print(f"Base64 '{input_str}' decodes to: {utf8}")
        else:
            print(f"'{input_str}' is not valid base64 or not valid UTF-8.")

if __name__ == "__main__":
    main()
