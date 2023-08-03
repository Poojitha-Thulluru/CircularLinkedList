class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head, self.tail = new_node, new_node
            new_node.prev = self.tail
            new_node.next = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        return data

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head, self.tail = new_node, new_node
            new_node.prev = self.tail
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node
        return data

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        temp = self.head
        data = temp.data
        if self.head == self.head.next:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        temp = None
        return data if temp is None else None

    def delete_at_end(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        temp = self.tail
        data = temp.data
        if self.tail == self.tail.next:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        temp = None
        return data if temp is None else None

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while temp != self.tail:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data)
        temp = None


if __name__ == "__main__":
    d_cll = CircularLinkedList()
    print("Welcome...")
    while True:
        print("\nDoubly Circular Linked List Operations:")
        print("1. Append")
        print("2. Prepend")
        print("3. Delete at Beginning")
        print("4. Delete at End")
        print("5. Display")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            data = int(input("Enter data to append: "))
            print("The appended value is : ", d_cll.append(data))
        elif choice == 2:
            data = int(input("Enter data to prepend: "))
            print("The prepended value is : ", d_cll.prepend(data))
        elif choice == 3:
            print("The deleted value from the beginning is : ", d_cll.delete_at_beginning())
        elif choice == 4:
            print("The deleted value from the end is : ", d_cll.delete_at_end())
        elif choice == 5:
            print("The elements in the list are : ")
            d_cll.display()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
