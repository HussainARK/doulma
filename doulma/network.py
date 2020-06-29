import urllib.request
import urllib.error
import json
from .variables import supported_http_methods


def fetch(url: str, options: dict = {'method': 'GET'}):
    request = urllib.request.Request(url)
    req_method = options['method']
    if req_method in supported_http_methods:
        if req_method == "GET":
            request.method = req_method
            return urllib.request.urlopen(request)

        elif req_method == "POST" or "PUT" or "PATCH":
            request.data = json.dumps(options['body']).encode()
            request.method = req_method
            return urllib.request.urlopen(request)

        elif req_method == "DELETE":
            request.method = req_method
            return urllib.request.urlopen(request)


def download(url: str, filename: str):
    urllib.request.urlretrieve(url, filename)
