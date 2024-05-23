class StackArray:
    def __init__(self, size: int):
        self.arr: list[int] = [None] * size
        self.top: int = -1
        self.capacity = size
    
    def isEmpty(self) -> bool:
        return self.top == -1
    
    def isFull(self) -> bool:
        return self.top == self.capacity - 1
    
    def push(self, x: int) -> None:
        if (self.isFull()):
            print("Overflow. Program Terinated.")
        self.top += 1
        self.arr[self.top] = x
    
    def pop(self) -> int:
        if (self.isEmpty()):
            print("Underflow. Program Terminated")
        t = self.top
        self.top -= 1
        return self.arr[t]
    
    def peek(self) -> int:
        if not self.isEmpty():
            return self.arr[self.top]
        else:
            return None
        
    def size(self) -> int:
        return self.top + 1
