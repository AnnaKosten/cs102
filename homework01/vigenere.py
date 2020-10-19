import string


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""

    alphabet_len = len(string.ascii_lowercase)

    for i in range(len(plaintext)):
        k = i % (len(keyword))
        shift = 0
        if keyword[k] in string.ascii_uppercase:
            shift = ord(keyword[k]) - ord("A")
        else:
            shift = ord(keyword[k]) - ord("a")
        ch = plaintext[i]
        if ch in string.ascii_letters:
            if (ch in string.ascii_lowercase) and (ord(ch) + shift > ord("z")):
                ciphertext += chr(ord(ch) - alphabet_len + shift)
            elif (ch in string.ascii_uppercase) and (ord(ch) + shift > ord("Z")):
                ciphertext += chr(ord(ch) - alphabet_len + shift)
            else:
                ciphertext += chr(ord(ch) + shift)
        else:
            ciphertext += ch

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    alphabet_len = len(string.ascii_lowercase)

    for i in range(len(ciphertext)):
        k = i % (len(keyword))

        shift = 0
        if keyword[k] in string.ascii_uppercase:
            shift = ord(keyword[k]) - ord("A")
        else:
            shift = ord(keyword[k]) - ord("a")
        ch = ciphertext[i]
        if ch in string.ascii_letters:
            if (ch in string.ascii_lowercase) and (ord(ch) - shift < ord("a")):
                plaintext += chr(ord(ch) + alphabet_len - shift)
            elif (ch in string.ascii_uppercase) and (ord(ch) - shift < ord("A")):
                plaintext += chr(ord(ch) + alphabet_len - shift)
            else:
                plaintext += chr(ord(ch) - shift)
        else:
            plaintext += ch

    return plaintext
