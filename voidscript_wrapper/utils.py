import os
from requests import post, get
from requests.auth import HTTPBasicAuth

base_url = "http://localhost:5000/"


def make_request(url, method, payload=None):
    url = base_url + url
    auth = HTTPBasicAuth(
        os.environ.get("VOIDSCRIPT_EMAIL", ""),
        os.environ.get("VOIDSCRIPT_API_KEY", ""),
    )

    if method == "GET":
        try:
            return get(url, auth=auth).json()
        except Exception as e:
            return e

    elif method == "POST":
        try:
            return post(url, data=payload, auth=auth).json()
        except Exception as e:
            return e
