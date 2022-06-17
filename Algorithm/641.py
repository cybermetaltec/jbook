class LinkedNode:
    def __init__(self, v=0, next=None):
        self.value = v
        self.next = next
        self.prev = None

    def __str__(self):
        return f'{self.value}->{self.next}'


class MyCircularDeque:
    def __str__(self):
        return str(self.head)

    def __init__(self, k: int):
        self.maxsize = k
        self.size = 0
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.size < self.maxsize:
            node = LinkedNode(value, self.head)
            if self.size:
                node.next = self.head
                node.next.prev = node
            else:
                self.tail = node
            self.head = node
            self.size += 1
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if self.size < self.maxsize:
            node = LinkedNode(value)
            if self.size:
                node.prev = self.tail
                node.prev.next = node
            else:
                self.head = node
            self.tail = node
            self.size += 1
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.head is not self.tail:
            oldhead = self.head
            self.head = oldhead.next
            self.head.prev = None
            oldhead.next = None
            self.size -= 1
        elif self.head:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            return False
        return True

    def deleteLast(self) -> bool:
        if self.tail is not self.head:
            prev = self.tail.prev
            self.tail.prev = None
            prev.next = None
            self.tail = prev
            self.size -= 1
        elif self.tail:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            return False
        return True

    def getFront(self) -> int:
        return self.head.value if self.head else -1

    def getRear(self) -> int:
        return self.tail.value if self.tail else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.maxsize


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(77)
obj.insertFront(89)
print(obj.tail)
obj.deleteLast()
print(obj.head)
obj.getRear()


