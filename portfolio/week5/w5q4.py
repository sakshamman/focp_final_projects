'''4. Write a program that takes a URL as a command-line argument and reports
whether or not there is a working website at that address.
Hint: You need to get the HTTP response code.
Another Hint: StackOverflow is your friend.
'''
#need some correction!!!

import sys
import requests

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code >= 200 and response.status_code < 300:
            print(f"The website at {url} is working.")
        else:
            print(f"The website at {url} returned a non-success status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_website.py <URL>")
    else:
        url = sys.argv[1]
        check_website(url)
