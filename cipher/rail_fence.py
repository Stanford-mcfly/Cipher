def rail_fence(key,text):
    if key == 1:
        return text
    
    matrix = [["\n" for _ in range(len(text))] for _ in range(key)]
    
    ptr = False
    row, coln = 0,0 
    for char in text:
        matrix[row][coln] = char
        coln+=1
        
        if row == 0 or row == key-1:
            ptr = not ptr 
        row+=1 if ptr else -1
        
    
    result=""
    for i in range(key):
        for j in range(len(text)):
            if matrix[i][j] != '\n':
                result+=matrix[i][j]
                
    return result
    
    
def main():
    answer = rail_fence(3,'reva')
    print(answer)
    
if __name__=='__main__':
    main()