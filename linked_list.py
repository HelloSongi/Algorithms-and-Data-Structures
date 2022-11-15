class Node:
    """
    An object to store a single node of a linked list
    models two attributes - data and link to the next node in the list
    """
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data =data
        
    def __repr__(self):
        return "<Node> data: %s" %self.data
    
class LinkedList:
    '''singly linked list'''
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
    
    def size(self):
        '''returns number of nodes in a list --takes linear time O(n)'''
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node 
        return count
    
    def add(self):
        '''adds new Node containg data at head-begining of list - O(1)'''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def __repr__(self):
        '''returns string representation of the list - O(n) time'''
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
            return '-> '.join(nodes)