from collections import deque

class MyStack:
    def __init__(self):
        # Initialize a single queue
        self.queue = deque()
    
    def push(self, x: int) -> None:
        # Get the current size of the queue
        size = len(self.queue)
        
        # Add the new element to the queue
        self.queue.append(x)
        
        # Rotate the queue to ensure the new element is at the front
        for _ in range(size):
            self.queue.append(self.queue.popleft())
    
    def pop(self) -> int:
        # Remove and return the front element of the queue
        return self.queue.popleft()
    
    def top(self) -> int:
        # Peek the front element of the queue
        return self.queue[0]
    
    def empty(self) -> bool:
        # Check if the queue is empty
        return not self.queue
