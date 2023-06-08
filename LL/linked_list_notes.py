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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        '''
        create new Node
        add Node to end
        '''
        new_node = Node(value)
        self.head = value
        self.tail = new_node
        self.length = self.length + 1

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