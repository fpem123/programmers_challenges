def solution(n, words):
    for idx in range(1, len(words)):
        if len(words[idx]) < 2 or words[idx][0] != words[idx - 1][-1] or words[idx] in words[:idx]:
            return [idx % n + 1, idx // n + 1]
    else:
        return [0, 0]