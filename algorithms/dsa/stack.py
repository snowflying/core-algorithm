#


class Stack(object):
    def __init__(self, size):
        self.box = []
        self._size = size

    def push(self, value):
        if not self.check_isfull():
            self.box.append(value)
        else:
            print('the stack is full !!')

    def pop(self):
        if not self.check_isempty():
            return self.box.pop()
        else:
            print('the stack is empty !!!')

    def check_isfull(self):
        if len(self.box) == self._size:
            return True
        else:
            return False

    def check_isempty(self):
        if len(self.box) == 0:
            return True
        else:
            return False


stacka = Stack(4)
stacka.push(1)
stacka.push(2)
# print('1'*5)
print(stacka.pop())
# print('2'*5)
stacka.push(3)
stacka.push(4)
stacka.push(5)
print(stacka.box)
stacka.push(6)
