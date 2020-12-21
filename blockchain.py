#_*_ coding: utf-8 _*_
"""
Created on Sun December 12 13:53:28 2020

@author Aldemaro Cruz
"""

#Import the libraries
import datetime
import hashlib
import json
from flask import jsonify

# blockchain class Core

class Blockchain:

    def __init__(self) -> None:
        self.chain:list = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash) -> list:
        block:dict = {
            'index' : len(self.chain) + 1,
            'timestamp' : str(datetime.datetime.now()),
            'proof' : proof,
            'previous_hash' : previous_hash
        }

        self.chain.append(block)
        return block

    def get_previous_block(self) -> list:

        return self.chain[-1]

    def proof_of_work(self, previous_proof) -> bool:

        new_proof:int = 1
        check_proof:bool = False

        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):

        encoded_block = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(encoded_block).hexdigest()

    
    def is_chain_valid(self, chain) -> bool:

        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['block']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True


