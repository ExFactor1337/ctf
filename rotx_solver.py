import re
import os
import sys
import argparse

def rotX(text, x):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            offset = ord('a')
            result.append(chr((ord(char) - offset + x) % 26 + offset))
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            result.append(chr((ord(char) - offset + x) % 26 + offset))
        else:
            result.append(char)
    return ''.join(result)

def load_dictionary(dict_path):
    if not os.path.isfile(dict_path):
        print(f"Dictionary file '{dict_path}' not found.")
        sys.exit(1)
    with open(dict_path, 'r', encoding='utf-8', errors='ignore') as f:
        return set(word.strip().lower() for word in f if word.strip())

def count_common_words(text, dictionary):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return sum(1 for word in words if word in dictionary)

def main():
    parser = argparse.ArgumentParser(description="ROT-X solver with dictionary matching.")
    parser.add_argument('-r', '--rot', type=int, help='Specific ROT integer to use (1-25)')
    parser.add_argument('-d', '--dict', type=str, default='/usr/share/dict/words', help='Dictionary file path')
    parser.add_argument('-t', '--text', type=str, help='Text to decode (if not provided, will prompt)')
    args = parser.parse_args()

    dict_path = args.dict
    dictionary = load_dictionary(dict_path)

    if args.text:
        input_str = args.text
    else:
        input_str = input("Enter a string: ")

    # Check if any input word is in the dictionary
    input_words = re.findall(r"[a-zA-Z']+", input_str.lower())
    found_words = [word for word in input_words if word in dictionary]
    if found_words and not args.rot:
        print(f"Some input words found in dictionary: {', '.join(found_words)}")
        resp = input("Do you want to translate into a specific ROT? (y/n): ").strip().lower()
        if resp == 'y':
            while True:
                rot_val = input("Enter ROT integer (1-25): ").strip()
                if rot_val.isdigit() and 1 <= int(rot_val) <= 25:
                    args.rot = int(rot_val)
                    break
                else:
                    print("Please enter a valid integer between 1 and 25.")

    if args.rot:
        if not (1 <= args.rot <= 25):
            print("ROT integer must be between 1 and 25.")
            sys.exit(1)
        decoded = rotX(input_str, args.rot)
        count = count_common_words(decoded, dictionary)
        print(f"ROT{args.rot}: {decoded} (dictionary words: {count})")
    else:
        best_matches = []
        max_count = 0
        for x in range(1, 26):
            decoded = rotX(input_str, x)
            count = count_common_words(decoded, dictionary)
            if count > max_count:
                best_matches = [(x, decoded, count)]
                max_count = count
            elif count == max_count and count > 0:
                best_matches.append((x, decoded, count))
        if best_matches:
            print("Most likely ROT-X decodings:")
            for x, decoded, count in best_matches:
                print(f"ROT{x}: {decoded} (dictionary words: {count})")
        else:
            print("No likely English decoding found.")

if __name__ == "__main__":
    main()
