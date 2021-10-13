import collections

rangeStart = ord(' ')
rangeEnd = ord('~') + 1
asciiDict = {(i - 32): chr(i) for i in range(rangeStart, rangeEnd)}
n_size = len(asciiDict)
characters = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def ord2(string):
    return (ord(string) - 32)


def vigenere_encrypt(text, key):
    encoded = []
    for i in range(len(text)):
        ciphered_i = asciiDict[(ord2(text[i]) + ord2(key[i%len(key)])) % n_size]
        encoded.append(ciphered_i)
    return ''.join(encoded)


def vigenere_decrypt(text, key):
    decoded = []
    for i in range(len(text)):
        message_i = asciiDict[(ord2(text[i]) - ord2(key[i%len(key)]) + n_size) % n_size]
        decoded.append(message_i)
    return ''.join(decoded)


def split_cipher(text, key_length):
    text_blocks = []
    for i in range(0, len(text), key_length):
        text_blocks.append(text[i:key_length + i])
    return text_blocks


def space_is_most_frequent(text):
    counter = collections.Counter(text)
    if counter.most_common(1)[0][0] == ' ':
        return True
    return False


def find_caesar_key(text):
    for key in characters:
        decrypted = vigenere_decrypt(text, key)
        if (space_is_most_frequent(decrypted)):
            return key


def find_key(text, key_length):
    text_blocks = split_cipher(text, key_length)
    ith_blocks = []
    for i in range(0, key_length):
        ith_blocks.append('')
    for i in range(0, key_length):
        for segment in text_blocks:
            try:
                ith_blocks[i] += segment[i]
            except:
                ith_blocks[i] += ''

    key = ''
    for segment in ith_blocks:
        key += find_caesar_key(segment)
    return key


if __name__ == '__main__':
    # Leitura texto 1 (chave de tamanho 4)
    file = open("texto_cripto_chave04.txt")
    texto1 = file.read()
    file.close()

    # Leitura texto 2 (chave de tamanho 20)
    file = open('texto_cripto_chave20.txt')
    texto2 = file.read()
    file.close()

    # Leitura texto base (texto não cifrado)
    file = open("texto.txt")
    texto3 = file.read()
    file.close()

    # Chave escolhida para cifrar o texto normal
    texto3_enc = vigenere_encrypt(texto3, "AboBoRa!")

    keyTexto1 = find_key(texto1, 4)
    keyTexto2 = find_key(texto2, 20)
    keyTexto3 = find_key(texto3_enc, 8)
    #print(vigenere_decrypt(texto1, keyTexto1))
    #print(vigenere_decrypt(texto2, keyTexto2))
    #print(vigenere_decrypt(texto3_enc, keyTexto3))
    print()
    print("Chave do texto de tamanho 4 = {}".format(keyTexto1))
    print("Chave do texto de tamanho 20 = {}".format(keyTexto2))
    print("Chave do texto normal = {}".format(keyTexto3))










