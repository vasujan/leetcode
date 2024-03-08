import random

class RandomizedSet:

    def __init__(self):
        self.dict = dict()
        self.list = list()
        self.count = 0

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = self.count
        self.list.append(val)
        self.count += 1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        idx = self.dict.pop(val)
        self.list[idx] = None
        last_elem = self.list.pop()
        self.count -= 1
        if idx < self.count:
            self.list[idx] = last_elem
            self.dict[last_elem] = idx
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()