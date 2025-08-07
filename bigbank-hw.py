"""Bigbank homework."""
import sys
import requests

# Ask for URL and throw help text in case of discrepancies
if len(sys.argv) != 2:
    print("Usage: python bigbank-hw.py <url>\nFor example: python bigbank-hw.py https://delfi.ee")
    sys.exit(0)

url = sys.argv[1]

# Use requests library to get our desired parameters
try:
    response = requests.get(url)
    response_code = response.status_code
    response_time = (response.elapsed.total_seconds() * 1000)
    result = "OK" if response_code == 200 else "NOK"
    print(f"Response Code: {response_code}\nResult: {result}\nResponse Time: {response_time} ms")

# Error handling
except requests.exceptions.RequestException as e:
    print(f"RequestException: {e}")
