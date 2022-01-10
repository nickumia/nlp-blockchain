
import hashlib
import json
from time import time

from .transactions import Transaction


class Blockchain:

    def __init__(self):
        self.chain = []
        self.unsettled_transactions = []
        self.nodes = set()

    def register_node(self, node_ip):
        pass

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
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
        self.pending_transactions.append(Transaction(s, r, v))
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
