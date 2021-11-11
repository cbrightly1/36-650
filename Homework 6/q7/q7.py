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
                if self.small is None:
                    self.small = Node(data)
                else:
                    self.small.insert(data)
            elif 0 <= data - self.data < 10:
                if self.big is None:
                    self.big = Node(data)
                else:
                    self.big.insert(data)
            elif 10 <= data - self.data:
                if self.toobig is None:
                    self.toobig = Node(data)
                else:
                    self.toobig.insert(data)
        else:
            self.data = data
    
    def traversal_print(self):
        if self.small:
            self.small.traversal_print()
        print(self.data)
        if self.big:
            self.big.traversal_print()
        if self.toobig:
            self.toobig.traversal_print()

root = Node(20) #Instantiate the tree
root.insert(40)
root.insert(45)
root.insert(32)
root.delete(45)
root.traversal_print()
