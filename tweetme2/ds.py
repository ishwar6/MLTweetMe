# Linked List

class Node:
    def __init__(self, data=None, next=None):

        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):

        self.head = None

    def printList(self):
        if self.head is None:
            print("EMPTY")
            return None
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            if temp.next:
                print("-->", end=" ")
            temp = temp.next
        print("")

    def insert_at_beg(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            node.next = temp
            self.head = node
        self.printList()

    def insert_at_end(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        self.printList()

    def delete_from_beg(self):
        if self.head:
            print("deleted node from beg", self.head.data)
            temp = self.head.next
            self.head = temp
        else:
            print("Empty linked list")

    def delete_end(self):
        if self.head and self.head.next:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
        elif self.head:

            self.head = None
        else:
            print("EMPTY")


llist = LinkedList()
llist.insert_at_beg(1)
llist.delete_end()
llist.insert_at_end(2)
llist.delete_from_beg()
llist.delete_from_beg()
llist.delete_from_beg()
llist.insert_at_end(3)
llist.delete_from_beg()
llist.insert_at_beg(0)
llist.delete_end()

print("Final")
llist.printList()
print("")
print("repeat")

# __REVISION__


class Nodes:
    def __init__(self, data=int, next=None) -> None:
        self.data = data
        self.next = next


class Linkedlists:
    def __init__(self) -> None:
        self.head = None

    def printl(self):
        temp = self.head
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next


first = Nodes(1)
second = Nodes(2)
# to get a cyclic linked list use: second = Nodes(2, first)
L = Linkedlists()
L.head = first
first.next = second
L.printl()
