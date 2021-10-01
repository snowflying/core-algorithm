# -*- encoding: utf-8 -*


class queue(object):
    def __init__(self, size):
        # insert side
        self._rear = 0
        # read side
        self._front = 0
        self.box = [None] * size

    def is_empty(self):
        pass

    def is_full(self):
        pass

    def enqueue(self, item):
        self.box[self._rear] = item
        self._rear = self._rear + 1

    def dequeue(self):
        item = self.box[self._front]
        self.box[self._front] = None
        self._front = self._front + 1
        return item


qobj = queue(10)
qobj.enqueue('A')
qobj.enqueue('B')
qobj.enqueue('C')
print(qobj.box)
qobj.dequeue()
print(qobj.box)
qobj.dequeue()
print(qobj.box)
qobj.dequeue()
print(qobj.box)
print('*' * 20)
print("self._rear: {0}".format(qobj._rear))
print("self._front: {0}".format(qobj._rear))
print('*' * 20)
qobj.enqueue('A')
qobj.enqueue('B')
print(qobj.box)
qobj.dequeue()
print(qobj.box)
qobj.enqueue('C')
qobj.enqueue('D')
print(qobj.box)
print('*' * 20)
print("self._rear: {0}".format(qobj._rear))
print("self._front: {0}".format(qobj._rear))




