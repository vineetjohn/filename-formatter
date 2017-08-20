#!/usr/bin/python

import re
import sys

def clean_str(string):
    string = re.sub(r"'", "", string)
    string = re.sub(r",", "", string)
    string = re.sub(r"!", "", string)
    string = re.sub(r"\(", "", string)
    string = re.sub(r"\)", "", string)
    string = re.sub(r"\[", "", string)
    string = re.sub(r"\]", "", string)
    string = re.sub(r"\?", "", string)
    string = re.sub(r":", "", string)
    string = re.sub(r" - ", "-", string)
    string = re.sub(r"\n", " ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = string.strip()
    string = re.sub(r" ", "-", string)
    string = re.sub(r"\.-", "-", string)

    return string.lower()

print(clean_str(sys.argv[1]))
