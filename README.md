# Blockchain Implementation in Python

This project simulates a basic blockchain system in Python, showcasing fundamental blockchain concepts such as cryptographic hashing, Proof of Work (PoW), and blockchain validation. It demonstrates how a blockchain works by storing data in blocks that are linked together to form a chain. Each block contains a list of transactions and is secured using cryptographic hashing. 

## Key Features

- **Blockchain Structure**: Each block contains the following:
  - A list of transactions.
  - A timestamp of when the block was created.
  - A cryptographic hash of the previous block.
  - A Proof of Work (PoW) to secure the block.
  
- **Cryptographic Hashing**: Blocks are hashed using the SHA-256 algorithm to ensure data integrity and prevent tampering. If a block is altered, its hash changes, breaking the entire chain.
  
- **Proof of Work**: A simple Proof of Work algorithm is implemented to add new blocks. This process involves finding a valid proof that satisfies a certain condition (e.g., a hash with four leading zeros).
  
- **Transaction Handling**: Users can add transactions (e.g., transfer money) to the blockchain. Each transaction is validated and added to the next block.

- **Chain Validation**: The blockchain includes a validation method to ensure that the chain is tamper-proof and all blocks are correctly linked.

## How it Works

1. **Genesis Block**: The first block in the blockchain is created with a hardcoded proof of `100` and a previous hash of `'1'`.

2. **Adding Transactions**: You can create transactions where one user sends money (or any other data) to another user. Transactions are added to the block and are validated before being included in the chain.

3. **Proof of Work**: A new block can only be added to the blockchain if the current block's proof and the next proof satisfy the PoW condition. This ensures that creating new blocks requires computational work and prevents fraudulent blocks from being added.

4. **Chain Validation**: The `chain_valid()` function ensures the blockchain is intact by checking if each block's hash matches the previous block's hash, and if the proof of work is correct for each block.

## This project is implemented using python and flask.

