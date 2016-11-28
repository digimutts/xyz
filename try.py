
import logging
logger = logging.getLogger("try")
logger.setLevel(logging.INFO)

class Troy(object):

    def __init__(self):
        self.children = {}
        self.payload = None

    def addItem(self, coord, payload):
        if len(coord) == 0:
            self.payload = payload
            return
        value = coord[0]
        if value not in self.children:
            self.children[value] = Troy()
        self.children[value].addItem(coord[1:], payload)

    def getChildren(self, root):
        """
        Gets all Payloads from children below the specified root, as a set
        :param root: a string
        :return: a set of Payloads
        """
        if len(root) == 0:
            # Base case: we've reached the end of the root, return all below this level
            return self.getAllPayloads(set())
        else:
            if root[0] in self.children:
                return self.children[root[0]].getChildren(root[1:])
            else:
                # Root not found, return empty set
                print('Root %s not found' % root)
                return set()

    def getAllPayloads(self, payloads):

        # payloads = set()
        if len(self.children) == 0:
            # Base case, no more children to check, union this payload with those found so far
            if self.payload is not None:
                print('Got payload %s' % self.payload)
                return payloads | {self.payload}
                # return {self.payload}
            else:
                print('No payload!')
                return payloads
                # return set()
        # We still have children to check
        for key in self.children:
            # Union payloads with the ones from children
            # self.children.get(key).getAllPayloads(payloads)
            payloads = payloads | self.children.get(key).getAllPayloads(payloads)
            # self.children.get(key).getAllPayloads(payloads)
        return payloads


def main():
    troy = Troy()
    coords = [('12345', 'ice cream'), ('12346', 'fish'), ('111', 'ooh')]

    for (coord, payload) in coords:
        troy.addItem(coord, payload)
    print('done adding items.')
    root = '12'
    payloads = troy.getChildren(root)
    print('Got payloads %s' % payloads)

main()