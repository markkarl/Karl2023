def rowencrypt(plaintext, key):
    ciphertext = []
    plaintexttable = []
    lenthnum = round(len(plaintext) / len(key))
    if len(plaintext) % len(key) != 0:
        lenthnum += 1
    for i in range(lenthnum):
        row = []
        for j in range(len(key)):
            num = i * len(key) + j
            if num < len(plaintext):
                row.append(plaintext[num])
            else:
                row.append(" ")
        plaintexttable.append(row)
    for i in range(len(key)):
        for j in range(lenthnum):
            ciphertext.append(plaintexttable[j][key[i] - 1])
    return "".join(ciphertext)


def rowdecrypt(ciphertext, key):
    plaintext = []
    ciphertexttable = []
    num = 0
    lenthnum = round(len(ciphertext) / len(key))
    for i in range(len(key)):
        col = []
        for j in range(lenthnum):
            if num < len(ciphertext):
                col.append(ciphertext[num])
                num += 1
            else:
                col.append(" ")
        ciphertexttable.append(col)

    rearrangedtable = []
    for i in range(len(key)):
        col = []
        for j in range(lenthnum):
            col.append(ciphertexttable[key.index(i + 1)][j])
        rearrangedtable.append(col)

    for i in range(lenthnum):
        for j in range(len(key)):
            if rearrangedtable[j][i] == " ":
                skip = 0
            else:
                plaintext.append(rearrangedtable[j][i])

    return "".join(plaintext)