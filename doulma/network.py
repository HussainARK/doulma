import urllib.request
import urllib.error


def fetch(url: str, verbose: bool = False):
    if verbose:
        return urllib.request.urlopen(url)
    else:
        return urllib.request.urlopen(url).read().decode().strip()
