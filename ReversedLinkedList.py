class Node:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class LinkedList:
    def __init__(self, head=None):
        self.head=Node()

def reversedLinkedList(list:LinkedList):
    cur = list.head
    prev = None

    while cur:
        # save next node in temp variable
        temp = cur.next
        
        # next value of current node is prev
        cur.next= prev
        # prev is  cur-node now 
        prev = cur
         # then cur now is next node
        cur = temp

        

