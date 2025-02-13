# https://www.youtube.com/watch?v=DDU0g4-H4fU&t=1s&ab_channel=KantanCoding
# Merge Two Sorted linked lists and return it as a sorted list. The list should be made 
# by splicing together the nodes of the first two lists.

# Defenition for singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    

def mergeTwoSortedLists(l1, l2):
    # we create a empty ListNode() or node
    # we will add our node here (it is singled linked list then we could go backwards)
    placeholder = ListNode() # value = 0, next=None
    # tail also pointing to the empty node
    tail = placeholder # pointing to the val=0

#  pointers are linked to the nodes in l1 and l2 subsequently
    l1_pointer = l1 # head
    l2_pointer = l2 # head

#  we loop through nodes until the end of LinkedList
    while l1_pointer and l2_pointer:
        # if value in pointer1 less than in pointer2 we 
        # add val in pointer1 to the next value in tail (= head)  
        if l1_pointer.val < l2_pointer.val:
            tail.next = l1_pointer
            # move to the next val in pointer1
            l1_pointer = l1_pointer.next
        else:
            # l1_pointer.val > l2_pointer.val:
            tail.next = l2_pointer
            # move to the next value in the pointer2
            l2_pointer = l2_pointer.next
        # we update = move tail to the next
        # val1 (next-val2)-->val2(next-val3)-->val3 ....--> tail.next=null
        tail = tail.next
# checking if linkedLists are not empty (not of them equally reaching the end)
    if l1_pointer:
        tail.next = l1_pointer
    elif l2_pointer:
        tail.next = l2_pointer

    return placeholder.next




if __name__ == "__main__":
    # l1 = [1, 2, 3], l2 = [1, 3, 4]
    # output [1, 2, 3, 4 ,4]
    # l1 nodes
    l1 = ListNode(1) # head
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1) # head
    l2.next = ListNode(3) # next elemnt (head--> next)
    l2.next.next = ListNode(4) # next elemnt (head--> next-->next.next)


    mergedList = mergeTwoSortedLists(l1, l2)

    #------iterate mergedList-------
    node = mergedList
    while node:
        print(node.val)
        node=node.next
