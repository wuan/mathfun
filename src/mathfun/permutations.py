class BitPermutations:

    def __init__(self, size: int, count: int):
        self.size = size
        self.count = count
        self.positions = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.positions is None:
            self.positions = list(range(self.count))
        else:
            at_end = True
            for index in range(self.count):
                pos = self.count - 1 - index
                if self.positions[pos] < self.size - 1 - index:
                    self.positions[pos] += 1
                    at_end = False
                    break

            if at_end:
                raise StopIteration

        return tuple(self.positions)
