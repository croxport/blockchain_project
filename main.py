from blockchain import Blockchain
from transactions import create_wallet, create_transaction

#create wallets
alice_wallet = create_wallet()
bob_wallet = create_wallet()

# Initialize the blockchain
gold_blockchain = Blockchain()
print(f"Welcome to the {gold_blockchain.coin_name} Blockchain!")
print(f"Alice's Wallet: {alice_wallet}")
print(f"Bob's Wallet: {bob_wallet}")

# Add a transaction
transaction = create_transaction(alice_wallet, bob_wallet, 10)
gold_blockchain.add_transaction(transaction["sender"], transaction["receiver"], transaction["amount"])

# Mine the pending transactions
print(f"Mining transactions...")
gold_blockchain.mine_pending_transactions("Miner1")

# Add some transactions
gold_blockchain.add_transaction("Alice", "Bob", 10)
gold_blockchain.add_transaction("Charlie", "Alice", 5)

# Mine a block
print(f"Mining block for {gold_blockchain.coin_name}...")
gold_blockchain.mine_pending_transactions("Miner1")

# Add more transactions
gold_blockchain.add_transaction("Bob", "Charlie", 7)
gold_blockchain.add_transaction("Alice", "Charlie", 3)

# Mine another block
print(f"Mining another block for {gold_blockchain.coin_name}...")
gold_blockchain.mine_pending_transactions("Miner2")

# Print the blockchain
for block in gold_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Transactions: {block.transactions}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 30)

# Validate the blockchain
print("Is blockchain valid?", gold_blockchain.is_chain_valid())
