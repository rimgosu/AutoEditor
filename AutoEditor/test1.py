def trim_edge(_gamestart, _gameend, source_list):
    edge = []
    for j in range(0, _gamestart):
        edge.append(j)
    for j in range(_gameend, 20000):
        edge.append(j)
    source_list = set(source_list)
    source_list = list(source_list)
    source_list.sort()
    for j in edge:
        while j in source_list:
            source_list.remove(j)
            print(j, 'removed')
    return source_list

recon =[6610, 6611, 6612, 6613, 6614, 6615, 6616, 6617, 6618, 6619, 6620, 6621, 6622, 6623, 6624, 9894, 9895, 9896, 9897, 9898, 9899, 10448, 10449, 10450, 10451, 10452, 10453, 10454, 10988, 10989, 10990, 10991, 10992, 10993, 10994, 10995, 10996, 10997, 10998, 10999, 11000, 11001, 11002, 11003, 11004, 11005, 11006, 11007, 11008, 11009, 11010, 11518, 11520, 11521, 11522, 11523, 11524, 11525, 11526, 11527, 
11528, 11529, 11530, 11531]

recon = trim_edge(343, 9196, recon)

print(recon)