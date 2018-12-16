"""Plot Graph"""

# ------- Import Section -------

import pygal as py
import numpy as num
import json as js

# ------- Read Data File Section -------

record = []

with open('Data.txt') as f:
    for line in f:
        record.append(line.split('~'))

record[0][0] = 'N'
print(record)

# ------- Draw A Graph Sections --------

# graph = pygal.Bar()
# graph.title = 'Browser usage evolution (in %)'
# graph.x_labels = map(str, range(2002, 2013))
# graph.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
# graph.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
# graph.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
# graph.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
# graph.render()