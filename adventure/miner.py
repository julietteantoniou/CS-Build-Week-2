import hashlib
import requests

import sys

from uuid import uuid4

from timeit import default_timer as timer

import random
import json
import time


def proof_of_work():
    r = requests.get("https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/", headers = {"Authorization": "Token bbb8cd4675926440ab7b37235d10b7a244415937"})
    res = r.json()
    last_proof = res['proof']
    difficulty = res['difficulty']
    print(last_proof)
    time.sleep(1)
    start = timer()

    print("Searching for next proof")
    proof = 17
    counter = 0

    while valid_proof(proof, last_proof, difficulty) is False:
        counter += 1
        proof = counter * random.getrandbits(7)
        # if counter > 2500000:
        #      return proof

    print("Proof found: " + str(proof) + " in " + str(timer() - start))
    return proof


def valid_proof(proof, last_proof, difficulty):
   
    # r = requests.get("https://lambda-treasure-hunt.herokuapp.com/api/bc/last_proof/", headers = {"Authorization": "Token bbb8cd4675926440ab7b37235d10b7a244415937"})
    # res = r.json()
    # # print(res)
    # time.sleep(1)
    # last_proof = res['proof']
    # difficulty = int(res['difficulty'])

    # prev_proof = f'{last_hash}'.encode()
    # prev_hash = hashlib.sha256(last_hash).hexdigest()
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    zeros = '0' * difficulty
    if guess_hash[:difficulty] == zeros:
        print(guess_hash)
    return guess_hash[:difficulty] == zeros

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-treasure-hunt.herokuapp.com/api/bc/mine/"

    coins_mined = 0

    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        # r = requests.get(url=node + "/last_proof")
        # data = r.json()
        headers = {"Authorization": "Token bbb8cd4675926440ab7b37235d10b7a244415937"}
        new_proof = proof_of_work()

        post_data = {"proof": new_proof}

        r = requests.post(url=node, json=post_data, headers = headers)
        data = r.json()
        cooldown = data['cooldown']
        time.sleep(cooldown)
        print(data, post_data)
  
        print(data.get('message'))
