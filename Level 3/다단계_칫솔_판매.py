def solution(enroll, referral, seller, amount):
    answer = []
    income = dict(zip(enroll, [0] * len(enroll)))
    enre = dict((zip(enroll, referral)))
    amount = list(map(lambda x: x * 100, amount))
    
    while seller:
        nseller = []
        namount = []

        for se, am in zip(seller, amount):
            if am == 0:
                continue
                
            tribute = am // 10
            income[se] += am - tribute
            re = enre[se]
            
            if re != '-':
                nseller.append(re)
                namount.append(tribute)
        
        seller = nseller
        amount = namount
    
    for en in enroll:
        answer.append(income[en])
    
    return answer