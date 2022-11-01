#find a string

def count_substring(string, sub_string):
    
    sub_length = int(len(sub_string))
    count = 0
    for i in range(0, len(string)+1):
        if string[i:i+sub_length] == sub_string:
            count+=1

    return count

