import csv 

with open('Assets/maze.csv', 'r') as data:
    tilemap = []  
    data = csv.reader(data, delimiter=',')
    for row in data:
        tilemap.append(row)

print('lolxd')
for row in tilemap:
    print(row)

