import os
from unittest import result

def get_location(data)->int:
    x = 0
    y = 0
    for item in data:
        coordinates = item.split(' ')
        if coordinates[0].lower() == 'forward':
            x += int(coordinates[1])
        
        if coordinates[0].lower() == 'up':
            y -= int(coordinates[1])
        
        if coordinates[0].lower() == 'down':
            y += int(coordinates[1])
        
    return (x*y)

path = os.getcwd() + '/day3/input_data.txt'
input_data = open(path, 'r').read().splitlines()

print(get_location(input_data))