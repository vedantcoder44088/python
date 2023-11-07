class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            print("The data is not found in the list.")
            return
        prev.next = current.next
        current = None


# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(5)
    linked_list.insert(10)
    linked_list.insert(15)
    linked_list.insert(20)
    linked_list.display()

    linked_list.delete(10)
    linked_list.display()

    linked_list.delete(25)  # Assuming 25 is not present in the list
