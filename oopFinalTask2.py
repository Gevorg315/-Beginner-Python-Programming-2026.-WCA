from string import ascii_lowercase

class Cipher:
    def __init__(self, key):
        self.alphabet_with_keyword = self.from_crypted_alphabet(keyword=key)

    def encode(self, data):
        encoding_dict = dict(zip(ascii_lowercase, self.alphabet_with_keyword))
        return self.crypt(encoding_dict, data)

    def decode(self, data):
        decoding_dict = dict(zip(self.alphabet_with_keyword, ascii_lowercase))
        return self.crypt(decoding_dict, data)

    @staticmethod
    def crypt(dict_to_crypt, words):
        result_words = ""
        for char in words:
            key_char = dict_to_crypt.get(char.lower(), char)
            result_words += key_char.upper() if char.isupper() else key_char
        return result_words

    @staticmethod
    def from_crypted_alphabet(keyword):
        return keyword.lower() + "".join(
            (char for char in ascii_lowercase if char not in keyword.lower()),
        )


cipher = Cipher("crypto")

if __name__ == "__main__":
    assert cipher.encode("Hello, world!") == "Btggj, vjmgp!"
    assert cipher.decode("Fjedhc, dn atidsn") == "Kojima, is genius"
    assert cipher.decode("Btggj vjmgp!") == "Hello world!"