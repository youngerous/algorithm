class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.map[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.map.keys():
            return self.map[key]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.map.keys():
            del self.map[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# ----------------------------------------------------- #

import collections


class ListNode:
    def __init__(self, key=None, value=None) -> None:
        self.key = key
        self.value = value
        self.next = None


class MyHashMapChanining:
    """ Hashmap using chaining """

    def __init__(self) -> None:
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size

        # when node doesn't exist in index
        # (use .value to avoid defaultdict generating default ListNode)
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        # when node does exist in index
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.nextreturn
            prev, p = p, p.next