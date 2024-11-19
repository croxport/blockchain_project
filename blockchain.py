import time
from block import Block  # Import the Block class from block.py

class Blockchain:
    def __init__(self):
        """
        Initializes the blockchain with a genesis block.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Creates the first block in the blockchain with predefined values.
        """
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Retrieves the most recent block in the blockchain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Adds a new block to the blockchain with the provided data.
        """
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Validates the blockchain by checking each block's hash and linkage.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check the current block's hash
            if current_block.hash != current_block.hash_block():
                print(f"Block {current_block.index} has been tampered with!")
                return False

            # Check the linkage to the previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} is not linked to Block {previous_block.index}!")
                return False

        return True

