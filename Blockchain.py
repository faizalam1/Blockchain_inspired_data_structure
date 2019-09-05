import hashlib
import time
import json

class Blockchain:

  """ Hash is by default sha256 but you can use sha3_256 sha3_512 blake2b sha512 shake_256 sha384 md5 sha1 sha3_384 blake2s sha224 shake_128 andsha3_224."""

  def __init__(self, hash="sha256"):
    self.hash_name = hash
    self.hash = eval(f"hashlib.{hash}()")
    self.len = 0
    self.previous_hash = "0000"
    self.blockchain = []

  def __len__(self):
    return self.len

  def __eq__(self,another):
    if self.blockchain == another.blockchain:
      return True
    return False

  def insert_block(self,data):
    new_block = {
        "Id":(self.len)+1,
        "Time":time.time(),
        "Data":data,
        "Previous Hash": self.previous_hash
    }
    hashed = str(self.__hash(new_block))
    self.previous_hash = hashed
    self.len += 1
    self.blockchain.append((new_block,hashed))
    return True

  def __hash(self,block):
    data = json.dumps(block).encode()
    self.hash.update(data)
    return self.hash.hexdigest()

  def verify(self):
    for i in range(self.len):
      if i != 0:
        if self.blockchain[i][0]["Previous Hash"] != self.blockchain[i-1][1]:
          return False
      else:
        if self.blockchain[i][0]["Previous Hash"] != "0000":
          return False
    if self.previous_hash != self.blockchain[(self.len)-1][1]:
      return False
    return True

  def save(self,filename="./.blockchain.json"):
    if not(self.verify()):
      return "Blockchain Not Valid"
    with open(filename,"w") as file:
      data = {
          "self.blockchain":self.blockchain,
          "self.hash":f"hashlib.{self.hash_name}()",
          "self.len" : self.len,
          "self.hash_name":self.hash_name,
          "self.previous_hash":self.previous_hash
      }
      json.dump(data,file)
      return True

  def load(self,filename="./.blockchain.json"):
    with open(filename) as file:
      data = json.load(file)
    self.blockchain = [tuple(data["self.blockchain"][i]) for i in range(len(data["self.blockchain"]))]
    self.len = data["self.len"]
    self.hash_name = data["self.hash_name"]
    self.hash = eval(data["self.hash"])
    self.previous_hash = data["self.previous_hash"]
    if not(self.verify()):
      return "Blockchain Not Valid"
    return True