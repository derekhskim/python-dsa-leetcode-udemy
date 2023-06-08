class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        '''
        create new Node
        add Node to end
        '''

        pass

    def prepend(self, value):
        '''
        create new Node
        add Node to beginning
        '''
        pass

    def insert(self, index, value):
        '''
        create new Node
        insert Node to indext
        '''
        pass

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)