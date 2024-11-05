from flask import Flask, jsonify, request, render_template
from blockchain import Blockchain

# Specify the custom template folder 'templates1'
app = Flask(__name__, template_folder='templates1')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('index1.html', blockchain=blockchain.chain)

@app.route('/mine', methods=['GET'])
def mine():
    # Run the Proof of Work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # Reward for finding the proof
    blockchain.new_transaction(
        sender="0",
        recipient="your_address",  # Mining reward is sent to the miner
        amount=1,
    )

    # Create a new Block and add it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # Check that the required fields are in the POSTed data
    required_fields = ['sender', 'recipient', 'amount']
    if not all(field in values for field in required_fields):
        return 'Missing values', 400

    # Create a new transaction
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/validate', methods=['GET'])
def validate_chain():
    is_valid = blockchain.chain_valid()
    if is_valid:
        response = {'message': 'The blockchain is valid.'}
    else:
        response = {'message': 'The blockchain is invalid.'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
