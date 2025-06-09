import copy
class Prototype:
    def __init__(self, value):
        self.value = value
    def clone(self):
        return copy.deepcopy(self)

if __name__ == "__main__":
    original = Prototype([1, 2, 3])
    clone = original.clone()
    print("Original:", original.value)
    print("Clone:", clone.value)
    print("Same object:", original is clone)
