import uuid

def create_wallet():
    """
    Simulates the creation of a wallet by generating a unique public key.
    """
    return str(uuid.uuid4())

def create_transaction(sender, receiver, amount):
    """
    Creates a transaction dictionary.
    """
    return {"sender": sender, "receiver": receiver, "amount": amount}
