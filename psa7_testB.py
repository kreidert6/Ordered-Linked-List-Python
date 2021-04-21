# File: psa7_testB.py
# Date: April 19, 2021
# Author: Dr. Glick
# Description: Code to test the merge and intersection methods
#  of the OrdereLinkedList class.

from ordered_linked_list import OrderedLinkedList

def ordered_list_test():

    # Count num tested and num correct
    num_tests = 0
    num_correct = 0

    # Define some numbers to work with
    n1 = 100
    n2 = 90
    n3 = 80
    n4 = 110
    n5 = 120
    n6 = 95
    n7 = 115
    n8 = 10
    n9 = 200
    n10 = 93

    print("Testing merge method.  Both lists nonempty.\n")
    num_tests += 1
    l1 = OrderedLinkedList()
    l1.insert(n3)
    l1.insert(n2)
    l1.insert(n10)
    l1.insert(n1)
    l1.insert(n4)
    l1.insert(n5)
    l2 = OrderedLinkedList()
    l2.insert(n8)
    l2.insert(n6)
    l2.insert(n7)
    l2.insert(n9)    
    print(f"self list is {str(l1)}\n")
    print(f"other list is {str(l2)}\n")
    correct = f"[{n8}, {n3}, {n2}, {n10}, {n6}, {n1}, {n4}, {n7}, {n5}, {n9}]"
    l3 = l1.merge(l2)
    str_forward = str(l3)
    str_back = get_str_from_back_pointers(l3)
    print(f"Your merged list is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l3.len == 10:
        l1_str = f"[{n3}, {n2}, {n10}, {n1}, {n4}, {n5}]"
        l2_str = f"[{n8}, {n6}, {n7}, {n9}]"
        if (str(l1) == l1_str and get_str_from_back_pointers(l1) == l1_str and
                        l2_str and get_str_from_back_pointers(l2) == l2_str):   
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect.  l1 and l2 not left unchanged.")
    else:
        print(f"Incorrect.  SHould be {correct} and len = 10")

    print("Testing merge method.  self list empty.\n")
    num_tests += 1
    l1 = OrderedLinkedList()
    l2 = OrderedLinkedList()
    l2.insert(n8)
    l2.insert(n6)
    l2.insert(n7)
    l2.insert(n9)    
    print(f"self list is {str(l1)}\n")
    print(f"other list is {str(l2)}\n")
    correct = f"[{n8}, {n6}, {n7}, {n9}]"
    l3 = l1.merge(l2)
    str_forward = str(l3)
    str_back = get_str_from_back_pointers(l3)
    print(f"Your merged list is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l3.len == 4:
        l1_str = f"[]"
        l2_str = f"[{n8}, {n6}, {n7}, {n9}]"
        if (str(l1) == l1_str and get_str_from_back_pointers(l1) == l1_str and
                        l2_str and get_str_from_back_pointers(l2) == l2_str):   
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect.  l1 and l2 not left unchanged.")
    else:
        print(f"Incorrect.  SHould be {correct} and len = 4")

    print("Testing merge method.  Other list empty.\n")
    num_tests += 1
    l1 = OrderedLinkedList()
    l1.insert(n3)
    l1.insert(n2)
    l1.insert(n10)
    l1.insert(n1)
    l1.insert(n4)
    l1.insert(n5)
    l2 = OrderedLinkedList()  
    print(f"self list is {str(l1)}\n")
    print(f"other list is {str(l2)}\n")
    correct = f"[{n3}, {n2}, {n10}, {n1}, {n4}, {n5}]"
    l3 = l1.merge(l2)
    str_forward = str(l3)
    str_back = get_str_from_back_pointers(l3)
    print(f"Your merged list is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l3.len == 6:
        l1_str = f"[{n3}, {n2}, {n10}, {n1}, {n4}, {n5}]"
        l2_str = f"[]"
        if (str(l1) == l1_str and get_str_from_back_pointers(l1) == l1_str and
                        l2_str and get_str_from_back_pointers(l2) == l2_str):   
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect.  l1 and l2 not left unchanged.")
    else:
        print(f"Incorrect.  SHould be {correct} and len = 6")

    print("Testing intersection method.  Both lists nonempty.\n")
    num_tests += 1
    l1 = OrderedLinkedList()
    l1.insert(n3)
    l1.insert(n2)
    l1.insert(n10)
    l1.insert(n1)
    l1.insert(n4)
    l1.insert(n5)
    l2 = OrderedLinkedList()
    l2.insert(n8)
    l2.insert(n3)
    l2.insert(n6)
    l2.insert(n4)
    l2.insert(n7)
    l2.insert(n9)    
    print(f"self list is {str(l1)}\n")
    print(f"other list is {str(l2)}\n")
    correct = f"[{n3}, {n4}]"
    l3 = l1.intersection(l2)
    str_forward = str(l3)
    str_back = get_str_from_back_pointers(l3)
    print(f"Your intersection list is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l3.len == 2:
        l1_str = f"[{n3}, {n2}, {n10}, {n1}, {n4}, {n5}]"
        l2_str = f"[{n8}, {n3}, {n6}, {n4}, {n7}, {n9}]"
        if (str(l1) == l1_str and get_str_from_back_pointers(l1) == l1_str and
                        l2_str and get_str_from_back_pointers(l2) == l2_str):   
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect.  l1 and l2 not left unchanged.")
    else:
        print(f"Incorrect.  SHould be {correct} and len = 2")

    print("Testing intersection method.  self list empty.\n")
    num_tests += 1
    l1 = OrderedLinkedList()
    l2 = OrderedLinkedList()
    l2.insert(n8)
    l2.insert(n3)
    l2.insert(n6)
    l2.insert(n4)
    l2.insert(n7)
    l2.insert(n9)    
    print(f"self list is {str(l1)}\n")
    print(f"other list is {str(l2)}\n")
    correct = f"[]"
    l3 = l1.intersection(l2)
    str_forward = str(l3)
    str_back = get_str_from_back_pointers(l3)
    print(f"Your intersection list is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l3.len == 0:
        l1_str = f"[]"
        l2_str = f"[{n8}, {n3}, {n6}, {n4}, {n7}, {n9}]"
        if (str(l1) == l1_str and get_str_from_back_pointers(l1) == l1_str and
                        l2_str and get_str_from_back_pointers(l2) == l2_str):   
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect.  l1 and l2 not left unchanged.")
    else:
        print(f"Incorrect.  SHould be {correct} and len = 0")

    print("Testing intersection method.  Other list empty.\n")
    num_tests += 1
    l1 = OrderedLinkedList()
    l1.insert(n3)
    l1.insert(n2)
    l1.insert(n10)
    l1.insert(n1)
    l1.insert(n4)
    l1.insert(n5)
    l2 = OrderedLinkedList()   
    print(f"self list is {str(l1)}\n")
    print(f"other list is {str(l2)}\n")
    correct = f"[]"
    l3 = l1.intersection(l2)
    str_forward = str(l3)
    str_back = get_str_from_back_pointers(l3)
    print(f"Your intersection list is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l3.len == 0:
        l1_str = f"[{n3}, {n2}, {n10}, {n1}, {n4}, {n5}]"
        l2_str = f"[]"
        if (str(l1) == l1_str and get_str_from_back_pointers(l1) == l1_str and
                        l2_str and get_str_from_back_pointers(l2) == l2_str):   
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect.  l1 and l2 not left unchanged.")
    else:
        print(f"Incorrect.  SHould be {correct} and len = 0")

    print("Testing intersection method.  Both lists nonempty, intersection empty.\n")
    num_tests += 1
    l1 = OrderedLinkedList()
    l1.insert(n3)
    l1.insert(n2)
    l1.insert(n10)
    l1.insert(n1)
    l1.insert(n4)
    l1.insert(n5)
    l2 = OrderedLinkedList()
    l2.insert(n8)
    l2.insert(n6)
    l2.insert(n7)
    l2.insert(n9)    
    print(f"self list is {str(l1)}\n")
    print(f"other list is {str(l2)}\n")
    correct = f"[]"
    l3 = l1.intersection(l2)
    str_forward = str(l3)
    str_back = get_str_from_back_pointers(l3)
    print(f"Your intersection list is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l3.len == 0:
        l1_str = f"[{n3}, {n2}, {n10}, {n1}, {n4}, {n5}]"
        l2_str = f"[{n8}, {n6}, {n7}, {n9}]"
        if (str(l1) == l1_str and get_str_from_back_pointers(l1) == l1_str and
                        l2_str and get_str_from_back_pointers(l2) == l2_str):   
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect.  l1 and l2 not left unchanged.")
    else:
        print(f"Incorrect.  SHould be {correct} and len = 0")

    print("Testing intersection method.  Both lists nonempty,")
    print("Some duplicates within self, and within other list")
    num_tests += 1
    l1 = OrderedLinkedList()
    l1.insert(n3)
    l1.insert(n3)
    l1.insert(n3)
    l1.insert(n2)
    l1.insert(n10)
    l1.insert(n1)
    l1.insert(n4)
    l1.insert(n4)
    l1.insert(n4)
    l1.insert(n4)
    l1.insert(n5)
    l2 = OrderedLinkedList()
    l2.insert(n8)
    l2.insert(n3)
    l2.insert(n3)
    l2.insert(n3)
    l2.insert(n3)
    l2.insert(n6)
    l2.insert(n4)
    l2.insert(n4)
    l2.insert(n4)
    l2.insert(n7)
    l2.insert(n9)    
    print(f"self list is {str(l1)}\n")
    print(f"other list is {str(l2)}\n")
    correct = f"[{n3}, {n4}]"
    l3 = l1.intersection(l2)
    str_forward = str(l3)
    str_back = get_str_from_back_pointers(l3)
    print(f"Your intersection list is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l3.len == 2:
        l1_str = f"[{n3}, {n3}, {n3}, {n2}, {n10}, {n1}, {n4}, {n4}, {n4}, {n4}, {n5}]"
        l2_str = f"[{n8}, {n3}, {n3}, {n3}, {n3}, {n6}, {n4}, {n4}, {n4}, {n7}, {n9}]"
        if (str(l1) == l1_str and get_str_from_back_pointers(l1) == l1_str and
                        l2_str and get_str_from_back_pointers(l2) == l2_str):   
            print("Correct")
            num_correct += 1
        else:
            print("Incorrect.  l1 and l2 not left unchanged.")
    else:
        print(f"Incorrect.  SHould be {correct} and len = 2")

    # Done testing.  Check results
    print(f"Num tests = {num_tests}")
    print(f"Num correct = {num_correct}")
    if num_tests == num_correct:
        print("All correct.  Nice job.")
        print("Check all program requirements before submitting")
    else:
        print("Some tests still incorrect.")
        print("Fix before submitting")  

def get_str_from_back_pointers(the_list):
    """
    Returns string representation of the_list, using
    back pointers.
    """   
    items = []
    cur = the_list.back
    while cur:
        items.append(cur.item)
        cur = cur.prev
    if len(items) == 0:
        return "[]"
    else:
        s = "["
        while len(items) > 1:
            s += str(items.pop()) + ", "
        s += str(items.pop()) + "]"
        return s

if __name__ == "__main__":
    ordered_list_test()