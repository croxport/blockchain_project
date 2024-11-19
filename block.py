import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """
        Represents a single block in the blockchain.
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """
        Generates a SHA-256 hash based on the block's content.
        """
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()

