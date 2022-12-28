import os
from blockchain_parser.blockchain import Blockchain

# Instantiate the Blockchain by giving the path to the directory
# containing the .blk files created by bitcoind
blockchain = Blockchain(os.path.expanduser('/mnt/d/Bitcoin/blocks'))

# Get the first block
block_height = 1
for block in blockchain.get_unordered_blocks():
    print("Block Height:", block_height)
# Get the first transaction in the block (the coinbase transaction)
    coinbase_tx = block.transactions[0]
    # Get the first input in the transaction (the coinbase field)
    coinbase_input = coinbase_tx.inputs[0]
    # Get the script of the input (the coinbase message)
    script = coinbase_input.script
    # Extract the meqssage from the script
    hex_message = str(script).replace(" ","")[7:-1]
    # Verify message length
    hex_message_length = len(hex_message)
    print("Hexa Length:", hex_message_length)
    # Decode the message
    try:
        if hex_message_length != 0:
            if (hex_message_length % 2) != 0:
                hex_message = hex_message[1:]
            if hex_message_length > 16:
                hex_message = hex_message[10:]
            else:
                hex_message = hex_message[4:]
            clear_message = bytes.fromhex(hex_message).decode('ascii')
            if any(char.isalpha() or char.isdigit() for char in clear_message):
                print("Miner's message:", clear_message)
            else:
                print("Miner's message: NONE")
    # Catch exception if miner didn't specify valid message
    except ValueError:
        print("Miner's message:", hex_message)
    # Increment block number
    block_height += 1
    # Stop processing blocks - will only decode Satoshi's genesis block message
    # break
