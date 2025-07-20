#creating class

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating Node 
   
node1 = Node(10)
node2 = Node(20)
node3 = Node(35)

#Connecting Nodes

node1.next = node2
node2.next = node3

#printing   

#O/P: 10>>>20>>>30>>>None


def add_at_anywhere(data,position):
    head = Node(position)
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return new_node

#head = add(55)
head = add_at_anywhere(99,2)

while head is not None:
    print(head.data,end=">>>")
    head = head.next
print('None')
