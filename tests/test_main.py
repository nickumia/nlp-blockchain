
from nlpchain.nlp import Blockchain
from nlpchain.transactions import Client


def test_blockchain_init():
    a = Blockchain()

    assert a.chain == []
    assert a.nodes == set()


def test_client_init():
    a = Client()

    assert a._private_key != a._public_key
