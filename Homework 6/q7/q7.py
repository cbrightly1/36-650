class Node:
    def __init__(self, data):
      self.small = None 
      self.big = None 
      self.toobig = None 
      self.data = data # Node data
    
    def PrintTree(self):
      print(self.data)
   
    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if 0 > data - self.data:
                if self.small is None: self.small = Node(data)
                else: self.small.insert(data)
            elif 0 <= data - self.data < 10:
                if self.big is None: self.big = Node(data)
                else: self.big.insert(data)
            elif 10 <= data - self.data:
                if self.toobig is None: self.toobig = Node(data)
                else: self.toobig.insert(data)
        else: self.data = data
    
    def traversal_print(self):
        if self.small:
            self.small.traversal_print()
        print(self.data)
        if self.big:
            self.big.traversal_print()
        if self.toobig:
            self.toobig.traversal_print()

    # Make a list of my tree
    def traversal_list(self, output = []):
        if self.small:
            self.small.traversal_list()
        output.append(self.data)
        if self.big:
            self.big.traversal_list()
        if self.toobig:
            self.toobig.traversal_list()
        return output

    # To keep the same tree, we will just clear its contents before
    # readding everything
    def clear_tree(self):
        self.data = None
        self.small = None
        self.big = None
        self.toobig = None
        return self

    def delete(self,value):
        node_list = self.traversal_list() # Get list of tree
        node_list.remove(value) # Remove the value I don't want anymore
        new_tree = self.clear_tree() # Clear the tree so we can add back things in the right order
        for node in node_list: # Insert nodes in the right order
            new_tree.insert(node)
        return new_tree

root = Node(20) #Instantiate the tree
root.insert(40)
root.insert(45)
root.insert(32)
root.insert(16)
root.insert(5)
print("tree contents after insertion using the traversal():")
root.traversal_print()
root.delete(40)
print("tree contents after deleting")
root.traversal_print()
