class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nex = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.m = {}
        self.size = 0

    def _move_to_head(self, node: Node) -> None:
        if self.head is node: return
        if node.key in self.m: self._delete(node)
        node.nex, self.head = self.head, node
        if node.nex: node.nex.prev = node
        if self.tail is None: self.tail = node

    def _delete(self, node: Node, remove_map: bool = False) -> None:
        p = node.prev
        n = node.nex
        if p: p.nex = n
        if n: n.prev = p
        node.prev = None
        node.nex = None
        if self.tail is node: self.tail = p
        if self.head is node: self.head = n
        if remove_map: del self.m[node.key]

    def get(self, key: int) -> int:
        if node := self.m.get(key):
            self._move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if old_node := self.m.get(key):
            self._delete(old_node)
            old_node.val = value
            self._move_to_head(old_node)
        else:
            node = Node(key, value)
            if self.size == self.capacity:
                self._delete(self.tail, True)
            self._move_to_head(node)
            self.m[key] = node
            if self.size < self.capacity: self.size += 1


# lRUCache = LRUCache(2)
# lRUCache.put(1, 1)
# lRUCache.put(2, 2)
# print(lRUCache.get(1))
# lRUCache.put(3, 3)
# print(lRUCache.get(2))
# lRUCache.put(4, 4)
# print(lRUCache.get(1))
# print(lRUCache.get(3))
# print(lRUCache.get(4))

# lRUCache = LRUCache(1)
# lRUCache.put(2, 1)
# print(lRUCache.get(2))
# lRUCache.put(3, 2)
# print(lRUCache.get(2))
# print(lRUCache.get(3))

# ["LRUCache", "put", "put", "get", "put", "put", "get"]
# [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]

# lRUCache = LRUCache(2)
# lRUCache.put(2, 1)
# lRUCache.put(2, 2)
# print(lRUCache.get(2))
# lRUCache.put(1, 1)
# lRUCache.put(4, 1)
# print(lRUCache.get(2))
