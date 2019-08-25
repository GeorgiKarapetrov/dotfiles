def listToSet(list):
    return {el for el in list}

def usingCycles(list):
    toSet = set()
    for element in list:
        toSet.add(element)
    return toSet