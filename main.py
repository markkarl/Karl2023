import random


def table3():
    # Create a list to store the table
    letters_and_digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for i in range(len(letters_and_digits)):
        row = []
        # Loop through the letters and digits and create a list for each row
        for j in range(len(letters_and_digits)):
            letter = (i + j) % len(letters_and_digits)
            row.append(letters_and_digits[letter])

        # Add the row to the table
        table.append(row)
    # Create a hashmap that maps integers to letters and digits
    for i in range(37):
        if i == 36:
            hashmap[i] = " "
        else:
            hashmap[i] = letters_and_digits[i]


def vigerenencrypt(plaintext, key):
    # Create a list to store the ciphertext
    ciphertext = []
    # Loop through the plaintext
    for i in range(len(plaintext)):
        # Get the corresponding row and column of the plaintext character
        row = list(hashmap.keys())[list(hashmap.values()).index(plaintext[i].upper())]
        column = list(hashmap.keys())[list(hashmap.values()).index(key[i])]

        ciphertext.append(table[row][column])
    # Return the ciphertext as a string
    return "".join(ciphertext)


def rowencrypt(plaintext, key):
    # Create a list to store the ciphertext
    ciphertext = []
    plaintexttable = []
    # Loop through the plaintext
    lenthnum = round(len(plaintext) / len(key))
    if len(plaintext) % len(key) != 0:
        lenthnum += 1
    # Create a 2D list to store the table
    for i in range(lenthnum):
        row = []
        for j in range(len(key)):
            num = i * len(key) + j
            if num < len(plaintext):
                row.append(plaintext[num])
            else:
                row.append(" ")
        plaintexttable.append(row)
        # Add the row to the table
    for i in range(len(key)):
        for j in range(lenthnum):
            ciphertext.append(plaintexttable[j][key[i] - 1])
    # Return the ciphertext as a string
    return "".join(ciphertext)


# this uses ceaser cipher and permutates the order of the characters in the encrypted message
def productencrypt(plaintext, key):
    plaintext2 = []
    for i in range(len(plaintext)):
        num = (
                list(hashmap.keys())[list(hashmap.values()).index(plaintext[i].upper())] + 2
        )
        if num >= 37:
            plaintext2.append(hashmap[num - 36])
        else:
            plaintext2.append(hashmap[num])

    # Permute the order of the characters in the list
    permuted_chars = []
    for i in range(len(plaintext2)):
        permuted_chars.append(plaintext2[key[i] - 1])
    # Convert the permuted list of characters back to a string
    return "".join(permuted_chars)


def productdecrypt(ciphertext, key):
    # Permute the order of the characters in the encrypted message to decrypt it
    decrypted_chars = list(ciphertext)
    for i in range(len(ciphertext)):
        decrypted_chars[key[i] - 1] = ciphertext[i]

    # decrypt ceaser cipher
    for i in range(len(ciphertext)):
        num = (
                list(hashmap.keys())[list(hashmap.values()).index(decrypted_chars[i].upper())] - 2
        )
        if num <= 0:
            decrypted_chars[i] = hashmap[num + 36]
        else:
            decrypted_chars[i] = hashmap[num]
    # Convert the list of characters back to a string
    return "".join(decrypted_chars)


def rowdecrypt(ciphertext, key):
    # Create a list to store the plaintext
    plaintext = []
    ciphertexttable = []
    num = 0
    # Loop through the ciphertext
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

    # Rearrange the columns of the ciphertext table using the key
    rearrangedtable = []
    for i in range(len(key)):
        col = []
        for j in range(lenthnum):
            col.append(ciphertexttable[key.index(i + 1)][j])
        rearrangedtable.append(col)

    # Extract the plaintext from the rearranged table
    for i in range(lenthnum):
        for j in range(len(key)):
            if rearrangedtable[j][i] == " ":
                skip = 0
            else:
                plaintext.append(rearrangedtable[j][i])

    # Return the plaintext as a string
    return "".join(plaintext)


def decrypt(ciphertext, key):
    # Create a list to store the plaintext
    plaintext = []
    # Loop through the ciphertext
    for i in range(len(ciphertext)):
        # Get the corresponding row of the key character
        key_row = list(hashmap.keys())[list(hashmap.values()).index(key[i])]
        table_row = table[key_row].index(ciphertext[i])
        plaintext.append(hashmap[table_row])
    # Return the plaintext as a string
    return "".join(plaintext)


table = []
hashmap = {}
table3()
plaintext = input("Enter the plaintext: ")
key = ""
plain = ""
for i in range(len(plaintext)):
    y = random.randint(0, 35)
    key += hashmap[y]
    if plaintext[i] == " ":
        key = key[:-1]
    else:
        plain += plaintext[i]
encrypted = vigerenencrypt(plain, key)
key2 = 0
num = round(len(plaintext) / 5)
for i in range(num):
    y = random.randint(1, num)
    # use a list to store the key
    if key2 == 0:
        key2 = []
    else:
        while y in key2:
            y = random.randint(1, num)
    key2.append(y)
encrypted2 = rowencrypt(encrypted, key2)
key3 = 0
for i in range(len(encrypted2)):
    y = random.randint(1, len(encrypted2))
    # use a list to store the key
    if key3 == 0:
        key3 = []
    else:
        while y in key3:
            y = random.randint(1, len(encrypted2))
    key3.append(y)
encrypted3 = productencrypt(encrypted2, key3)
decrypted3 = productdecrypt(encrypted3, key3)
decrypted2 = rowdecrypt(decrypted3, key2)
decrypted = decrypt(decrypted2, key)
num1 = 8049367138491
num2 = list(range(5))
print(num2)
print("Your encrypted vigeren text is:", encrypted, "with key:", key)
print(hashmap)
print("Your decrypted vigeren text is:", decrypted)
print("Your encrypted row text is:", encrypted2, "with key:", key2)
print("Your decrypted row text is:", decrypted2)
print("Your encrypted product text is:", encrypted3, "with key:", key3)
print("Your decrypted product text is:", decrypted3)
