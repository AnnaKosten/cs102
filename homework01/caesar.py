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
        if ord("A") <= ord(letter) <= ord("Z"):
            ciphertext += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
        elif ord("a") <= ord(letter) <= ord("z"):
            ciphertext += chr((ord(letter) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += letter
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
        if ord("A") <= ord(letter) <= ord("Z"):
            plaintext += chr((ord(letter) - ord("A") - shift) % 26 + ord("A"))
        elif ord("a") <= ord(letter) <= ord("z"):
            plaintext += chr((ord(letter) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += letter
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    words = ciphertext.split()
    for w in words:
        for i in range(0, 26):
            dword = decrypt_caesar(w, i)
            if dword in dictionary:
                best_shift = i
    return best_shift
