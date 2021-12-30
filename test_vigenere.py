from vigenere_cipher import vigenere_encode, vigenere_decode


def test_vigenere():
    # Running the vigenere encode test example.
    print('-' * 100)
    print('Running the vigenere encode test example.')
    plaintext = "As temperatures drop and daylight hours decrease, it's not unusual for people to express dread about the dark days ahead. Many of us also continue to work from home and spend much of our time indoors. Without the change of environment and personal interactions that workplaces can provide, it's even more difficult to escape the winter blues. For many, though, this time of year marks the onset of a more serious condition. Seasonal affective disorder, or SAD, is a type of depression that usually gets worse during the fall and winter."
    key = 'cryptii'
    print('The plaintext is:\n%s' % plaintext)
    print('The key is:\n%s' % key)
    ciphertext = vigenere_encode(plaintext, key)
    print('The ciphertext is:\n%s' % ciphertext)
    # Running the vigenere decode with key test example.
    print('-' * 100)
    print('Running the vigenere decode with key test example.')
    print('The ciphertext is:\n%s' % ciphertext)
    print('The key is:\n%s' % key)
    plaintext = vigenere_decode(ciphertext, key=key)
    print('The plaintext is:\n%s' % plaintext)
    # Running the vigenere decode with key length test example.
    print('-' * 100)
    keylen = 7
    print('Running the vigenere decode with key length test example.')
    print('The ciphertext is:\n%s' % ciphertext)
    print('The key length is:\n%s' % keylen)
    plaintext, possible_key = vigenere_decode(ciphertext, keylen=keylen)
    print('The plaintext is:\n%s' % plaintext)
    print('The possible key is:\n%s' % possible_key)
    # Running the vigenere decode without key and key length test example
    print('-' * 100)
    print('Running the vigenere decode without key and key length test example.')
    print('The ciphertext is:\n%s' % ciphertext)
    plaintext, possible_key = vigenere_decode(ciphertext)
    print('The plaintext is:\n%s' % plaintext)
    print('The possible key is:\n%s' % possible_key)


if __name__ == '__main__':
    test_vigenere()
