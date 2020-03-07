#!/usr/bin/python

import json
import sys
import requests
from tabulate import tabulate
from name_prettier import prettify

URL = "https://kapskypl.github.io/planyn-backend/classes/"

def get_plan(cls):
    plan = requests.get(URL + cls + ".json").json()
    return plan

def is_empty(row):
    for el in row:
        if el:
            return False
    return True

def parse_plan(plan):
    """
    Replace rows with columns.
    """
    parsed_plan = [ [] for _ in range(len(plan[0])) ]
    for day in plan:
        for i, lesson in enumerate(day):
            if type(lesson) == list and len(lesson) > 0:
                parsed_plan[i].append(prettify(lesson[0]["subject"]) + ' ' + lesson[0]["room"])
            else:
                parsed_plan[i].append(None)
    return [ row for row in parsed_plan if not is_empty(row)]

def print_table(plan):
    print(tabulate(plan, ["Pn", "Wt", "Sr", "Czw", "Pt"], tablefmt="grid"))

if __name__ == "__main__":
    plan = get_plan(sys.argv[1])
    p_plan = parse_plan(plan)
    print_table(p_plan)
