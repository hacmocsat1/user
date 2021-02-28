
import requests
import sys
import json


def get_data(username):
    url = "https://api.github.com/users/{}/repos".format(username)
    resp = requests.get(url)
    data = json.loads(resp.text)
    if len(data) == 0:
        print("User don't exists")
    if isinstance(data, list):
        with open('data_cv.json', 'w') as f:
            f.write(json.dumps(data, indent= 4))


def main():
    if len(sys.argv) != 2:
        print('Usage: python user.py <USERNAME>')
    else:
        username = sys.argv[1]
        get_data(username)


if __name__ == "__main__":
    main()