def solution(word):
    answer = 0
    size = len(word)
    wordList = {'A': 0, 'E': 1, "I": 2, 'O': 3, 'U': 4}
    count = [781, 156, 31, 6, 1]
    
    for idx in range(size):
        answer += wordList[word[idx]] * count[idx]
        
    answer += size
    
    return answer