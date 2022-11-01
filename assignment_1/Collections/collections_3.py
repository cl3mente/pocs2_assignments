# Named Tuple

from collections import namedtuple

N = int(input())
Student = namedtuple("Student", input())

grades = []
for i in range(N):
    
    stud = Student(*input().split())
    grades.append(int(stud.MARKS))
    
print(sum(grades)/N)
    