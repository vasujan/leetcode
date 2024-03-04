class MonotonicStack:
    def __init__(self, capacity: int, ascending: bool=True, dtype=None):
        self.capacity = capacity
        self.ascending = ascending
        if dtype is None:
            self.dtype = int
        else:
            self.dtype = dtype
        self.stack: list[self.dtype]
    
    def add(self, n):
        if not isinstance(n, self.dtype):
            raise ValueError(f"Expecting the value to be of type: {self.dtype}")
        
        