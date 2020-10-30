def solution(phone_book):
    answer = True
    first = dict()

    phone_book.sort()

    for i in phone_book:
        if i[0] not in first:
            first[i[0]] = [i]
        else:
            first[i[0]] += [i]

    for i in first.values():
        finder = 0
        f_len = 1
        for j in i:
            if finder != j[:f_len]:
                finder = j
                f_len = len(j)
            else:
                return False


    return answer