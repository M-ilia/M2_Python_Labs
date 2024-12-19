# TODO решите задачу

import json
file = 'input.json'

def task(file) -> float:
    sum_ = 0
    with open(file) as f:
        for line in json.load(f):
            sum_ += line["score"] * line["weight"]
    return sum_

print(f'{task(file):.3f}')
