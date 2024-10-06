import requests


def extract(
    url="https://reurl.cc/pvAYlx",
    file_path="data/US_births.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
