class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def append(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            new_node.next = self.last
        else:
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node
        return self.last.data

    def prepend(self, data):
        new_node = Node(data)
        if self.last is None:
            self.last = new_node
            self.last.next = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node

        return self.last.next.data

    def delete_at_beginning(self):
        if self.last is None:
            print("List is empty. Nothing to delete.")
            return
        temp = self.last.next
        data = temp.data
        if temp == self.last:
            self.last = None
            temp = None
        else:
            self.last.next = temp.next
            temp.next = None
        return temp.data if temp is not None else data

    def delete_at_end(self):
        if self.last is None:
            print("List is empty. Nothing to delete.")
            return
        temp = self.last.next
        data = self.last.data
        prev = None
        if temp.next == temp:
            self.last = None
            temp = None
        else:
            while temp.next != self.last.next:
                prev = temp
                temp = temp.next
            prev.next = self.last.next
            self.last = prev
            temp = None
        return data

    def display(self):
        if self.last is None:
            print("List is empty.")
            return
        temp = self.last.next
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.last:
                print(temp.data)
                break


if __name__ == "__main__":
    cll = CircularLinkedList()
    print("Welcome...")
    while True:
        print("\nSingly Circular Linked List Operations:")
        print("1. Append")
        print("2. Prepend")
        print("3. Delete at Beginning")
        print("4. Delete at End")
        print("5. Display")
        print("6. Exit")

        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            data = int(input("Enter data to append: "))
            print("The appended value is : ", cll.append(data))
        elif choice == 2:
            data = int(input("Enter data to prepend: "))
            print("The prepended value is : ", cll.prepend(data))
        elif choice == 3:
            print("The deleted value from the beginning is : ", cll.delete_at_beginning())
        elif choice == 4:
            print("The deleted value from the end is : ", cll.delete_at_end())
        elif choice == 5:
            print("The elements in the list are : ")
            cll.display()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
