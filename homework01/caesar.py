import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""

    for letter in plaintext:
        if ord(letter) in range(65, 88) or ord(letter) in range(97, 120):
            ch = ord(letter) + shift
            chletter = chr(ch)
        elif ord(letter) in range(88, 91) or ord(letter) in range(120, 123):
            ch = ord(letter) - 26 + shift
            chletter = chr(ch)
        else:
            chletter = letter
        ciphertext += chletter
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""

    for letter in ciphertext:
        if ord(letter) in range(68, 91) or ord(letter) in range(100, 123):
            pl = ord(letter) - shift
            pletter = chr(pl)
        elif ord(letter) in range(65, 68) or ord(letter) in range(97, 100):
            pl = ord(letter) + 26 - shift
            pletter = chr(pl)
        else:
            pletter = letter
        plaintext += pletter
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    words = ciphertext.split()
    for w in words:
        for i in range(0,26):
            dword=decrypt_caesar(word, i)
            if dword in dictionary:
                best_shift=i
    return best_shift
