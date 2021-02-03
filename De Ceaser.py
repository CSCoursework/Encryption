uencypted = input("Please write your text to encrypt: ")
ukey = [ch for ch in input("Please write the key: ")]
result = "The decrypted result is:"
encrypted = [ch for ch in uencypted]
key = 0
for i in range(0,len(ukey)):
    key += ord(ukey[i])
    print(key)
for i in range(0,len(encrypted)):
    encrypted[i] =ord(encrypted[i])-int(key)
    result += chr(encrypted[i])
print(result)
input("")