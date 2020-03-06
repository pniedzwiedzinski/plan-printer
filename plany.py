#!/usr/local/bin/python3

import json
import sys
import requests
from name_prettier import prettify

URL = "https://kapskypl.github.io/planyn-backend/classes/"

def get_plan(cls):
    plan = requests.get(URL + cls + ".json").json()
    return plan

def print_table(plan):
    rows = [ [ day[i] for day in plan ] for i in range(len(plan[0])) ]
    for row in rows:
        for lesson in row:
            if lesson and lesson[0] and "subject" in lesson[0]:
                print(prettify(lesson[0]["subject"]), end='\t')
            else:
                print("\t", end='')
        print()

if __name__ == "__main__":
    plan = get_plan(sys.argv[1])
    print_table(plan)
