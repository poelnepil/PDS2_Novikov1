
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.capacity = 50
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0

        for idx, val in enumerate(key):
            hashsum += (idx+len(key))**ord(val)
            hashsum = hashsum % self.capacity

        return hashsum

    def insert(self, key, value):
        # + size
        self.size += 1

        # get index from key
        index = self.hash(key)

        # go to simular node to hash
        node = self.buckets[index]

        # if bucket is empty
        if node is None:
            self.buckets[index] = Node(key, value)
            return

        # collision
        prev = node
        while node is not None:
            prev = node
            node = node.next

        prev.next = Node(key, value)

    def find(self, key):

        index = self.hash(key)

        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None

        else:
            return node.key, node.value


    def remove(self, key):

        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None

        else:
            self.size -= 1
            result = node.value

            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next

            return result

    def show_ht(self):
        return self.buckets

ht = HashTable()

alpb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
c = 0


for i in alpb:
    c += 1
    ht.insert(i, c)

ht.remove('d')

for i in alpb:
    print(ht.find(i))

print(ht.show_ht())
