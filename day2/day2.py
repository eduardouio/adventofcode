import os

def get_location(data)->int:
    x = y = 0
    for item in data:
        coordinates = item.split(' ')
        if coordinates[0].lower() == 'forward':
            x += int(coordinates[1])
        
        if coordinates[0].lower() == 'up':
            y -= int(coordinates[1])
        
        if coordinates[0].lower() == 'down':
            y += int(coordinates[1])
        
    return (x*y)

def get_location_2(data)->int:
    x = obj = dep = 0
    for item in data:
        coordinates = item.split(' ')
        if coordinates[0].lower() == 'forward':
            x += int(coordinates[1])
            dep = (int(coordinates[1]) * obj) + dep

        if coordinates[0].lower() == 'up':
            obj -= int(coordinates[1])

        if coordinates[0].lower() == 'down':
            obj += int(coordinates[1])    
    
    return (x * dep)

path = os.getcwd() + '/day2/input_data.txt'
input_data = open(path, 'r').read().splitlines()

print(get_location(input_data))
print(get_location_2(input_data))




