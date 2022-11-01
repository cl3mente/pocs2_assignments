# Find the Runner Up Score

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    maximum = max(arr)
    while max(arr) == maximum:
        arr.remove(max(arr))
    print(max(arr))