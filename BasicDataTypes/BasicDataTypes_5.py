#Lists

if __name__ == '__main__':
    N = int(input())
    
    list = []
    
    for _ in range(N):
        
        action = input().split()
        
        

        if action[0] == "insert":
            list.insert(int(action[1]), int(action[2]))
        if action[0] == "print":
            print(list)
        if action[0] == "remove":
            list.remove(int(action[1]))
        if action[0] == "append":
            list.append(int(action[1]))
        if action[0] == "pop":
            list.pop()
        if action[0] == "reverse":
            list.reverse()
        if action[0] == "sort":
            list.sort()
        
            
