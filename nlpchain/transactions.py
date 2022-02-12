
import binascii
from time import time

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class Client:
    def __init__(self, private_key=None, public_key=None):
        '''
        IN: private_key: binary format (PEM or DER)
        IN: public_key: binary format (PEM or DER)
        '''
        random = Crypto.Random.new().read
        if private_key is None:
            self._private_key = RSA.generate(1024, random)
            self._public_key = self._private_key.publickey()
        else:
            self._private_key = RSA.importKey(private_key)
            self._public_key = RSA.importKey(public_key)

        self._signer = PKCS1_v1_5.new(self._private_key)
        self._signer_public = PKCS1_v1_5.new(self._public_key)

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
