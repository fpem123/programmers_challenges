def solution(records):
    answer = []
    new_records = []
    id_dict = {}
    
    for record in records:
        record = record.split()
        
        if record[0] == "Enter":
            id_dict[record[1]] = record[2]
            new_records.append(["Enter", record[1]])
        elif record[0] == "Change":
            id_dict[record[1]] = record[2]
        else:
            new_records.append(["Leave", record[1]])
    
    for record in new_records:
        if record[0] == "Enter":
            answer.append(f"{id_dict[record[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{id_dict[record[1]]}님이 나갔습니다.")
            
    return answer