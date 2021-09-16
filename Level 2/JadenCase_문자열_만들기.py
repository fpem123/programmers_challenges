def solution(s):
    s = s.split(" ")
    
    for idx, item in enumerate(s):
        """
        if item.isalpha():
            s[idx] = item.title()
        else:
            s[idx] = item.lower()"""
        s[idx] = item.capitalize()
    
    return " ".join(s)