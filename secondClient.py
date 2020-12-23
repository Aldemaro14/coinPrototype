#_*_ coding: utf-8 _*_
"""
Created on Sun December 12 13:53:28 2020

@author Aldemaro Cruz
"""

#Import the libraries
from flask import Flask, request
from flask.json import jsonify

from uuid import uuid4

from flask.wrappers import Response
from blockchain import Blockchain
# mining and API

# Creating a Web App
app = Flask(__name__)

#Create an address for the node on Port 5000
node_address = str(uuid4()).replace('-', '')

# Creating a Blockchain
blockchain = Blockchain()

# Mining a new block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender = node_address, receiver = 'Second User', amount = 2) 
    block = blockchain.create_block(proof, previous_hash)
    response:dict = {
        'message' : 'Congratulations, you just mined a block',
        'index' : block['index'],
        'timestamp' : block['timestamp'],
        'proof' : block['proof'],
        'previous_hash' : block['previous_hash'],
        'transactions' : block['transactions']
    } 

    return jsonify(response), 200

# Getting the full Blockchain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain' : blockchain.chain,
        'length' : len(blockchain.chain)
    }
    return jsonify(response), 200

# Checking if the Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200

#Adding a new transaction to the blockchain
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
    json = request.get_json()
    transactions_keys = ['sender', 'receiver', 'amounrt']
    if not all (key in json for key in transactions_keys):
        return 'Some elements of the transaction are missing', 400
    index = blockchain.add_transaction(json['sender'], json['receiver'], json['amount'])
    response = {'message' : f'This transaction will be added to Block {index}'}
    return jsonify(response), 201

#Decentralizing our Blockchain
#Connecting new nodes
@app.route('/connect_node', methods = ['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return 'No node', 400
    for node in nodes:
        blockchain.add_node(node)
    response = {
        'message' : 'All the nodes are now connected. The CetaCoin now contains the following nodes:',
        'total_nodes' : list(blockchain.nodes)
    }
    return jsonify(response), 200

#Replacing the chain by the longest chain if needed
@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
    is_chain_replaced = blockchain.is_chain_valid(blockchain.chain)
    if is_chain_replaced:
        response = {
            'message': 'The nodes had different chains so the chain was replaced by the longest one.',
            'new_chain' : blockchain.chain
        }
    else:
        response = {
            'message': 'All good, the chain is the largest one.',
            'actual_chain' : blockchain.chain
        }
    return jsonify(response), 200
# Running the app
app.run(host = '0.0.0.0', port = 7000)

if __name__ == '__main__':
    app.run()