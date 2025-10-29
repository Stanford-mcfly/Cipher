def encrypt(key,text):
    if key == 1:
        return text
    rails = [''] * key
    row, dir = 0,1

    for c in text:
        rails[row] += c
        row += dir
        if row == 0 or row == key-1:
            dir = -dir
    return ''.join(rails)

print(encrypt(3,'reva'))