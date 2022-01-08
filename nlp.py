
import hashlib
import json


class Blockchain:

    def __init__(self):
        self.chain = []
        self.unsettled_transactions = []
        self.nodes = set()

    def register_node(self, node_ip):
        pass

    def new_block(self):
        pass

    def newest_block(self):
        return self.chain[-1]

    def new_transaction(self):
        pass

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
