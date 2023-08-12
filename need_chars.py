with open('iw4x_english.str', 'r') as f:
    strings = f.read()

char_array=[]

for char in strings:
    code = ord(char)
    if code > 127 and code not in char_array:
        
        char_array.append(code)

print(char_array)
print(len(char_array))