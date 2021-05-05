# File: ordered_list.py
# Date: April 19, 2021
# Author: John Glick
# Description: Ordered linked list.

class Node:
    def __init__(self, item, next = None, prev = None):
        """ 
        Constructor.  Creates a node.
        Instance variables must be next, prev, and item.
        """
        self.item = item
        self.next = next
        self.prev = prev
       

class OrderedLinkedList:
    def __init__(self):
        """ 
        Constructor.  Creates an empty ordered list.
        Instance variables must be front, back, and len.
        """

        self.front = None
        self.back = None
        self.len = 0
        

    def insert(self, x):
        """ 
        Insert x into the list so that it remains ordered
        (smallest to largest) after the insert.  Duplicates
        are ok.
        """
        if self.len == 0:
            self.front = self.back = Node(x)
            self.len += 1

        else:

            current = self.front 
            
            placed = False
            counter = 0
            
            while not placed: 
                
                counter +=1
                if counter == self.len:
                        if self.len == 1:
                            new_node = Node(x)
                            self.front = new_node
                            new_node.next = current
                            current.prev = new_node
                            placed = True
                            pass
                        else:
                            new_node = Node(x)
                            new_node.prev = current
                            current.next = new_node
                            placed = True
                            pass

                if x <= current.item:

                    new_node = Node(x)

                    new_node.prev = current.prev
                    current.prev.next = new_node

                    current.prev = new_node
                    new_node.next = current
                    placed = True
                    pass
                   
                else:
                    current = current.next
                            
                    


    def __len__(self):
        """ Returns length of list """
        return self.len

    def __str__(self):
        """ Returns string representation of list """
        if self.front == None:
            return "[]"
        else:
            s = "["
            cur = self.front
            while cur.next != None:
                s += str(cur.item) + ", "
                cur = cur.next
            s += str(cur.item) + "]"
        return s

    def remove(self, x):
        """
        Removes the one instance of x in the list.
        Raises ValueError if x is not in the list.
        Do not perform any unnecessary comparisons -
        so if you are iterating down the list, and you reach
        an item greater than x, do not continue searching
        the list.
        """
        # You write the code for this
        pass

    def remove_all(self, x):
        """
        Removes all instances of x in the list.
        Raises ValueError if x is not in the list.
        The method must run in O(n) time, where n
        is the number of items in the list.  This means
        you must remove all items in one pass through the list.
        Remember that because the list is ordered, all copies
        of x will be next to one another in the list.
        Do not perform any unnecessary comparisons -
        so if you are iterating down the list, and you reach
        an item greater than x, do not continue searching
        the list.
        """
        
        # You write the code for this
        pass

    def remove_duplicates(self):
        """
        Removes all duplicate items from the list, leaving just
        one copy of each different item.
        This method must be performed in one pass through list.
        """
        # You write the code for this
        pass

    def merge(self, other_ordered_list):
        """
        Merges the items in the self list (the list calling the method), and 
        the items in other_ordered_list into a new orderedLinkedList object,
        that is then returned by the method.
        DO NOT simply create an empty orderedLinkedList object, and then
        insert each item in self and other_ordered_list into that new orderedLinkedList
        obect.  You must merge the items from self and 
        other_ordered_list into a newly created linked list, that operates in O(n) 
        running time, where n is the total number of items in both lists.
        (Think of the merge operation in merge sort as a guide for how to do this.)
        Duplicates are allowed.
        Leave self and other_ordered_list unchanged, so do not remove 
        the items from either list.  Just copy their items into your newly
        created list.  And don't try to reuse the nodes from either self
        or other_ordered_list.  You want to just copy the items from their nodes.
        """

        # You write the code for this
        pass

    def intersection(self, other_ordered_list):
        """
        Creates a new list that is the intersection of the items in the self list 
        (the list calling the method), 
        and the items in other_ordered_list, and this new list is returned.
        All items that appear in both lists should
        be in the intersection list.  You should keep just one copy of each item that
        appears in both lists, so for example,
        if there are two copies of an item in the self list, and 3 copies in the
        other_ordered_list list, then just one copy should be in the intersection.
        (Also, as another example, if there are 2 copies in the self list and 0 copies
        in the other list, then no copies should be in the intersection list.)
        You must find the intersection of self and other_ordered_list in one
        pass through both lists, and so its running time should be O(n), where n is 
        the total number of items in both lists.
        (This should have a similar feel to the merge operation.)
        Leave self and other_ordered_list unchanged, so do not remove 
        the items from either list.  Just copy their items into your newly
        created list.  And don't try to reuse the nodes from either self
        or other_ordered_list.  You want to just copy the items from their nodes.
        """

        # You write the code for this
        pass