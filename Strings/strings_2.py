#String Validators

if __name__ == '__main__':
    s = input()
    
    if s.isalnum() == False:
        for i in s:
            if i.isalnum() == True:
                print(True)
                break
        else:
            print(False)          
    else:
        print(True)  
            
    if s.isalpha() == False:
        for i in s:
            if i.isalpha() == True:
                print(True)
                break
        else:
            print(False)          
    else:
        print(True)  

    
    if s.isdigit() == False:
        for i in s:
            if i.isdigit() == True:
                print(True)
                break
        else:
            print(False)          
    else:
        print(True)  
    
    if s.islower() == False:
        for i in s:
            if i.islower() == True:
                print(True)
                break
        else:
            print(False)          
    else:
        print(True)  
    
    if s.isupper() == False:
        for i in s:
            if i.isupper() == True:
                print(True)
                break
        else:
            print(False)          
    else:
        print(True)  

    
