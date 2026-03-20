class MyHashSet:
    # new_set=[]

    def __init__(self):
        # self.new_set_size=500
        self.new_set=[False]*(10**6+1)
        

    def add(self, key: int) -> None:
        self.new_set[key]=True
        

    def remove(self, key: int) -> None:
        self.new_set[key]=False
        

    def contains(self, key: int) -> bool:
        return self.new_set[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)