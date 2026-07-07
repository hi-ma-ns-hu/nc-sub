class Node:
    def __init__(self, key: Optional[int] = 0, val: Optional[int] = 0, prev: 'Optional[Node]' = None, next: 'Optional[Node]' = None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        ptr = self.map.get(key, None)
        if ptr is None:
            return -1
        before = ptr.prev
        after = ptr.next
        before.next = after
        after.prev = before
        tail_prev = self.tail.prev
        tail_prev.next = ptr
        ptr.next = self.tail
        self.tail.prev = ptr
        ptr.prev = tail_prev
        return ptr.val
        


    def put(self, key: int, value: int) -> None:
        ptr = self.map.get(key, None)
        if ptr is None:
            # create a new node and move its position, update the map
            node = Node(key, value)
            before = self.tail.prev
            before.next = node
            node.next = self.tail
            self.tail.prev = node
            node.prev = before
            # add to map
            self.map[key] = node
            capacity = len(self.map)
            if capacity > self.capacity:
                removed_node = self.head.next
                self.head.next = removed_node.next
                removed_node.next.prev = self.head
                del self.map[removed_node.key]
            return
        
        # update the value
        ptr.val = value
        before = ptr.prev
        after = ptr.next
        before.next = after
        after.prev = before
        tail_prev = self.tail.prev
        tail_prev.next = ptr
        ptr.next = self.tail
        self.tail.prev = ptr
        ptr.prev = tail_prev
