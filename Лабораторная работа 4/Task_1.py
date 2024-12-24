# TODO решите задачу

import json
file = 'input.json'

def task(file) -> float:
    sum_ = 0
    with open(file) as f:
        sum_ = sum([line["score"] * line["weight"] for line in json.load(f)])
    return sum_

print(f'{task(file):.3f}')
