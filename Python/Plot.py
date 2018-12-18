"""Plot Graph"""

# ------- Import Section -------

import pygal as py
import json as js

# ------- Data Section -------

with open('Data.txt') as f:
    record = [line.replace('\n', '').split('~') for line in f]

record[0][0] = 'N'

sex = [record[i][0] for i in range(len(record))]
age = [record[i][1] for i in range(len(record))]
platform = [record[i][2] for i in range(len(record))]
genre = [record[i][3].lstrip('[').rstrip(']').replace(' ', '').split(',') for i in range(len(record))]
games = [record[i][4].lstrip('[').rstrip(']').replace(' ', '').split(',') for i in range(len(record))]

genre_count = {}
for i in genre:
    for j in i:
        if j not in genre_count:
            genre_count[j] = 1
        else:
            genre_count[j] += 1

games_count = {}
for i in games:
    for j in i:
        if j not in games_count:
            games_count[j.encode('ascii', 'ignore').decode("utf-8")] = 1
        else:
            games_count[j.encode('ascii', 'ignore').decode("utf-8")] += 1

del games_count['MOBA']

print(js.dumps(genre_count, indent=2))
print(js.dumps(games_count, indent=2))

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
byplatform.add('Consoles', platform.count('Consoles')+1)
byplatform.render_to_file('./chart/byPlatform.svg')

# .......................................

bygenre = py.Pie()
bygenre.title = 'Genre'
for i in genre_count:
    bygenre.add(i, genre_count[i])
bygenre.render_to_file('./chart/byGenre.svg')

# .......................................

bygames = py.Pie()
bygames.title = 'Games'
for i in games_count:
    bygames.add(i, games_count[i])
bygames.render_to_file('./chart/byGames.svg')


