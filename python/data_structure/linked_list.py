"""
create linked lists
"""

class node(object):
    """
    Nodes of linked list
    Linked List Nodes store a value and points to next node
    
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class linked_list(object):
    """
    This class is used to setup the linked list
    """
    def __init__(self, head=None):
        """
        initialize head node to have default value as None
        """
        self.head = head

    
    def append(self, new_node):
        # go to LinkedList first object
        current = self.head
        # if first object is not null then find the last node
        if self.head:
            # cycle through the LL to find last filled node
            while current.next:
                current = current.next
            # assign the last node with new node object
            current.next = new_node
        else:
            # if first node of LL, assign node object to head
            self.head = new_node


    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        index_ref = 1
        temp = self.head
        match_index = None
        while temp:
            # if the index matches the position then return index
            if index_ref == position:
                print(temp.value)
                break
            index_ref += 1
            temp = temp.next
        return match_index
    

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        pass
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        pass


    def printList(self):
        # take LL node to head
        temp = self.head 
        # cycle through and print value of each node
        while (temp): 
            print (temp.value) 
            temp = temp.next       


def main():

    # creating nodes with values
    n1 = node(1)
    n2 = node(2)
    n3 = node(3)
    n4 = node(4)

    ll = linked_list()
    ll.append(n1)
    ll.append(n2)
    ll.append(n3)
    ll.append(n4)

    ll.printList()

if __name__ == "__main__":
    main()