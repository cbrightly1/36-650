    def deleteDeepest(self, d_node):
        q = []
        q.append(self)
        while(len(q)):
            temp = q.pop(0)
            if temp is d_node:
                temp = None
                return
            if temp.small:
                if temp.small is d_node:
                    temp.small = None
                    return
                else: 
                    q.append(temp.small)
            if temp.big:
                if temp.big is d_node:
                    temp.big = None
                    return
                else: 
                    q.append(temp.big)
            if temp.toobig:
                if temp.toobig is d_node:
                    temp.toobig = None
                    return
                else: 
                    q.append(temp.toobig)

    def delete(self, data):
    # Compare the new value with the parent node
        if not self: return None

        if self.data == data:
            if not self.big and not self.toobig: return self.small
            if not self.small and not self.toobig: return self.big
            if not self.small and not self.big: return self.toobig
            
        key_node = None
        q = []
        q.append(self)
        temp = None
        while(len(q)):
            temp = q.pop(0)
            if temp.data == data:
                key_node = temp
            if temp.small:
                q.append(temp.small)
            if temp.big:
                q.append(temp.big)
            if temp.toobig:
                q.append(temp.toobig)
        if key_node:
            x = temp.data
            self.deleteDeepest(temp)
            key_node.data = x
        return self