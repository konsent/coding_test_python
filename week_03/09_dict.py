class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        self.items[hash(key) % len(self.items)] = value
        #index = hash(key) % len(self.items)  이렇게 나눠서 해도 됨
        #self.items[index] = value
        return

    def get(self,key):
        return self.items[hash(key) % len(self.items)]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))