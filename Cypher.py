def getkey(ukey):
    key = 0
    for i in range(0,len(ukey)):
        key += ord(ukey[i])
    return key
def cypher(encrypted,key,isencrypted):
    result = "The result is:"
    for i in range(0,len(encrypted)):
        if(isencrypted == True):
            encrypted[i] =ord(encrypted[i])+int(key)
        else:
            encrypted[i] =ord(encrypted[i])-int(key)
        result += chr(encrypted[i])
    print(result)
    input("")
uinput = input("Please write your string here: ")
isencrypted = (input("type y if the string you inputted is allready encrypted : ").lower().lstrip().rstrip()!= "y")
ukey = [ch for ch in input("Please write the key: ")]
encrypted = [ch for ch in uinput]
key = 0
cypher(encrypted,getkey(ukey),isencrypted)
