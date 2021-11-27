# Linked List

class Node:
    def __init__(self, data=None, next=None):
        print("Running for", data)
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):

        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, "-- ->", end=" ")
            temp = temp.next

    def insert_at_beg(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            node.next = temp
            self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node


llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)
llist.head.next = second
second.next = third

print(llist.head)
llist.insert_at_beg(22)
llist.insert_at_end(123)
llist.insert_at_beg(11)
llist.insert_at_end(33)
llist.printList()
