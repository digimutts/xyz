from listnode import ListNode
import logging
logging.basicConfig()
logger = logging.getLogger("stackll")
logger.setLevel(logging.INFO)


class StackLL:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        topush = ListNode(x)
        topush.next = self.head
        self.head = topush
        self.size += 1
        logger.debug('stack is %s' % self.size)

    def peek(self):
        if self.is_empty():
            return None
        return self.head.val

    def pop(self):
        if self.is_empty():
            return None
        topop = self.head.val
        self.head = self.head.next
        self.size -= 1
        logger.debug('popped %s, %s remain' % (topop, self.size))
        return topop


def main():
    stack = StackLL()
    stack.push('fish')
    print(stack.peek())
    popped = stack.pop()
    print('Popped %s' % popped)
    pop2 = stack.pop()
    print('Popped empty: %s' % pop2)
    print(stack.size)
    stack.push('things')
    stack.push('stuff')
    stack.push('bitch dog')
    stack.push(44)
    while not stack.is_empty():
        poppy = stack.pop()
        print(poppy, stack.size)

if __name__ == "__main__":
    main()