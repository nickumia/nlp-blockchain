
import binascii
from time import time

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:
    def __init__(self):
        random = Crypto.Random.new().read
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(
            format='DER')).decode('ascii')


class Transaction:
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.time = time()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return {'sender': identity,
                'recipient': self.recipient.identity,
                'value': self.value,
                'time': self.time}

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

    @staticmethod
    def verify_transaction(transaction, signature, public_key):
        verifier = PKCS1_v1_5.new(
            RSA.importKey(binascii.unhexlify(public_key.encode('ascii')))
        )
        h = SHA.new(str(transaction).encode('utf8'))

        if verifier.verify(h, binascii.unhexlify(signature.encode('ascii'))):
            return True
        return False
