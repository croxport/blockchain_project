from blockchain import Blockchain  # Import the Blockchain class from blockchain.py

# Initialize the blockchain
my_blockchain = Blockchain()

# Add some blocks with sample data
my_blockchain.add_block("Alice sends 5 coins to Bob")
my_blockchain.add_block("Bob sends 2 coins to Charlie")

# Print the blockchain
for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 30)

# Validate the blockchain
print("Is blockchain valid?", my_blockchain.is_chain_valid())
