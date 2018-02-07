from Crypto.Hash import keccak


class keccak_256:
    def __init__(self, value):
        self.hash = keccak.new(digest_bits=256)
        self.hash.update(value)

    def digest(self):
        return self.hash.digest()


assert keccak_256(b'').digest() == b"\xc5\xd2F\x01\x86\xf7#<\x92~}\xb2\xdc\xc7\x03\xc0\xe5\x00\xb6S\xca\x82';\x7b\xfa\xd8\x04\x5d\x85\xa4p", "Incorrect sha3.  Make sure it's keccak"  # noqa: E501
