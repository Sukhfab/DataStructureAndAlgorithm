# list = "march 22n "
# def hash_fun(list):
#     h = 0
#     for letter in list:
#         ascii_value = ord(letter)
#         h += ascii_value
#     return h %100
# # print(hash_fun(list))

class hashMap:
    def __init__(self):
        self.max_value = 100
        self.bucket_array = [[] for x in range(self.max_value)]

    def get_hash(self, key):
        adding_assci= 0
        for x in key:
            adding_assci += ord(x)
        return adding_assci % 100


    def add_key_value(self, key, value):
        hashed_key = self.get_hash(key)
        found = False
        for i, (k, v) in enumerate(self.bucket_array[hashed_key]):
            if k == key:
                self.bucket_array[hashed_key][i] = (key, value)
                found = True
                break
        if not found:
            self.bucket_array[hashed_key].append((key, value))

    def getValue(self,key):
        hashedKey= self.get_hash(key)

        for x in self.bucket_array[hashedKey]:
            if x[0] == key:
                return x


h = hashMap()
print(h.get_hash("march 6"))
print(h.get_hash("6 march"))
h.add_key_value("march",123)
h.add_key_value("march 6",122)
h.add_key_value("march 6",132)
h.add_key_value("6 march",17)

print((h.getValue("march 6")))
print(h.bucket_array)
print(h.getValue("6 march"))
