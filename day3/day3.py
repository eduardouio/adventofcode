import os

def get_value_energy(input_data):
    t_gama = ''
    data = [list(item) for item in input_data]
    data = [list(item) for item in zip(*data)]

    for column in data:
        if column.count('1') > (len(input_data)//2):
            t_gama += '1'
        else:
            t_gama += '0'
    
    t_epsilon = t_gama.replace('1', ' ').replace('0', '1').replace(' ', '0')
      
    return (int(t_gama, 2) * int(t_epsilon, 2))

def get_value_common(input_data, position, most_common):
    data = [list(item) for item in input_data]
    file_numbers= []
    common_bit = None
    result = []

    for row in data:
        file_numbers.append(row[position])
            
    common_bit = '1' if file_numbers.count('1') > file_numbers.count('0') else '0'
    for row in data:
        if most_common:
            result.append(row if row[position] == common_bit else None)
        else:
            result.append(row if row[position] != common_bit else None)
    
    result = [''.join(r) for r in result if r is not None]
    return result

def get_vital_support(input_data):
    o2_nominal_value = None
    co2_depuration_value = None

    for position in range(0, len(input_data[0]) - 1):
        if position == 0:
            data = input_data
        
        data = get_value_common(data, position, True)
        
        # TODO
        # DEfinir solamente el mas commun, deberia hacerce en la de most_common
        
        
    return data
        
        
    
    
    return(int(o2_nominal_value, 2) * int(co2_depuration_value, 2))
    
    
    

path = os.getcwd() + '/day3/input_data.txt'
input_data = open(path, 'r').read().splitlines()

print(get_value_energy(input_data))