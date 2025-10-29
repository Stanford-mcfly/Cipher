def rail_fence(key, text):
    if key == 1 or key >= len(text):
        return text
    
    rails = [''] * key
    row, direction = 0, 1
    
    for char in text:
        rails[row] += char
        row += direction
        if row == 0 or row == key - 1:
            direction = -direction
    
    return ''.join(rails)

def main():
    answer = rail_fence(3, 'reva')
    print(answer)
    
if __name__ == '__main__':
    main()