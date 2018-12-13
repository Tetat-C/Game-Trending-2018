"""Plot Graph"""



import matplotlib.pyplot as plt

data = open("Data.txt", "r")
lines = data.read().split(',')

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

# plt.figure(1, figsize=(9, 3))

# plt.subplot(131)
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()