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

    def delete_x_position(self, x: int):
        print("To be deleted", x, "position")
        l = self.length_of_list()
        if x > l:
            print("position do not exists")
        else:
            if x == 1:
                print('deleting first node')
                if self.head.next:
                    self.head = self.head.next
                    return
                else:
                    self.head = None
                    return

            temp = self.head

            while x > 2:
                temp = temp.next
                x -= 1

            if temp.next and temp.next.next:
                temp.next = temp.next.next
            elif temp.next:
                temp.next = None
            else:
                self.head = None

    def length_of_list(self):
        l = 0
        if self.head is None:
            pass
        else:
            temp = self.head
            while temp:
                l += 1
                temp = temp.next
        return l
        print("Length of list is", l)

    def search_x(self, x):
        if self.head:
            temp = self.head
            k = 1
            while temp:
                if temp.data == x:
                    print("found at position", k)
                    return k
                else:
                    if temp.next:
                        temp = temp.next
                        k += 1
                    else:
                        return -1
            return -1

        else:
            print("Not found")
            return -1

    def delete_value_x(self, x):
        if self.head:
            item = self.search_x(x)

            if item != -1:

                if item == 1:
                    print("running")
                    if self.head.next:
                        self.head = self.head.next
                    else:
                        self.head = None
                    return 1

                temp = self.head

                while item > 2:
                    temp = temp.next
                    item -= 1

                if temp.next.next:

                    temp.next = temp.next.next
                else:

                    temp.next = None

            else:
                print(x, "do not found in the list")

    def find_middle(self):
        if self.head:
            fast = slow = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print(slow.data)

    def detect_loop(self):
        if self.head:
            s = set()

            temp = self.head
            while temp:
                if temp in s:
                    print("detected")
                    return True
                s.add(temp)

                temp = temp.next

        return False

    def floyd_cycle_loop_detect(self):
        if self.head:
            slow = fast = self.head
            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True

        return False

    # remove repeated elements from a sorted linked list

    def remove_repeated_from_sorted(self):
        if self.head:
            temp = self.head
            while temp.next:
                if temp.data == temp.next.data:
                    temp.next = temp.next.next
                else:
                    temp = temp.next

    def remove_repeated_from_unsorted(self):
        if self.head:
            prev = None
            temp = self.head
            s = set()
            while temp.next:
                if temp.data in s:
                    prev.next = temp.next
                    temp = prev.next
                else:
                    s.add(temp.data)
                    prev = temp
                    temp = temp.next


llist = LinkedList()
llist.insert_at_beg(1)
llist.insert_at_beg(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.insert_at_end(4)
llist.insert_at_end(5)
llist.insert_at_end(2)
llist.insert_at_end(5)
llist.insert_at_end(33)
llist.insert_at_end(6)
# llist.head.next.next = llist.head #to make a loop in the linked list

print(llist.detect_loop())
print(llist.floyd_cycle_loop_detect())

# llist.delete_x_position(3)
# llist.search_x(-2)
print("Middle")
llist.printList()
# llist.find_middle()
# llist.remove_repeated_from_sorted()
llist.remove_repeated_from_unsorted()
# llist.delete_value_x(3)


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
