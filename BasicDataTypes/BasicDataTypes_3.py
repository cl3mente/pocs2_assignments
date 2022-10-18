if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
        
    lowest = min(scores)
    remove = []
    for score in scores:
        if score != lowest:
            remove.append(score)
        else:
            pass
            
    lowest = min(remove)
    
    result = []
    
    for s in students:
        for a in s:
            if type(a) == float and a == lowest:
                result.append(s)

    name_result = []
    for s in result:
        for a in s:
            if type(a) == str:
                name_result.append(a)
    name_result.sort()
    for s in name_result:
        print(s)
            
                
            
    
