# File: ordered_list.py
# Date: May 6, 2021
# Authors: Griffin Palmeri and Tyler Kreider
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

        current = self.front    

        #if nothing in list, create node and set it to front and back 
        if self.len == 0:
            self.front = self.back = Node(x)
        
        #if 1 item in list already, compare it and set it in front of it or behind it
        elif self.len == 1:
            if x <= current.item:

                new_node = Node(x, current)
                self.front =  current.prev = new_node

            else:

                new_node = Node(x,None, current)
                current.next = self.back = new_node

        #if list is already longer than 2    
        else:

            placed = False
            while not placed:  

                #identifies the location to insert    
                if x <= current.item:
                    
                    #if at the front of the list
                    if self.front == current:
                        new_front_node = Node(x, current)
                        self.front = current.prev = new_front_node    
                    
                    #if not at the front of the list
                    else:
                        new_node = Node(x,current, current.prev)
                        current.prev.next = current.prev = new_node

                    placed = True

                #placing at the end of the list
                elif current == self.back and not placed:         
    
                        new_node = Node(x,)
                        new_node.prev = current
                        current.next = self.back = new_node

                        placed = True  

                #moves to next item in the list
                else:
                    current = current.next  

        self.len += 1  # Add one to the length because we added one node   


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
        
        current = self.front
        removed = False
        
        #if there is nothing in the list
        if self.len == 0 or (self.len == 1 and current.item != x ):
            raise ValueError

        #if the list is length of 1
        elif self.len == 1:
            if current.item == x:
                self.front = self.back = None
                removed = True


        #if the list length is bigger than 1
        else:

            while removed == False:

                for i in range(1, self.len + 1):

                    #if x was not found in the list
                    if (i == self.len and current.item < x and removed == False) or current.item > x and removed == False:
                        raise ValueError

                    #if x is found in the list
                    elif current.item == x and removed == False:

                        #if x is the first item in the list
                        if i == 1:
                            if len == 2:
                                self.front = self.back = current.next = current.prev = None

                            else:
                                self.front = current.next
                                current.next.prev = None

                            removed = True

                        #if x is the last item in the list
                        elif i == self.len:
                            self.back = current.prev
                            current.prev.next = None
                            removed = True
                        
                        #if x is in the middle of the list
                        else:
                            current.prev.next = current.next
                            current.next.prev = current.prev
                            removed = True
                    
                    #checks next number in th list
                    elif removed == False:
                        current = current.next

        #if x is never found               
        if removed == False:
            raise ValueError
        else:
            self.len -= 1 # If we removed something, decrease the length by 1


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
        
        current = self.front
        
        #if the list is empty or isn't in list with length 1
        if self.len == 0 or (self.len == 1 and current.item != x):
            raise ValueError
        
        #if the length of list is 1
        elif self.len == 1:
            if current.item == x:
                self.front = self.back = None
                self.len -= 1

        #if length of list is more than 1
        else:
            for i in range(self.len):

                if current == self.back and current.item < x:
                    raise ValueError

                #when x is found in list
                elif current.item == x :

                    #if x is the first item in list
                    if current == self.front:

                        #deletes the first item in a list with length 2
                        if self.len == 2:
                            self.front = self.back = current.next
                            current = self.front
                            current.next = current.prev = None

                        #deletes the first item
                        else:

                            if self.len == 1:
                                self.front = self.back = None
                            else:
                                self.front = current.next
                                current.next.prev = None
                           
                    #deletes last item in list
                    elif current == self.back:
                        self.back = current.prev
                        current.prev.next = None

                    #deletes item of x in middle of list
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    
                    self.len -= 1 # Remove one from the length because an item has been removed
                
                if self.len > 1:
                    current = current.next
                        
        

    def remove_duplicates(self):
        """
        Removes all duplicate items from the list, leaving just
        one copy of each different item.
        This method must be performed in one pass through list.
        """
        
        current = self.front

        #if list length is 2 
        if self.len == 2:

            #if the items are duplicates then remove one
            if current.item == current.next.item:
                current.next = None
                self.back = self.front

        #if list length is bigger than 2
        if self.len > 2:
            for i in range(self.len - 1):

                #checking for duplicates and deleting one
                if current.item == current.next.item:
                    if current.next.next == None:
                        self.back = current
                    else:
                        current.next.next.prev = current

                    current.next = current.next.next 
                    self.len -= 1
                
                #checks the next item in list
                else:
                    current = current.next



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

        # Create list and booleans 
        merged_list = OrderedLinkedList()
        first_done = False
        second_done = False

        # If self or the other list is empty we are done with it
        if self.front == None:
            first_done = True
    
        if other_ordered_list.front == None:
            second_done = True

        # Set the value of the current first, second list items to the front of the lists
        current_first = self.front
        current_second = other_ordered_list.front

        # While both lists aren't done, iterate    
        while not (first_done and second_done):

            # Check if the first list is still not empty and the second list is done, or the item is ready to be placed
            if not first_done and (second_done or current_first.item < current_second.item):

                # Insert item 
                merged_list.insert(current_first.item)

                # Update current if the next item exists, if not the first list is done
                if current_first.next != None:
                    current_first = current_first.next
                else:
                    first_done = True

            # Check if the second list is still not empty and the first list is done, or the item is ready to be placed
            elif not second_done and (first_done or current_first.item > current_second.item):
                
                # Insert item 
                merged_list.insert(current_second.item)

                 # Update current if the next item exists, if not the secondlist is done
                if current_second.next != None:
                    current_second = current_second.next
                else:
                    second_done = True

            else:
                # This is when the current numbers are equal

                # There is a special case where they are both none and would fall into this spot
                # So by making sure current_second isn't none, we know they both aren't none

                if current_second != None:
                    merged_list.insert(current_first.item)
                    merged_list.insert(current_second.item)

                   
                    # Update current
                    current_first = current_first.next  
                    current_second = current_second.next

                    # Check if first and second lists are done, if a list is done, set its boolean to true
                    if current_first.next == None:          
                        first_done = True

                    if current_second.next == None:
                        second_done = True

        # Set the length to the combined length of l1 and 2
        merged_list.len = self.len + other_ordered_list.len

        # Return the merged list that you have created
        return merged_list

               

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

        # Create list and boolean 
        intersection_list = OrderedLinkedList()
        done = False

        # If self or the other list is empty we are done instantly
        if self.front == None or other_ordered_list.front == None:
            done = True
        else:

            # Set the value of the current first, second list items to the front of the lists
            current_first = self.front
            current_second = other_ordered_list.front
       

        # While both lists aren't done, iterate    
        while not done:

            if current_first.item == current_second.item:
                
                # Insert node: doesn't matter if its first or second item because they're the same value
                same_val = current_first.item
                intersection_list.insert(same_val)

                # Go through list until the current item becomes a new value or you reach the end of the list
                while current_first.item == same_val and current_first != None:
                    current_first = current_first.next
            
                # Go through list until the current item becomes a new value or you reach the end of the list
                while current_second.item == same_val and current_second != None:
                    current_second = current_second.next

            else:
                
                # Depending on which number is bigger, update the current accordingly
                if current_second.item < current_first.item:
                    current_second = current_second.next
                else:
                    current_first = current_first.next

            # If either are None, it is no longer possible for them to equal the same number and we are done
            if current_first == None or current_second == None:
                done = True

        # Return the intersection list that you have created
        return intersection_list