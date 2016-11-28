from listnode import ListNode
import logging
logging.basicConfig()
logger = logging.getLogger("queuell")
logger.setLevel(logging.INFO)


class QueueLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, x):
        node = ListNode(x)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            # There is at least one item
            # Point the tail to the new node
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        topop = self.head.val
        self.head = self.head.next
        self.size -= 1
        return topop


def main():
    q = QueueLL()
    # try to pop empty
    logger.info('Pop empty: %s ' % q.dequeue())
    q.enqueue('first')
    q.enqueue('second')
    q.enqueue('third')
    logger.info('%s in q' % q.size)
    while not q.is_empty():
        pop = q.dequeue()
        logger.info('popped %s, %s left' % (pop, q.size))

if __name__ == "__main__":
    main()

