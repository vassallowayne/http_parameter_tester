# http_parameter_tester
Takes a target URL with a single FUZZ placeholder



## HTTP Parameter Tester

This script helps identify potentially injectable, reflected, or interesting HTTP parameters by fuzzing a target URL with common parameter names.

### What It Does

- Takes a URL with a `FUZZ` placeholder (e.g., `https://example.com/page.php?FUZZ=value`)
- Substitutes `FUZZ` with common parameter names from a wordlist
- Sends HTTP GET requests for each parameter
- Detects:
  - Reflected values in the response body
  - Changes in status code or content length
- Useful for recon, web fuzzing, XSS injection points, or identifying undocumented parameters

### Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- A wordlist of parameter names (`params.txt` included)

### Usage

```bash
python3 http_parameter_tester.py "https://example.com/index.php?FUZZ=value" --wordlist params.txt

