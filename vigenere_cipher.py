def table3(table, hashmap):
    letters_and_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(len(letters_and_digits)):
        row = []
        for j in range(len(letters_and_digits)):
            letter = (i + j) % len(letters_and_digits)
            row.append(letters_and_digits[letter])
        table.append(row)
    for i in range(37):
        if i == 36:
            hashmap[i] = " "
        else:
            hashmap[i] = letters_and_digits[i]


def vigerenencrypt(plaintext, key, hashmap, table):
    ciphertext = []
    for i in range(len(plaintext)):
        row = list(hashmap.keys())[list(hashmap.values()).index(plaintext[i].upper())]
        column = list(hashmap.keys())[list(hashmap.values()).index(key[i])]

        ciphertext.append(table[row][column])
    return "".join(ciphertext)


def decrypt(ciphertext, key, hashmap, table):
    plaintext = []
    for i in range(len(ciphertext)):
        key_row = list(hashmap.keys())[list(hashmap.values()).index(key[i])]
        table_row = table[key_row].index(ciphertext[i])
        plaintext.append(hashmap[table_row])
    return "".join(plaintext)