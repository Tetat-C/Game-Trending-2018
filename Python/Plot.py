"""Plot Graph"""

# ------- Import Section -------

import pygal as py
import json as js

# ------- Read Data File Section -------

record = []

with open('Data.txt') as f:
    for line in f:
        record.append(line.split('~'))

record[0][0] = 'N'

sex = [record[i][0] for i in range(len(record))]
age = [record[i][1] for i in range(len(record))]
platform = [record[i][2] for i in range(len(record))]
genre = [record[i][3] for i in range(len(record))]
games = [record[i][4] for i in range(len(record))]

# ------- Draw A Graph Sections --------

bysex = py.Pie()
bysex.title = 'Gender'
bysex.add('Male', sex.count('M'))
bysex.add('Female', sex.count('W'))
bysex.add('Non-Specific', sex.count('N'))
bysex.render_to_file('./chart/byGender.svg')

# .......................................
