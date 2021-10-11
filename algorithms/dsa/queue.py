#


class Queue(object):
    def __init__(self, size):
        self._front = 0
        self._rear = 0
        self.box = [None] * size

    def enqueue(self, value):
        if self.isfull():
            print('Queue is full !')
        else:
            self.box[self._rear] = value
            self._rear = 1 + self._rear

    def dequeue(self):
        if self.isempty():
            print('Queue is empty !')
        else:
            item = self.box[self._front]
            self.box[self._front] = None
            self._front = self._front + 1
            return item

    def isfull(self):
        if self._rear == len(self.box):
            return True

    def isempty(self):
        if self._front == self._rear or self._rear == 0:
            return True


queuea = Queue(5)
queuea.enqueue(1)
queuea.enqueue(2)
queuea.enqueue(3)
queuea.enqueue(4)
queuea.enqueue(5)
print('-+'*10)
print("the pointer self._rear's values: {0}".format(queuea._rear))
print('the queue is full? {0}'.format(queuea.isfull()))
print('-+'*10)
queuea.dequeue()
queuea.dequeue()
queuea.dequeue()
queuea.dequeue()
queuea.dequeue()
queuea.dequeue()
queuea.dequeue()
queuea.dequeue()
queuea.dequeue()