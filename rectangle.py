class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# Test
if __name__ == "__main__":
    rect = Rectangle(5, 3)
    for dim in rect:
        print(dim)
