#Finding Percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    grade_list = student_marks[query_name]
    average = (sum(grade_list))/len(grade_list)
    
    print("{:.2f}".format(average))
