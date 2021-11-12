class Node(object):
    def __init__(self, data):
        self.data = data
        self.previous = None

# Class to create a Linked List
class LinkedList(object):
    def __init__(self, tail=None):
        self.tail = tail

    # Print the linked list
    def print_list(self):
        if self.tail == None:
            raise ValueError("List is empty")
        current = self.tail
        while current:
            print(current.data, end="  ")
            current = current.previous
        print("\n")

    # Insert a node in a linked list
    def insert(self, data):
        node = Node(data)
        current = self.tail
        if not current:
            self.tail = node
        else:
            while (current.previous):
                current = current.previous
            current.previous = node
            
    def insert(self, data):
        node = Node(data)
        node.previous = self.tail
        self.tail = node

    # Delete a node in a linked list
    def delete(self, data):
        if not self.tail:
            return
        temp = self.tail
        if self.tail.data == data:
            self.tail = temp.previous
            return
        while temp.previous:
            if temp.previous.data == data:
                temp.previous = temp.previous.previous
                return
            temp = temp.previous
        return
    
    def search(self, data):
        current = self.tail
        print(self.tail.data)
        while current:
            if current.data == data:
                return True
            current = current.previous  
        return False

first_node = Node(11)
linked_list = LinkedList(first_node)
linked_list.insert(3)
linked_list.insert(6)
linked_list.insert(5)

print("The Linked List is:")
linked_list.print_list()

linked_list.delete(6)
print("After deleting 6, the Linked List is:")
linked_list.print_list()

print("Does 5 exist?")
print(linked_list.search(11))

print("Does 17 exist?")
print(linked_list.search(6))