class DSAListNode:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None
    
    def getValue(self):
        return self.value
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setNext(self, newNext):
        self.next = newNext

    def setPrev(self, newPrev):
        self.prev = newPrev


class DSALinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 
    
    def isEmpty(self):
        return self.head is None and self.tail is None
    
    def peekFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        return self.head.getValue()

    def peekLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        return self.tail.getValue()
    
    def insertFirst(self, newItem):
        newNode = DSAListNode(newItem)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
        self.size += 1
    
    def insertLast(self, newItem):
        newNode = DSAListNode(newItem)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
        self.size += 1
    
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("List is empty")
        removedValue = self.head.getValue()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.getNext()
            self.head.setPrev(None)
        self.size -= 1
        return removedValue

    def removeLast(self):
        if self.isEmpty():
            raise Exception("List is empty")
        removedValue = self.tail.getValue()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.getPrev()
            self.tail.setNext(None)
        self.size -= 1
        return removedValue

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.getValue()
            current = current.getNext()

if __name__ == "__main__":
    linked_list = DSALinkedList()

    def display_list():
        if linked_list.isEmpty():
            print("List is empty.")
        else:
            print("List contents: ", end="")
            for value in linked_list:
                print(value, end=" ")
            print()

    while True:
        print("\nLinked List Menu:")
        print("1. Insert First")
        print("2. Insert Last")
        print("3. Remove First")
        print("4. Remove Last")
        print("5. Display List")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                val = input("Enter value to insert at the front: ")
                linked_list.insertFirst(val)
            elif choice == "2":
                val = input("Enter value to insert at the end: ")
                linked_list.insertLast(val)
            elif choice == "3":
                removed = linked_list.removeFirst()
                print(f"Removed from front: {removed}")
            elif choice == "4":
                removed = linked_list.removeLast()
                print(f"Removed from end: {removed}")
            elif choice == "5":
                display_list()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose 1-6.")
        except Exception as e:
            print("Error:", e)