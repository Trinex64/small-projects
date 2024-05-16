def rot_n(text, shifts, decode=False):
    res = []
    shifts = [(ord(char.lower()) - 96) * (-1 if decode else 1) for char in shifts]
    for i, char in enumerate(text):
        if char.isalpha():
            shift = shifts[i % len(shifts)]
            a = 65 if char.isupper() else 97
            res.append(chr((ord(char) - a + shift) % 26 + a))
        else:
            res.append(char)
    return ''.join(res)

opt = input("Select 1 for encode and 2 for decode: ")
text = input("Enter your message: ")
key = input("Enter the key: ")
print(rot_n(text, key, decode=opt=='2'))
input()

### ULTRA COMPACT VER ###
#def rot_n(t, k, d=False):
#    s = [(ord(c.lower()) - 96) * (-1 if d else 1) for c in k]
#    return ''.join(chr((ord(c) - (65 if c.isupper() else 97) + s[i % len(s)]) % 26 + (65 if c.isupper() else 97)) if c.isalpha() else c for i, c in enumerate(t))

#o = input("1 for encode, 2 for decode: ")
#print(rot_n(input("Message: "), input("Key: "), d=o=='2'))
