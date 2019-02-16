def BFS_Large_Database_Search(data, actor_id_1, actor_id_2):
    """
    BFS for large database. data is raw data resource from IMDB, can be
    converted into more efficient data structure with helper function.
    You can always also write your own converting function or find other
    resources originally with workable structure. actor_id_1 and
    actor_id_2 are "start" and "end" id (int) of actors.
    Another helper function, written below, helps sort the
    returning answer (set) into an existing path.
    """
    # Help form dictionary-based data.
    dataDict = helper_data_reorganize(data)

    # Check if both id is in the name list...
    if actor_id_1 not in dataDict or actor_id_2 not in dataDict:
        return None

    # Initial first path based on your own preference.
    initPath = {actor_id_1}
    pathQueue = set()
    pathQueue.add(tuple(initPath)) # pathQueue store paths as tuple

    # Keep track of considered paths.
    considered = set()

    # Keep track of all visited nodes, given that they've already
    # been reached some time before by shorter paths, there's no need to reach them anymore
    visited = set()

    # While not all paths have been considered...
    while len(considered) < len(pathQueue):
        # Get the un-considered part.
        thisRound = pathQueue.difference(considered)
        for tempPath in thisRound:  # tempPath is a tuple now, but will be converted back into set
            tempPathSet = set(tempPath)
            # Get the un-visited ones of all time.
            thisNode = tempPathSet.difference(visited)
            for node in thisNode:
                # If arrived the end...
                if node == actor_id_2:
                    sortedPath = helper_sort_path(dataDict, tempPathSet, actor_id_1)
                    return sortedPath
                for nextNode in dataDict[node]:
                    if nextNode not in tempPathSet and nextNode not in visited:
                        newPath = list (tempPathSet) + [nextNode]
                        pathQueue.add(tuple(newPath))
                visited.add(node)
            considered.add(tuple(tempPathSet))
    return None

def helper_sort_path(dataDict, path, actor_id_start):
    """
    Help sort the un-ordered set into a real path.
    path is a set of integers.
    """
    list = [actor_id_start]
    # Father node...
    father = actor_id_start
    set.remove(actor_id_start)
    for i in range(len(path)):
        for x in dataDict[father]:
            if x in set:
                list.append(x)
                father = x
                set.remove(x)

    return list
