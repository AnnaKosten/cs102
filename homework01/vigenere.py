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

    keyword = keyword.lower

    for l, ch in enumerate(plaintext):
        ch = ord(plaintext[l])
        key = ord(keyword[l % len(keyword)])
        if ch in range(65, 91):
            ciphertext += chr(((ch - 65) + (key - 97)) % 26 + 65)
        elif ch in range(97, 123):
            ciphertext += chr(((ch - 97) + (key - 97)) % 26 + 97)
        else:
            ciphertext += chr(ch)
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

    keyword = keyword.lower

    for l, ch in enumerate(ciphertext):
        ch = ord(ciphertext[l])
        key = ord(keyword[l % len(keyword)])
        if ch in range(65, 91):
            plaintext += chr(((ch - 65) - (key - 97)) % 26 + 65)
        elif ch in range(97, 123):
            plaintext += chr(((ch - 97) - (key - 97)) % 26 + 97)
        else:
            plaintext += chr(ch)
    return plaintext
