"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""

import requests


def extract(
    url="https://reurl.cc/pvAYlx",
    file_path="data/US_births_2000-2014_SSA.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path
