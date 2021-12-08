import os

def day_1(input_data) -> int:
    counter = 0
    for key, item in enumerate(input_data):
        if key:
            if item > input_data[key-1]:
                counter += 1
        
    return counter


path = os.getcwd() + '/day1/input_data.txt'
input_data = open(path, 'r').read().splitlines()
input_data = [int(x) for x in input_data]
print(day_1(input_data))