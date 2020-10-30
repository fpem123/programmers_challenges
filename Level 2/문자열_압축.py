def solution(s):
    answer = 0
    s += 'X'
    sizes = []
    
    for size in range(1, len(s)):
        t = ''
        tmp = ''
        count = 0
        for i in range(0, len(s), size):
            if tmp != s[i:i + size]:
                if count > 1:
                    t += str(count)
                tmp = s[i:i + size]
                t += tmp
                count = 1
            else:
                count += 1
        sizes.append(len(t[:-1]))
    
    return min(sizes)