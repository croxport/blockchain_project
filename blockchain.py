import time
from block import Block

class Blockchain:
    def __init__(self):
        self.coin_name = "GoldCoin"
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []  # List of unprocessed transactions
        self.difficulty = 4  # Adjust difficulty as needed
        self.mining_reward = 50  # Reward for mining a block
        self.max_supply = 10000  # Max supply of coins
        self.total_mined = 0  # Total coins mined

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

    def add_transaction(self, sender, receiver, amount):
        """
        Adds a new transaction to the list of pending transactions.
        """
        transaction = {"sender": sender, "receiver": receiver, "amount": amount}
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        """
        Mines all pending transactions into a new block and rewards the miner.
        """
        # Reward the miner
        if self.total_mined + self.mining_reward <= self.max_supply:
            reward_transaction = {
                "sender": "System",
                "receiver": miner_address,
                "amount": self.mining_reward,
                "coin": self.coin_name  # Include the coin name in transactions
            }
            self.pending_transactions.append(reward_transaction)

        # Create a new block with pending transactions
        new_block = Block(len(self.chain), time.time(), self.pending_transactions, self.get_latest_block().hash)
        new_block.mine_block(self.difficulty)

        # Add the new block to the chain
        self.chain.append(new_block)
        self.pending_transactions = []  # Clear pending transactions

        # Update total mined coins
        self.total_mined += self.mining_reward

        print(f"Block mined! {self.mining_reward} {self.coin_name} rewarded to {miner_address}")

    def is_chain_valid(self):
        """
        Validates the blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.hash_block():
                print(f"Block {current_block.index} has been tampered with!")
                return False

            if current_block.previous_hash != previous_block.hash:
                print(f"Block {current_block.index} is not linked to Block {previous_block.index}!")
                return False

        return True

