class MyList:
    def __init__(self):
        self.elements = []

    def __str__(self):
        return str(self.elements)

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __setitem__(self, index, value):
        self.elements[index] = value

    def append(self, value):
        self.elements.append(value)

    def remove(self, value):
        self.elements.remove(value)

    def pop(self, index=None):
        if index is None:
            return self.elements.pop()
        return self.elements.pop(index)

    def insert(self, index, value):
        self.elements.insert(index, value)

    def extend(self, other_list):
        self.elements.extend(other_list)

    def clear(self):
        self.elements = []

    def count(self, value):
        return self.elements.count(value)

    def index(self, value):
        return self.elements.index(value)

    def sort(self):
        self.elements.sort()

    def reverse(self):
        self.elements.reverse()
