
import hashlib
import os

import nlpchain


def software_hash():
    core_files = [
        '/nlp.py',
        '/node.py',
        '/transactions.py',
    ]

    path = os.path.dirname(nlpchain.__file__)
    software = b''
    for soft_file in core_files:
        with open(path+soft_file, 'rb') as in_tar:
            software += in_tar.read()

    h = hashlib.sha512()
    h.update(software)
    return h.digest()
