import re

def solution(skill, skill_trees):
    answer = 0
    fm_skill = '[' + skill + ']'
    p = re.compile(fm_skill)
    
    for skill_tree in skill_trees:
        skill_tree = ''.join(p.findall(skill_tree))
        if re.match(skill_tree, skill):
            answer += 1
    
    return answer