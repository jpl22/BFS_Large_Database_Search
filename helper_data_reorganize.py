# Last edit: Sat Feb 16 02:35

import json

def helper_data_reorganize():
    """
    Help reorganize the raw data mined from IMDB to a structure the BFS function can handle easily and fast.
    pre-converted: [[actor_id_1, actor_id_2, movie_id]]
    post-converted: {actor_id_1: {actor_id_2, actor_id_3, actor_id_4}}
    """
    # Open and load the JSON data file.
    with open ('Data resources/data.json') as dataFile:
        dataSample = json.load(dataFile)

    # Convert "List of Lists" structure to a dictionary where keys are actor's IDs and
    # value is a set IDs of actors who have acted together with the "key" actor.
    dataDict = {}
    for d in dataSample:
        for i in range(2):
            if d[i] not in dataDict:
                dataDict[d[i]] = {d[1 - i]}
            else:
                dataDict[d[i]].add(d[1 - i])
    return dataDict