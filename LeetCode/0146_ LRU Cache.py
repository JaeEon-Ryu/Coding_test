'''
1. Use dictionary datatypes to store value for key
2. For data types, use FIFO(First In-First Out) data structure
'''

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            k,v = key,self.cache[key] # key, value
            del self.cache[k] # Sent to the back because you used it
            self.cache[k] = v
            return v
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        if len(self.cache) >= self.capacity:
            for k in self.cache: # To remove the first element
                del self.cache[k]
                break
        self.cache[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)