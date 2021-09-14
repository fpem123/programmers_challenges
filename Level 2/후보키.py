def isUnique(attrs):
    attrs = list(map(list, zip(*attrs)))
    sizeOfAttrs = len(attrs)
    sizeOfSet = len(set(map(tuple, attrs)))
    
    if sizeOfAttrs == sizeOfSet:
        return True
    
    return False


def solution(relation):
    answer = 0
    numOfTuples = len(relation[0])
    newRelation = [[] for _ in range(numOfTuples)]
    
    for line in relation:
        for idx, attr in enumerate(line):
            newRelation[idx].append(attr)
    
    queue = [tuple(i for i in range(numOfTuples))]
    visited = set()
    cKeys = set()
    
    while queue:
        idxs = queue.pop(0)
        getUniqueSon = False
        visited.add(idxs)
        
        for i in idxs:
            nidxs = []
            ntable = []
            
            for j in idxs:
                if j == i:
                    continue
                nidxs.append(j)
            
            nidxs = tuple(nidxs)
            
            for j in nidxs:
                ntable.append(newRelation[j])
            
            if isUnique(ntable) and ntable and nidxs not in visited:
                queue.append(nidxs)
                getUniqueSon = True
        
        if not getUniqueSon:
            cKeys.add(idxs)
    
    return len(cKeys)