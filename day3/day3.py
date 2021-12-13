import os

def get_value_energy(input_data):
    t_gama = ''
    range_data = len(input_data)
    data = [list(item) for item in input_data]
    cleaned_data = []
    
    for item in range(0, len(data[0])):
        cleaned_data.append([x[item] for x in data])
    
    for item in cleaned_data:
        found_1 = [x for x in item if x == '1']
        if len(found_1) > (range_data//2):
            t_gama += '1'
        else:
            t_gama += '0'
    
    t_epsilon = t_gama.replace('1', ' ').replace('0', '1').replace(' ', '0')
      
    return (int(t_gama, 2) * int(t_epsilon, 2))


def get_vital_support(input_data):
    return 230

path = os.getcwd() + '/day3/input_data.txt'
input_data = open(path, 'r').read().splitlines()

print(get_value_energy(input_data))