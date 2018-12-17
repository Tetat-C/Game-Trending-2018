"""Plot Graph"""

# ------- Import Section -------

import pygal as py
import json as js

# ------- Read Data File Section -------

record = []

with open('Data.txt') as f:
    for line in f:
        record.append(line.replace('\n', '').split('~'))

record[0][0] = 'N'

sex = [record[i][0] for i in range(len(record))]
age = [record[i][1] for i in range(len(record))]
platform = [record[i][2] for i in range(len(record))]
genre = [record[i][3].lstrip('[').rstrip(']').replace(' ', '').split(',') for i in range(len(record))]
games = [record[i][4].lstrip('[').rstrip(']').replace(' ', '').split(',') for i in range(len(record))]


# ------- Draw A Graph Sections --------

bysex = py.Pie()
bysex.title = 'Gender'
bysex.add('Male', sex.count('M'))
bysex.add('Female', sex.count('W'))
bysex.add('Non-Specific', sex.count('N'))
bysex.render_to_file('./chart/byGender.svg')

# .......................................

byage = py.Pie()
byage.title = 'Age'
byage.add(' Below 9', age.count('9'))
byage.add('9 - 15', age.count('9 - 15'))
byage.add('16 - 22', age.count('16 - 22'))
byage.add('23 - 29', age.count('23 - 29'))
byage.add(' Beyond 30', age.count('30'))
byage.render_to_file('./chart/byAge.svg')

# .......................................

byplatform = py.Pie()
byplatform.title = 'Platform'
byplatform.add('PC', platform.count('PC'))
byplatform.add('Mobile', platform.count('Mobile')+1)
byplatform.add('Consoles', platform.count('Consoles'))
byplatform.render_to_file('./chart/byPlatform.svg')

# .......................................



