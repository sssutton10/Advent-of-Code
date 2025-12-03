from collections import Counter, defaultdict
from datetime import datetime
from operator import itemgetter
import re

records = [[datetime.fromisoformat(y.strip()[1:17]), y.strip()[19:]] for y in open('./Day_4.txt', 'r').readlines()]
records = sorted(records, key=itemgetter(0))

# Part 1
guard_sleep = defaultdict(Counter)
guard_total = defaultdict(int)
current_guard = None

sleep_start = None
sleep_end = None

for record in records:
    if 'Guard' in record[1]:
        current_guard = re.search(r'[0-9]+', record[1]).group(0)
    elif 'falls asleep' in record[1]:
        sleep_start = record[0].minute
    elif 'wakes up' in record[1]:
        sleep_end = record[0].minute
        for minute in range(sleep_start, sleep_end):
            guard_sleep[current_guard][minute] += 1
        guard_total[current_guard] += (sleep_end - sleep_start)

sleepiest_guard = max(guard_total, key=guard_total.get)
guard_sleep[sleepiest_guard].most_common()[0][0] * int(sleepiest_guard)

# Part 2
guard_id = None
minute_most_asleep = 0
times_slept = 0

for guard, log in guard_sleep.items():
    mc = log.most_common()[0]
    if mc[1] > times_slept:
        guard_id = guard
        minute_most_asleep = mc[0]
        times_slept = mc[1]
print(int(guard_id) * minute_most_asleep)
