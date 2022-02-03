# Implements the vigenere cipher

message = 'barry is the spy'
encrypted = 'dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encryptionKey = 'friends'
keyword = 'dog'


def encrypt(message, key):
    result = ''
    message = message.lower()
    key = key.lower()
    i = 0
    for cha in message:
        if not inAlp(cha):
            result += cha
            continue
        value = getIn(cha)
        keyValue = i % len(key)
        currentKey = key[keyValue]
        keykey = getIn(currentKey)
        cryptoShift = (value+keykey) % 26
        result += alphabet[cryptoShift]
        i += 1
    return result


def decrypt(message, key):
    result = ''
    message = message.lower()
    key = key.lower()
    i = 0
    for cha in message:
        if not inAlp(cha):
            result += cha
            continue
        value = getIn(cha)
        keykey = getIn(key[i % len(key)])
        index = value-keykey
        if(index < 0):
            index += 26
        result += alphabet[index]
        i += 1
    return result


def inAlp(char):
    return char in alphabet.lower()


def getIn(char):
    return alphabet.lower().index(char)


print(encrypt(message, keyword))

print(decrypt(encrypted, encryptionKey))

#encrypt('DCODE', 'KEY')
