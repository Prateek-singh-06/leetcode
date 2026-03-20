class MyHashSet:
    # new_set=[]

    def __init__(self):
        self.new_set=[]
        

    def add(self, key: int) -> None:
        if(self.contains(key)):
            return None
        else:
            self.new_set.append(key)
        

    def remove(self, key: int) -> None:
        if(self.contains(key)==False):
            return None
        else:
            self.new_set.remove(key)
        

    def contains(self, key: int) -> bool:
        for num in self.new_set:
            if(num==key):
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)