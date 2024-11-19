import hashlib

class Block:
    def __init__(self, index, timestamp, transactions, previous_hash):
        """
        Represents a single block in the blockchain.
        """
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions  # List of transactions
        self.previous_hash = previous_hash
        self.nonce = 0  # Proof of Work nonce
        self.hash = self.hash_block()

    def hash_block(self):
        """
        Generates a SHA-256 hash based on the block's content and nonce.
        """
        block_content = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Implements Proof of Work by finding a hash with a specific number of leading zeroes.
        """
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.hash_block()
