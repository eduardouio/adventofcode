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

def get_value_common(input_data, position=0 ,most_common = True):
    data = [list(item) for item in input_data]
    file_numbers= []
    
    for k,row in enumerate(data):
        for col in row:
            file_numbers.append(col[position])
            
    count_bit_0 = file_numbers.count('0')
    count_bit_1 = file_numbers.count('1')
    
    import ipdb; ipdb.set_trace()
    
    if most_common:
        return '1' if count_bit_1 > count_bit_0 else '0'
    
    return '1' if count_bit_1 < count_bit_0 else '0'
        
    
    base = [list(i) for i in data]
        
        # TODO
        # Hace tomar el valor por nuemros de 5 bits, solamente hacer la lista para buscar el mas comun 
        # con el count, luego de tomar el mas comuno retorar todos los valores de esa fila.
        if column[position].count('1') > (len(input_data)//2):
            common_value = '1'
        
      
    return '10111'

def get_vital_support(input_data):
    return 230

path = os.getcwd() + '/day3/input_data.txt'
input_data = open(path, 'r').read().splitlines()

print(get_value_energy(input_data))