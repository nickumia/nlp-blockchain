
from nlpchain.nlp import Blockchain
from nlpchain.transactions import Client

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256


def test_blockchain_init():
    a = Blockchain()

    assert len(a.chain) == 1
    assert a.newest_block()['index'] == 1
    assert a.newest_block()['previous_hash'] == 'nlp'
    assert a.nodes == set()


def test_client_init():
    a = Client()

    assert a._private_key != a._public_key


def test_transaction():
    A = Blockchain()
    a = Client()
    b = Client()

    A.new_transaction(a, b, 100)
    new_block = A.new_block()
    assert new_block['index'] == 2
    assert new_block['transactions'][0]['transaction']['sender'] == a.identity
    assert new_block['transactions'][0]['transaction']['recipient'] == \
        b.identity


def test_importkey():
    filepath = 'test.pem'
    with open(filepath, 'wb') as outar:
        outar.write(RSA.generate(2048).export_key('PEM'))

    a = Client(private_key=filepath)

    message = b'Test Message'
    message_hash = SHA256.new(message)
    signature = a._signer.sign(message_hash)

    try:
        a._signer_public.verify(message_hash, signature)
    except (ValueError, TypeError):
        print("The signature is not valid.")
