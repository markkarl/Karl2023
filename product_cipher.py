def productencrypt(plaintext, key, hashmap):
    plaintext2 = []

    for i in range(len(plaintext)):
        num = (
                list(hashmap.keys())[list(hashmap.values()).index(plaintext[i].upper())] + 2
        )
        if num >= 37:
            plaintext2.append(hashmap[num - 36])
        else:
            plaintext2.append(hashmap[num])

    permuted_chars = []

    for i in range(len(plaintext2)):
        permuted_chars.append(plaintext2[key[i] - 1]) #
    return "".join(permuted_chars)


def productdecrypt(ciphertext, key, hashmap):
    decrypted_chars = list(ciphertext)
    for i in range(len(ciphertext)):
        decrypted_chars[key[i] - 1] = ciphertext[i]

    for i in range(len(ciphertext)):
        num = (
                list(hashmap.keys())[list(hashmap.values()).index(decrypted_chars[i].upper())] - 2
        )
        if num <= 0:
            decrypted_chars[i] = hashmap[num + 36]
        else:
            decrypted_chars[i] = hashmap[num]
    return "".join(decrypted_chars)