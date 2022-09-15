from collections import deque
from pickle import TRUE

#English
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# key = "wenenlich"
# message = "abcdefghijklmnopqrstuvwxyz"
# encodedMessage = "wfphrqojpfoyqazxsyoxhzjigb"
# encodedMessage = "jlyvrataakpnwgxmuzwkrpfdmpaoshxusqutwrtvhaxguerbwgwipkkryctccp dwpqvrxikuossgbxuuawjsavwtdlsmgllzcuvkrpeaywvoapcjrpttlcvrxszzrh nxvrgsqudwwgmzpejljpbzropktwwfsapdgujsjhbywvadmaojttnininorlak sutesppmfzfslvbzbfpoxeipomrvomgiqdmebniycnwtgsoivrulvfzpmypplcvp krnkntvuadiyfbcodbpcbyzlsgvsrzmaocrhbxrvzfkjdkvxkepmpzgmawepiffp scpnjxcyphrjrykgzsinorymfhjhsyaoatlyfsoflngsuly"

#Russian
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def getPos(symbol, alphabet):
    a = alphabet.find(symbol)
    if a<0:
        raise "Cannot find symbol in alphabet"
    return a    

def encode(messageToEncode, key, alphabet):
    shiftingArray = deque(alphabet)

    m = messageToEncode.lower().replace(" ","")
    ans=""

    # print(alphabet)
    for i in range (len(m)):
        messageLetter = m[i]
        messageLetterPos = getPos(messageLetter, alphabet)

        keyLetter = key[i%len(key)]
        keyLetterPos = getPos(keyLetter, alphabet)

        shiftingArray.rotate(-keyLetterPos)

        ans=ans+shiftingArray[messageLetterPos]
        shiftingArray.rotate(keyLetterPos)

    return ans

def decode(messageToDecode, key, alphabet):
    shiftingArray = deque(alphabet)
    
    m = messageToDecode.lower().replace(" ","")
    ans=""

    for i in range(len(m)):
        keyLetter = key[i%len(key)]
        keyLetterPos = getPos(keyLetter, alphabet)

        shiftingArray.rotate(-keyLetterPos)

        messageLetter = m[i]
        for j in range(len(shiftingArray)):
            if (shiftingArray[j] == messageLetter):
                ans += alphabet[j]
                break
        
        shiftingArray.rotate(keyLetterPos)

    return ans    

while TRUE:

    message = input("Enter your message: ").lower().replace(" ","")
    if(message=="exit"):
        break

    option = input("What would you like to do with this message (E for Encode or D for Decode): ").lower()
    key = input("Enter the key you want to use: ").lower().replace(" ","")
    if(option=="e" or option=="encode"):
        encodedMessage = encode(message, key, alphabet)
        print(encodedMessage)
    elif(option=="d" or option=="decode"):
        decodedMessage = decode(message, key, alphabet)
        print(decodedMessage)