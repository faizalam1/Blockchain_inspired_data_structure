import time
import bencode

class Block:

    def __init__(self, id, data, previous_hash, hash, difficulty):
        self.hash = hash
        self.difficulty = difficulty
        self.block = {
            "Id": id,
            "Nonce":0,
            "Time": str(time.time()),
            "Data": data,
            "Previous Hash": previous_hash
            }
        self.valid_hash = "0000"

    def verify(self,shahash):
        if len(str(shahash)) != 64:
            return False
        elif int(shahash,16) > 2**(256-self.difficulty):
            return False
        return True

    def mine(self):
        for i in range(2**256):
            shahash = self.__hash(self.block)
            if self.verify(shahash):
                return shahash
            self.block["Nonce"] += 1

    def get_block(self):
        if self.valid_hash == "0000":
            self.valid_hash = self.mine()
            return [self.block,self.valid_hash]

    def __hash(self, data):
        return self.hash(bencode.bencode(data)).hexdigest()
