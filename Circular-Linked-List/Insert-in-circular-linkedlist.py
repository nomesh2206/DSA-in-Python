# Node class definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to insert a node at the head of a circular linked list
def insertInHead(head, x):
    temp = Node(x)
    
    if head is None:
        temp.next = temp
        return temp
        
    curr = head
    while curr.next != head:
        curr = curr.next
        
    curr.next = temp
    temp.next = head
    
    return temp

# Function to print the circular linked list
def printList(head):
    if head is None:
        return

    temp = head
    while True:
        print(temp.data, end=" ")
        temp = temp.next
        if temp == head:
            break
    print()

# Driver code
head = None
head = insertInHead(head, 1)
head = insertInHead(head, 2)
head = insertInHead(head, 3)

print("Circular Linked List after insertion at head:")
printList(head)
