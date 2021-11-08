class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

# Class to create a Linked List
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # Print the linked list
    def print_list(self):
        if self.head == None:
            raise ValueError("List is empty")
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("\n")
    
    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
        else:
            while (current.next):
                current = current.next
            current.next = node

    # Find length of Linked List
    def size(self):
        if self.head == None:
            return 0
        size = 0
        current = self.head
        while current:
            size += 1
            current = current.next
        return size
    
    # Sort the linked list
    def sort(self):
        for i in range(self.size()-1):
            current = self.head
            for i in range(self.size()-1):
                value1 = current.data
                next = current.next
                value2 = next.data
                if value1 < value2:
                    current.data = value2
                    next.data = value1
                current = current.next
        return self.print_list()

first_node = Node(1)
linked_list = LinkedList(first_node)
linked_list.insert(5)
linked_list.insert(10)
linked_list.insert(74)
linked_list.insert(1)
linked_list.insert(2)

print("The Linked List is:")
linked_list.print_list()

print('The sorted Linked List is:')
linked_list.sort()