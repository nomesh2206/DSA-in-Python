class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def getLength(head):
    #code here
    count = 1
    if head == None:
        return
    #print(head.data, end=" ")
    curr = head.next
    while curr != head:
        #print(curr.data, end=" ")
        count = count+1
        curr = curr.next

    return count

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

print (getlength(head))
