class Node:
    def __init__(self,val):
        self.value = val
        self.next = None

class Solution :

    def insertAtBegin(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        else :
            new_node= self.head
            self.head = new_node
            


    