
# ask user for message
def get_message():
    message = raw_input("Type your message to be encrypted: ")
    message = message.lower()
    return message

# ask user for key
def get_key():
    key = ''
    while key.isalpha() != True:
        print ("Type your encryption key: ")
        key = raw_input()
    return key
    print "thnx"


# create a duplicate of message with only letters
def alpha_only(message):
    char = 0
    no_space = ""
    ignore = ""
    while (len(no_space) + len(ignore)) < len(message):
        if message[char].isalpha():
            no_space += message[char]
        else:
            ignore += message[char]
        char += 1
    return no_space

# creates string of key repeated appropriate times
def create_keyString(key, no_space):
    keyString = ""
    times_repeat = 1 + (len(no_space) / len(key))
    while times_repeat > 0:
        keyString += key
        times_repeat -= 1
    return keyString

# uses encryption key character as dictionary key to fetch value
# value encrypts message letter to encrypted letter
def look_up(no_space, keyString, x):
    k = no_space[0]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',
                'a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']
    D = {
        'a': alphabet[alphabet.index(k)],
        'b': alphabet[alphabet.index(k) + 1],
        'c': alphabet[alphabet.index(k) + 2],
        'd': alphabet[alphabet.index(k) + 3],
        'e': alphabet[alphabet.index(k) + 4],
        'f': alphabet[alphabet.index(k) + 5],
        'g': alphabet[alphabet.index(k) + 6],
        'h': alphabet[alphabet.index(k) + 7],
        'i': alphabet[alphabet.index(k) + 8],
        'j': alphabet[alphabet.index(k) + 9],
        'k': alphabet[alphabet.index(k) + 10],
        'l': alphabet[alphabet.index(k) + 11],
        'm': alphabet[alphabet.index(k) + 12],
        'n': alphabet[alphabet.index(k) + 13],
        'o': alphabet[alphabet.index(k) + 14],
        'p': alphabet[alphabet.index(k) + 15],
        'q': alphabet[alphabet.index(k) + 16],
        'r': alphabet[alphabet.index(k) + 17],
        's': alphabet[alphabet.index(k) + 18],
        't': alphabet[alphabet.index(k) + 19],
        'u': alphabet[alphabet.index(k) + 20],
        'v': alphabet[alphabet.index(k) + 21],
        'w': alphabet[alphabet.index(k) + 22],
        'x': alphabet[alphabet.index(k) + 23],
        'y': alphabet[alphabet.index(k) + 24],
        'z': alphabet[alphabet.index(k) + 25],
    }
    # print "using %s key number %d" % (keyString[x], x)
    m = keyString[x]
    en_letter = D[m]
    return en_letter

def encrypt_message(message, no_space, keyString, look_up):
    en_message = ""
    n = 0
    x = 0
    while len(en_message) < len(message):
        if message[n].isalpha():
            en_letter = look_up(no_space, keyString, x)
            en_message += en_letter   # append the encrypted message
            # no_space = no_space.lstrip(no_space[x])
            no_space = no_space[1:]
            x += 1
        else:
            # append the ecrypted message with non-alpha characters
            en_message += message[n]
        n += 1
    return en_message


if __name__ == '__main__':
    message = str(get_message())
    key = str(get_key())

    no_space = alpha_only(message)
    keyString = create_keyString(key, no_space)
    encrypted_message = encrypt_message(message, no_space, keyString, look_up)

    print message
    print encrypted_message
