from double_linked_list import TwoWayNode

class Queue:
    def __init__(self) -> TwoWayNode:
        """
        Create a queue based in two way nodes
        """
        self.head = None
        self.tail = None
        self.count = 0

    def iter(self):
        probe = self.head

        while probe != None:
            value = probe.data
            probe = probe.next
            yield value
        yield value

    def length(self) -> int:
        """
        Return length of a Queue
        """
        return self.count

    def enqueue(self, data) -> TwoWayNode:
        """
        add a node into queue.
        """
        new_node = TwoWayNode(data, None, None)

        if self.count == 0:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node

            self.tail = new_node

    def dequeue(self):
        """
        Remove a node from queue
        """
        probe = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.previous = None
            self.coun -= 1
    
        return probe.data