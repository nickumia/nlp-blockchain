
import hashlib
import json
from time import time

from .transactions import Transaction


class Blockchain:

    def __init__(self):
        self.chain = []
        self.unsettled_transactions = []
        self.nodes = set()

        self.new_block(previous_hash='nlp')

    def register_node(self, node_ip):
        pass

    def new_block(self, proof=None, previous_hash=None):
        for pending in self.unsettled_transactions:
            verifier = Transaction('unknown', 'unknown', 0)
            assert verifier.verify_transaction(pending['transaction'],
                pending['signature'], pending['transaction']['sender'])
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.unsettled_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.unsettled_transactions = []
        self.chain.append(block)

        return block

    def newest_block(self):
        return self.chain[-1]

    def new_transaction(self, s, r, v):
        '''
        IN: s: sender, instance(Client)
        IN: r: recipient, instance(Client)
        IN: v: value, int
        OUT: block index that transaction will be part of
        '''
        transaction = Transaction(s, r, v)
        verified_transaction = {
            'transaction': transaction.to_dict(),
            'signature': transaction.sign_transaction()
        }
        self.unsettled_transactions.append(verified_transaction)
        return self.newest_block()['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
