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

    def dedupe(self):
        current = self.head
        unique_list = [] # list keeps everything in order
        previous = None # another pointer to keep track of the previous node
        while current is not None:
            if current.data in unique_list:
                previous.next = current.next # delete node by remapping the pointers
            else:
                unique_list.append(current.data)
                previous = current # save last node
            current = current.next #move onto the next one

        return self.print_list()
            
first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(3)
linked_list.insert(11)
linked_list.insert(6)
linked_list.insert(5)
linked_list.insert(7)
linked_list.insert(5)
linked_list.print_list()
linked_list.dedupe()