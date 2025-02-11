'''Barney is writing a program to store data in a linked list. He is writing the initial program for a maximum of 10 data items.
Each node in the linked list has a data value and a pointer (to the next item).
A null pointer is stored with the value –1.
Barney wants the nodes to be stored as objects using object-oriented programming.'''
listOfNodes = []
count = 0

class Node():

    def __init__(self):
        self.data = 0.0
        self.pointer = 0

    def set_pointer(self, newPointer):
        self.pointer = newPointer

    def set_data(self, newData):
        self.data = newData

    def get_pointer(self):
        return self.pointer

    def get_data(self):
        return self.data     
    

    '''main starts here'''

myNode = Node()
listOfNodes.append(myNode)
count += 1

myNode = Node()
listOfNodes.append(myNode)
count += 1

for node in listOfNodes:
    print(node.get_data())

