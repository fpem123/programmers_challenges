import re

def originName(item):
    return item[1]


def solution(files):
    answer = []
    nregex = re.compile('\d+')
    filesDict = {}  # head : number, origin name
    
    for idx, file in enumerate(files):
        nstart, nend = nregex.search(file).span()
        head, number, tail = file[:nstart].lower(), int(file[nstart:nend]), file[nend:]
        
        filesDict.setdefault(head, [])
        filesDict[head].append((number, file))
    
    for head, arr in sorted(filesDict.items()):
        arr = sorted(arr, key=lambda x: x[0])
        answer += list(map(originName, arr))
    
    return answer