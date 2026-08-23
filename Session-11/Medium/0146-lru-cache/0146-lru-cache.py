class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict[key] = self.dict.pop(key) # 최근 사용 갱신

        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
        
        self.dict[key] = value
        if len(self.dict) > self.size:
            self.dict.pop(next(iter(self.dict)))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)