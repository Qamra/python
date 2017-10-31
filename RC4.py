def rc4(data, key):
    '''

        data:    data that to be encrypted or decrypted.

        key:     key to encrypt or decrypt.

    '''

    # some parameters check here ...



    # if the data is a string, convert to hex format.

    if (type(data) is type("string")):

        tmpData = data

        data = []

        for tmp in tmpData:
            data.append(ord(tmp))

    # if the key is a string, convert to hex format.

    if (type(key) is type("string")):

        tmpKey = key

        key = []

        for tmp in tmpKey:
            key.append(ord(tmp))

    # the Key-Scheduling Algorithm

    x = 0

    box = list(range(256))

    for i in range(256):
        x = (x + box[i] + key[i % len(key)]) % 256

        box[i], box[x] = box[x], box[i]

    # the Pseudo-Random Generation Algorithm

    x = 0

    y = 0

    out = []

    for c in data:
        x = (x + 1) % 256

        y = (y + box[x]) % 256

        box[x], box[y] = box[y], box[x]

        out.append(c ^ box[(box[x] + box[y]) % 256])

    result = ""

    printable = True

    for tmp in out:

        if (tmp <0x21 or tmp > 0x7e):

            # there is non-printable character

            printable = False

            break

        result += chr(tmp)

    if (printable == False):

        result = ""

        # convert to hex string

        for tmp in out:
            result += "{0:02X}".format(tmp)

    return result

out=rc4("chenqiutong", "writingcode")

print("chenqiutong encryption:{}".format(out))

out=rc4([0xD3,0x33,0xBB,0x0A,0x8B,0x3E,0x72,0xD5,0x4D,0x83,0x36], "writingcode")

print("[0xD3,0x33,0xBB,0x0A,0x8B,0x3E,0x72,0xD5,0x4D,0x83,0x36] decryption:{}".format(out))