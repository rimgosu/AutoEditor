def index_exapnd(input_index, minus_constant, plus_constant):
    output_index = []
    for j in input_index:
        for k in range(-minus_constant, plus_constant):
            output_index.append(j+k)
    return output_index
def set_list_sort(index):
    index = set(index)
    index = list(index)
    index.sort()
    return(index)
def trim_edge(_gamestart, _gameend, source_list):
    edge = []
    for j in range(0, _gamestart):
        edge.append(j)
    for j in range(_gameend, 20000):
        edge.append(j)
    for j in edge:
        while j in source_list:
            source_list.remove(j)
    source_list = set_list_sort(source_list)
    return source_list

input_index = []
output_index = index_exapnd(input_index, 1, 5)
print(output_index)
input_index = trim_edge(1, 5, input_index)
print(input_index)