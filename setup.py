from setuptools import setup, find_packages

setup(
    name='nlp-blockchain',
    version='0.0.1',
    description="Natural Language Processing Blockchain",
    long_description="""\
        Provide long term persistent memory and training for NLP applications.
        The blockchain is the memory.  The smart contracts are the basis for
        AI on their own sub-chain.
    """,
    author='nickumia',
    packages=find_packages(include=['nlpchain'])
)
