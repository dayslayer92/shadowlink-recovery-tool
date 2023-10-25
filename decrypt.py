#!/usr/bin/env python3
import sys
import os

def decode_file(path):
    with open(path, "rb") as f:
        data = f.read()
    # TODO: Implement decryption logic
    return data.decode("utf-8", errors="replace")

def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Error: No input file specified.\n')
        sys.stderr.write('Usage: python decrypt.py <input_file.shadow>\n')
        sys.exit(1)
    
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        sys.stderr.write(f'Error: "{input_file}" file not found.\n')
        sys.exit(1)
    
    print(decode_file(input_file))

if __name__ == "__main__":
    main()
