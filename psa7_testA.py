# File: psa7_testA.py
# Date: April 19, 2021
# Author: Dr. Glick
# Description: Code to test insert, remove, and remove_all
#    methods of the OrderedLinkedList class. 

from ordered_linked_list import OrderedLinkedList

def ordered_list_test():

    # Create a linked list
    l = OrderedLinkedList()

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
    
    print("Testing insert into empty list\n")
    num_tests += 1
    print(f"list before insert is {str(l)}\n")
    correct = f"[{n1}]"
    l.insert(n1)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after inserting {n1} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 1:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 1")

    print("\n***********\nTesting insert into front of list\n")
    num_tests += 1
    print(f"list before inserts is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n1}]"
    l.insert(n2)
    l.insert(n3)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after inserting {n2} and {n1} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 3:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 3")

    print("\n***********\nTesting insert into back of list\n")
    num_tests += 1
    print(f"list before inserts is {str(l)}\n") 
    correct = f"[{n3}, {n2}, {n1}, {n4}, {n5}]"
    l.insert(n4)
    l.insert(n5)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after inserting {n4} and {n5} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 5:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 5")

    print("\n***********\nTesting insert into middle of list\n")
    num_tests += 1
    print(f"list before inserts is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n6}, {n1}, {n4}, {n7}, {n5}]"
    l.insert(n6)
    l.insert(n7)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after inserting {n6} and {n7} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 7:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 7")

    print("\n***********\nTesting remove of item not in list and smaller than first item\n")
    num_tests += 1
    print(f"list before remove attempt is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n6}, {n1}, {n4}, {n7}, {n5}]"
    try:
        l.remove(n8)
        print(f"Incorrect.  SHould have raised ValueError")   
    except ValueError:
        str_forward = str(l)
        str_back = get_str_from_back_pointers(l)
        print(f"Your list after attempting to remove {n8} is {str_forward}")
        print(f"Your list constructed from back pointers = {str_back}")
        if str_forward == correct and str_back == correct and l.len == 7:
            print("Correct")
            num_correct += 1
        else:
            print(f"Incorrect.  SHould be {correct} and len = 7")

    print("\n***********\nTesting remove of item not in list and bigger than last item\n")
    num_tests += 1
    print(f"list before remove attempt is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n6}, {n1}, {n4}, {n7}, {n5}]"
    try:
        l.remove(n9)
        print(f"Incorrect.  SHould have raised ValueError")   
    except ValueError:
        str_forward = str(l)
        str_back = get_str_from_back_pointers(l)
        print(f"Your list after attempting to remove {n9} is {str_forward}")
        print(f"Your list constructed from back pointers = {str_back}")
        if str_forward == correct and str_back == correct and l.len == 7:
            print("Correct")
            num_correct += 1
        else:
            print(f"Incorrect.  SHould be {correct} and len = 7")

    print("\n***********\nTesting remove of item not in list and greater than the first item and less than the last item\n")
    num_tests += 1
    print(f"list before remove attempt is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n6}, {n1}, {n4}, {n7}, {n5}]"
    try:
        l.remove(n10)
        print(f"Incorrect.  SHould have raised ValueError")   
    except ValueError:
        str_forward = str(l)
        str_back = get_str_from_back_pointers(l)
        print(f"Your list after attempting to remove {n10} is {str_forward}")
        print(f"Your list constructed from back pointers = {str_back}")
        if str_forward == correct and str_back == correct and l.len == 7:
            print("Correct")
            num_correct += 1
        else:
            print(f"Incorrect.  SHould be {correct} and len = 7")


    print("\n***********\nTesting remove from front of list\n")
    num_tests += 1
    print(f"list before remove is {str(l)}\n")
    correct = f"[{n2}, {n6}, {n1}, {n4}, {n7}, {n5}]"
    l.remove(n3)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing {n3} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 6:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 6")

    print("\n***********\nTesting remove from back of list\n")
    num_tests += 1
    print(f"list before remove is {str(l)}\n")
    correct = f"[{n2}, {n6}, {n1}, {n4}, {n7}]"
    l.remove(n5)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing {n5} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 5:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 5")

    print("\n***********\nTesting remove from middle of list\n")
    num_tests += 1
    print(f"list before remove is {str(l)}\n")
    correct = f"[{n2}, {n6}, {n4}, {n7}]"
    l.remove(n1)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing {n1} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 4:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 4")

    print("\n***********\nTesting remove of last item from list\n")
    num_tests += 1
    print(f"list before remove is {str(l)}\n")
    correct = f"[]"
    l.remove(n6)
    l.remove(n4)
    l.remove(n7)
    l.remove(n2)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing {n6}, {n4}, {n7}, {n2} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 0:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and l = 0")

    print("\n***********\nTesting remove of item from empty list\n")
    num_tests += 1
    print(f"list before remove attempt is {str(l)}\n")
    correct = f"[]"
    try:
        l.remove(n10)
        print(f"Incorrect.  SHould have raised ValueError")   
    except ValueError:
        str_forward = str(l)
        str_back = get_str_from_back_pointers(l)
        print(f"Your list after attempting to remove {n10} is {str_forward}")
        print(f"Your list constructed from back pointers = {str_back}")
        if str_forward == correct and str_back == correct and l.len == 0:
            print("Correct")
            num_correct += 1
        else:
            print(f"Incorrect.  SHould be {correct} and len = 0")

    print("\n***********\nTesting remove all, where first and last instances are in middle of list\n")
    num_tests += 1
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n1)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    print(f"list before remove all {n1} is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n4}, {n5}]"
    l.remove_all(n1)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing all {n1} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 4:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 4")

    print("\n***********\nTesting remove all, where first instance is the front of list")
    print("and last is in middle of list\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n1)
    l.insert(n1)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    print(f"list before remove all {n1} is {str(l)}\n")
    correct = f"[{n4}, {n5}]"
    l.remove_all(n1)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing all {n1} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 2:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 2")

    print("\n***********\nTesting remove all, where first instance in the middle of the list")
    print("and last is at the end of the list\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n1)
    l.insert(n1)
    print(f"list before remove all {n1} is {str(l)}\n")
    correct = f"[{n3}, {n2}]"
    l.remove_all(n1)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing all {n1} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 2:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 2")

    print("\n***********\nTesting remove all, where first instance is the front of the list")
    print("and last is at the end of the list\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n1)
    l.insert(n1)
    l.insert(n1)
    print(f"list before remove all {n1} is {str(l)}\n")
    correct = f"[]"
    l.remove_all(n1)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing all {n1} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 0:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 0")

    print("\n***********\nTesting remove all, with only one instance in the list\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    print(f"list before remove all {n1} is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n4}, {n5}]"
    l.remove_all(n1)
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after removing all {n1} is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 4:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 4")

    print("\n***********\nTesting remove all of item not in list\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    print(f"list before remove attempt is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n1}, {n4}, {n5}]"
    try:
        l.remove(n10)
        print(f"Incorrect.  SHould have raised ValueError")   
    except ValueError:
        str_forward = str(l)
        str_back = get_str_from_back_pointers(l)
        print(f"Your list after attempting to remove {n10} is {str_forward}")
        print(f"Your list constructed from back pointers = {str_back}")
        if str_forward == correct and str_back == correct and l.len == 5:
            print("Correct")
            num_correct += 1
        else:
            print(f"Incorrect.  SHould be {correct} and len = 5")

    print("\n***********\nTesting remove duplicates.  Duplicates at beginning of list\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n3)
    l.insert(n3)
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    print(f"list before remove duplicates is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n1}, {n4}, {n5}]"
    l.remove_duplicates()
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after remove_duplicates is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 5:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 5")

    print("\n***********\nTesting remove duplicates.  Duplicates at end of list\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    l.insert(n5)
    l.insert(n5)
    print(f"list before remove duplicates is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n1}, {n4}, {n5}]"
    l.remove_duplicates()
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after remove_duplicates is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 5:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 5")

    print("\n***********\nTesting remove duplicates.  Duplicates in middle of list\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n1)
    l.insert(n1)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    print(f"list before remove duplicates is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n1}, {n4}, {n5}]"
    l.remove_duplicates()
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after remove_duplicates is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 5:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 5")

    print("\n***********\nTesting remove duplicates.  Duplicates in multiple places\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n3)
    l.insert(n3)
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n1)
    l.insert(n1)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    l.insert(n5)
    l.insert(n5)
    print(f"list before remove duplicates is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n1}, {n4}, {n5}]"
    l.remove_duplicates()
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after remove_duplicates is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 5:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 5")

    print("\n***********\nTesting remove duplicates.  No duplicates\n")
    num_tests += 1
    l = OrderedLinkedList()
    l.insert(n3)
    l.insert(n2)
    l.insert(n1)
    l.insert(n4)
    l.insert(n5)
    print(f"list before remove duplicates is {str(l)}\n")
    correct = f"[{n3}, {n2}, {n1}, {n4}, {n5}]"
    l.remove_duplicates()
    str_forward = str(l)
    str_back = get_str_from_back_pointers(l)
    print(f"Your list after remove_duplicates is {str_forward}")
    print(f"Your list constructed from back pointers = {str_back}")
    if str_forward == correct and str_back == correct and l.len == 5:
        print("Correct")
        num_correct += 1
    else:
        print(f"Incorrect.  SHould be {correct} and len = 5")

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