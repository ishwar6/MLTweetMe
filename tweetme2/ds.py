# Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):

        self.head = None


llist = LinkedList()

llist.head = Node(1)
llist.head = Node(2)
print(llist.head)
