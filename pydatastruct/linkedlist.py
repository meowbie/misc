# linked list implementation in Python

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return(self.data)

    def connect_aft(self, prev):
        prev.next = self

