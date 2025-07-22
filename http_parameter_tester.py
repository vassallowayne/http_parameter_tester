# Author: Wayne Vassallo

import requests
import argparse
import sys

def load_wordlist(path):
    try:
        with open(path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {path}")
        sys.exit(1)

def test_parameters(url_template, wordlist, value, verbose):
    print(f"[+] Testing parameters on: {url_template}")
    print(f"[+] Using payload value: {value}")
    print("-" * 60)

    headers = {
        "User-Agent": "ParamTester"
    }

    for param in wordlist:
        test_url = url_template.replace("FUZZ", f"{param}={value}")
        try:
            resp = requests.get(test_url, headers=headers, timeout=5)
            content = resp.text

            reflected = value in content
            status = resp.status_code
            length = len(content)

            line = f"{param:<20} | {status:<4} | {length:<6} | {'[REFLECTED]' if reflected else ''}"
            print(line)

        except requests.exceptions.RequestException as e:
            print(f"[!] Error on {param}: {e}")

def main():
    parser = argparse.ArgumentParser(description="HTTP Parameter Tester")
    parser.add_argument('url', help='Target URL with FUZZ placeholder (e.g., https://example.com/index.php?FUZZ=value)')
    parser.add_argument('--wordlist', help='Path to parameter name wordlist', default='params.txt')
    parser.add_argument('--value', help='Value to inject for each parameter', default='injected_test')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    args = parser.parse_args()

    if "FUZZ" not in args.url:
        print("[!] URL must contain FUZZ placeholder")
        sys.exit(1)

    wordlist = load_wordlist(args.wordlist)
    test_parameters(args.url, wordlist, args.value, args.verbose)

if __name__ == "__main__":
    main()
