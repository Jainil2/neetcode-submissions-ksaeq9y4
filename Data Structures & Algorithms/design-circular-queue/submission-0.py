class Node:
    
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.l = 0
        self.head = self.tail = Node(-1)
        self.head.next = self.tail 
        self.tail.prev = self.head

    def enQueue(self, value: int) -> bool:
        if self.l >= self.k:
            return False
        node = Node(value)
        temp = self.tail.prev
        temp.next = node
        node.prev = temp
        node.next = self.tail
        self.tail.prev = node
        self.l += 1
        # if self.l >= self.k:
        #     return self.deQueue()
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        temp = self.head.next
        self.head.next = temp.next
        temp.next.prev = self.head
        del temp
        self.l -= 1
        return True

    def Front(self) -> int:
        return self.head.next.val

    def Rear(self) -> int:
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        return self.l == 0

    def isFull(self) -> bool:
        return self.l == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()