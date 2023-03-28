# This is my lab assignment for python course
    # It is assumed that you have the data in the same folder as the program


# Import required libraries
import matplotlib.pyplot as plt
import collections
import functools
import operator
import math


# Empty variables to work with and variables that are not empty
table = []
test = []

with open('influenza.csv', 'r') as data:
    
    next(data) # Skips header line
    
    for line in data.readlines():
            line = line.replace('Level ', '')
            line = line.strip('\n')

            row = {}
            tokens = line.split(',')
            
            
            row['state'] = tokens[0]
            row['url'] = tokens[1]
            row['website'] = tokens[2]
            row['activity_lvl'] = tokens[3]
            row['activity_lvl_lbl'] = tokens[4]
            row['weekend'] = tokens[5]
            row['week'] = tokens[6]
            row['season'] = tokens[7]
        
            # print(row) # For Testing Purposes Only

            table.append(row)

        
# print(table) # For Testing Purposes Only
# print(len(table)) # For Testing Purposes Only
# print(len([x for x in table if x['state'] == 'North Carolina'])) # For Testing Purposes Only
# There are 493 NC keys

# First Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2012-13']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

x = sum(item['activity_lvl'] for item in nc_new)
x = x / len(nc)
print(round(x, 2))

# Second Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2013-14']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

y = sum(item['activity_lvl'] for item in nc_new)
y = y / len(nc)
print(round(y, 2))

# Third Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2014-15']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

z = sum(item['activity_lvl'] for item in nc_new)
z = z / len(nc)
print(round(z, 2))

# Fourth Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2015-16']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

v = sum(item['activity_lvl'] for item in nc_new)
v = v / len(nc)
print(round(v, 2))

# Fifth Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2016-17']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

q = sum(item['activity_lvl'] for item in nc_new)
q = q / len(nc)
print(round(q, 2))

# Sixth Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2017-18']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

p = sum(item['activity_lvl'] for item in nc_new)
p = p / len(nc)
print(round(p, 2))

# Seventh Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2018-19']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

u = sum(item['activity_lvl'] for item in nc_new)
u = u / len(nc)
print(round(u, 2))

# Eighth Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2019-20']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

n = sum(item['activity_lvl'] for item in nc_new)
n = n / len(nc)
print(round(n, 2))

# Ninth Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2020-21']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

m = sum(item['activity_lvl'] for item in nc_new)
m = m / len(nc)
print(round(m, 2))

# Tenth Season

nc = [x for x in table if x['state'] == 'North Carolina' and x['season'] == '2021-22']
nc_new = []

for items in nc:
    for k, v in items.items():
        if k == 'activity_lvl':
            items[k] = int(v)
            nc_new.append(items)

h = sum(item['activity_lvl'] for item in nc_new)
h = h / len(nc)
print(round(h, 2))

# After all that time to create the list for the chart
average = [2.42, 1.77, 2.62, 2.15, 2.77, 2.77, 3.38, 4.15, 1.74, 3.39]
seasons = ['2012-13', '2013-14', '2014-15', '2015-16', '2016-17', '2017-18', '2018-19', '2019-20', '2020-21', '2021-22']
x_pos = range(len(average))
font = {
    'family': 'serif',
    'color': 'crimson',
    'weight': 'bold',
    'size': 16,
}


# Plot Bar Graph
plt.bar(x_pos, average)

# Edit Bar
plt.xticks(x_pos, seasons)
plt.title('Average Influenza Cases by Season and Year', fontdict=font)
plt.xlabel('Seasons of Influenza by year', fontdict=font)
plt.ylabel('Seasonal Average', fontdict=font)
plt.tick_params(axis='both', which='major', pad=10)

plt.show()