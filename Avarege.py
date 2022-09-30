#avarage

"""

import statistics

n = int(input())

a = list(map(int, input().split()))[:n]

z = statistics.mean(a)

print(z)

"""

n = int(input())

a = list(map(int, input().split()))[:n]

avarage = 0
value = 1

for i in range(0, n):
    avarage += a[i]
    z = (avarage / value)
    print(z)
    value += 1

