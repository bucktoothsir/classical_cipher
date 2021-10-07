from __future__ import division
import string

ALPHABET = string.ascii_lowercase
LENGTH_OF_ALPHABET = 26
IC_OF_ENGLISH = 0.06
IC_OF_ENGLISH_VIGENERE_GROUP = 0.05
CHAR_TO_IDX = dict(zip(ALPHABET, range(LENGTH_OF_ALPHABET)))
IDX_TO_CHAR = dict(zip(range(LENGTH_OF_ALPHABET), ALPHABET))
LETTER_FREQUENCIES_OF_ENGLISH = {
    'e': 0.126,
    't': 0.0937,
    'a': 0.0834,
    'o': 0.077,
    'n': 0.068,
    'i': 0.0671,
    'h': 0.0611,
    's': 0.0611,
    'r': 0.0568,
    'l': 0.0424,
    'd': 0.0414,
    'u': 0.0285,
    'c': 0.0273,
    'm': 0.0253,
    'w': 0.0234,
    'y': 0.0204,
    'f': 0.0203,
    'g': 0.0192,
    'p': 0.0166,
    'b': 0.0154,
    'v': 0.0106,
    'k': 0.0087,
    'j': 0.0023,
    'x': 0.0020,
    'q': 0.0009,
    'z': 0.0006
    }


def count_letter_frequency(text):
    """Count the frequency of each letter in the input text

    Args:
        text: string instance
    Returns:
        A List containing items(letter(lower_case), frequency), sorting by the percentage in the descending order.
    """
    letter_to_freq = dict(zip(ALPHABET, [0]*LENGTH_OF_ALPHABET))

    for c in text:
        c = c.lower()
        if c in ALPHABET:
            letter_to_freq[c] += 1

    letter_and_freq_sorted = sorted(letter_to_freq.items(), key=lambda a:(-a[1],a[0]))
    return letter_and_freq_sorted


def count_letter_percentage(text):
    """Count the frequency percentage of each letter in the input text

    Args:
        text: string instance

    Returns:
        A List containing items(letter(lower_case), percentage), sorting by the percentage in the descending order.
        [('d', 0.08), ('x', 0.16), ...]
    """
    letter_and_freq_sorted = count_letter_frequency(text)
    letter_to_per = dict(zip(ALPHABET, [0]*LENGTH_OF_ALPHABET))
    all_num_of_char = 0

    for item in letter_and_freq_sorted:
        all_num_of_char += item[1]
    for item in letter_and_freq_sorted:
        letter, freq = item
        letter_to_per[letter] = freq / all_num_of_char
    letter_and_per_sorted = sorted(letter_to_per.items(), key=lambda a:(-a[1],a[0]))
    return letter_and_per_sorted


def index_of_coincidence(text):
    """cal the IC of test

       IC = \sigma_{i=A}^{i=Z} count_i * (count_i - 1) / N * (N - 1))

       N is the length of letters(a-z) in the text

    Args:
        text: string instance

    Returns:
        index_of_coincidence: float
    """
    letter_and_freq_sorted = count_letter_frequency(text)
    print(letter_and_freq_sorted)
    ic = 0
    for item in letter_and_freq_sorted:
        ic += item[1] * (item[1] - 1)
    n = 0
    for c in text:
        if c.lower() in ALPHABET:
            n += 1
    ic /= n * (n - 1)
    return ic

def get_single_key_and_mutual_ic(letter_and_per_sorted):
    """
    Return best key with the max mutual ic.
    For the Caecar cipher, the possible key in the range of [0, 25]

    Args:
        letter_and_per_sorted: A List containing items(letter(lower_case), percentage), sorting by the percentage in the descending order.
    Return:
        A list containing [best_key(int), best_mutual_ic(float)]
    """
    #key_to_mutual_ic = dict(zip(range(1, LENGTH_OF_ALPHABET), [0]*LENGTH_OF_ALPHABET))
    best_single_key = ''
    best_mutual_ic = 0
    for i in range(1, LENGTH_OF_ALPHABET):
        mutual_ic = 0
        for item in letter_and_per_sorted:
            letter, per = item
            mutual_ic += LETTER_FREQUENCIES_OF_ENGLISH[IDX_TO_CHAR[(CHAR_TO_IDX[letter] - i) % LENGTH_OF_ALPHABET]] * per
        if best_mutual_ic < mutual_ic:
            best_mutual_ic = mutual_ic
            best_single_key = i
    return [best_single_key, best_mutual_ic]

