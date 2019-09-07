import time
import bencode

class Block:

    def __init__(self, id, data, previous_hash, hash):
        self.hash = hash
        self.block = {
            "Id": id,
            "Time": str(time.time()),
            "Data": data,
            "Previous Hash": previous_hash
            }

    def get_block(self):
        return [self.block,self.__hash(self.block)]
    
    def __hash(self, data):
        return self.hash(bencode.bencode(data)).hexdigest()