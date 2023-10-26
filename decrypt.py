#!/usr/bin/env python3
import sys
import os

def load_env(path):
    env = {}
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
        if "SHADOW_KEY" not in env or not env["SHADOW_KEY"].strip():
            sys.stderr.write('Error: "SHADOW_KEY" environment variable not set in .env\n')
            sys.exit(1)
    return env

def decode_file(path):
    with open(path, "rb") as f:
        data = f.read()
    
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    env = load_env(env_path)
    key = env.get("SHADOW_KEY", "")
    
    if not key:
        sys.stderr.write('Error: "SHADOW_KEY" environment variable not set in .env\n')
        sys.exit(1)
    
    # TODO: Implement decryption logic using key
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
