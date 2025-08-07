A simple script to monitor external endpoints.

# Usage
Simply call the script and specify a URL to test.

`python bigbank-hw.py <url>`

For example, to query the status of the Delfi news portal.

`python bigbank-hw.py https://delfi.ee`

# Outputs
The script will return the following.
- Response code (for example 200)
- Result (OK in case of code 200, else NOK)
- Response time in ms
