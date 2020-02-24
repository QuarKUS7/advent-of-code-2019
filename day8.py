if  __name__== '__main__':
    with open('./input/day8', 'r') as f:
        input = f.read()
    min_layer = ""
    min_zeros = 9999999
    for i in range(150,len(input),150):
        layer_start = i - 150
        layer_end = i
        layer = input[layer_start:layer_end]
        num_zeros = layer.count('0')
        #import pdb; pdb.set_trace()
        if num_zeros < min_zeros:
            min_zeros = num_zeros
            min_layer = layer
    print(min_layer)
    ones = min_layer.count('1')
    twos = min_layer.count('2')
    print(ones*twos)
