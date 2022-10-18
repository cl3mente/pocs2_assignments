# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

ab = int(input())
bc = int(input())

theta = round(math.degrees(math.atan(ab/bc)))

print(str(theta) + chr(176))
     
