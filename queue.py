class Queue:
    def __init__(self):
        self.queue = []

    def to_string(self):
        print(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, x):
        # Insert at front of list
        self.queue.insert(0, x)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop()

    def peek(self):
        # Use #-1: to slice last item in list
        if self.is_empty():
            return None
        return self.queue[-1:]

    def size(self):
        return len(self.queue)

def main():
    q = Queue()
    print(q.dequeue())
    print(q.peek())
    q.enqueue('dog1')
    q.enqueue('dog2')
    q.to_string()
    q.enqueue('chinese')
    print(q.peek())
    print(q.dequeue())
    print(q.dequeue())
    q.to_string()

if __name__ == "__main__":
    main()
