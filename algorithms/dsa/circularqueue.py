# -*- encoding: utf-8 -*

class CircularQ(object):
    def __init__(self, size):
        self._front = self._rear = -1
        self.circlebox = [None] * size

    def enqueue(self, value):
        if self._rear == -1:
            self._rear = self._front = 0
            self.circlebox[self._rear] = value
            self._rear = self._rear + 1
        elif self._rear == self._front and self._rear != 0:
            print('The circularQ is full !!')
        elif self._rear == self._front == 0 and self.circlebox[0] is None:
            self.circlebox[self._rear] = value
            self._rear = self._rear + 1
        elif self._rear < self._front:
            self.circlebox[self._rear] = value
            self._rear = self._rear + 1
        elif (self._rear + 1) % len(self.circlebox) != 0:
            self.circlebox[self._rear] = value
            self._rear = self._rear + 1
        elif (self._rear + 1) % len(self.circlebox) == 0:
            self.circlebox[self._rear] = value
            self._rear = 0

    def dequeue(self):
        if self._rear == -1:
            print("this is one empty Q")

        item = self.circlebox[self._front]
        self.circlebox[self._front] = None
        if (self._front + 1) % len(self.circlebox) != 0:
            self._front = self._front + 1
        else:
            self._front = 0
        return item


class Circularq(object):
    def __init__(self, size):
        self._front = self._rear = -1
        self.circlebox = [None] * size
        self._size = size

    # init, _rear=0 is the first place to get element in
    # step1, plus 1 to _rear, then add element into pointer _rear+1
    # (_rear + 1) % _size eq|ne _front to judge if it is full under two different scenario(_front=0 & _rear=end, _rear+1=_front)
    def enqueue(self, value):
        if self._rear == -1:
            self._front = self._rear = 0
            self.circlebox[self._rear] = value
        elif (self._rear + 1) % self._size == self._front:
            print('the Q is full !!!')
        else:
            self._rear = (self._rear + 1) % self._size
            self.circlebox[self._rear] = value

    def dequeue(self):
        if self._rear == -1:
            print("this is one empty Q")
            return False

        if self._front == self._rear:
            temp = self.circlebox[self._front]
            self._front = self._rear = -1
            return temp

        # step1, return the value of pointer _front
        # step2, plus 1 to _front
        item = self.circlebox[self._front]
        self.circlebox[self._front] = None

        self._front = (self.__front + 1) % self._size
        # if (self._front + 1) % len(self.circlebox) != 0:
        #     self._front = self._front + 1
        # else:
        #     self._front = 0
        return item

class MyCircularQueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp


q = Circularq(5)
q.encirclebox('a')
q.encirclebox('b')
q.encirclebox('c')
q.encirclebox('d')
q.encirclebox('e')
q.encirclebox('f')
print("current _front: {0} and _rear: {1}".format(q._front, q._rear))
q.encirclebox('g')
print("the q is: {0}".format(q.circlebox))
print("current _front: {0} and _rear: {1}".format(q._front, q._rear))
q.encirclebox('h')
q.encirclebox('i')
print('decirclebox one item: {0}'.format(q.decirclebox()))
print("the q is: {0}".format(q.circlebox))
print("current _front: {0} and _rear: {1}".format(q._front, q._rear))
print('decirclebox one item: {0}'.format(q.decirclebox()))
print("the q is: {0}".format(q.circlebox))
print("current _front: {0} and _rear: {1}".format(q._front, q._rear))
q.encirclebox('j')
q.encirclebox('k')
q.encirclebox('l')
print("the q is: {0}".format(q.circlebox))
print("current _front: {0} and _rear: {1}".format(q._front, q._rear))

# # 
# q.dequeue()
# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('c')
# q.enqueue('d')
# q.enqueue('e')
# q.enqueue('f')
# # print("the q is: {0}".format(q.circlebox))
# # print("current _front: {0} and _rear: {1}".format(q._front, q._rear))
# print("the q is: {0}".format(q.queue))
# print("current _front: {0} and _rear: {1}".format(q.head, q.tail))


# # ##
# q.enqueue('a')
# q.enqueue('b')
# q.enqueue('c')
# q.enqueue('d')
# q.enqueue('e')
# 
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# # print("current _front: {0} and _rear: {1}".format(q._front, q._rear))
# print("current _front: {0} and _rear: {1}".format(q.head, q.tail))
# 
# q.enqueue('f')
# q.enqueue('g')
# q.enqueue('h')
# q.enqueue('i')
# q.enqueue('j')
# 
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# q.dequeue()
# 
# q.enqueue('k')
# q.enqueue('l')
# q.enqueue('m')
# q.enqueue('n')
# q.enqueue('o')
# 
# print("the q is: {0}".format(q.queue))
# print("current _front: {0} and _rear: {1}".format(q.head, q.tail))