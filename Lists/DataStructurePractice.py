"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        first_position = self.head
        x=1
        while x < position:
            first_position = first_position.next
            x +=1
        if first_position:
            return first_position
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements.

        newelemnt.next= last elemt.next
        last element.next =new element
        """

        first_pos = self.head
        x=1
        # found = False

        if position ==1:
            new_element.next = self.head
            self.head = new_element
            return
        while x < position-1:
            first_pos = first_pos.next
            x +=1

        new_element.next = first_pos.next
        first_pos.next = new_element
        return

    def delete(self, position):
        """Delete the first node with a given value."""

        first_pos = self.head
        # curr = self.head
        x = 1

        if position ==1:
            self.head = self.head.next
        while x < position-1:
            first_pos = first_pos.next

        first_pos.next = first_pos.next.next
        return



    def reverseLinkedList(self):
        current = self.head
        length = 1
        previous = None
        while current != None:
            next_node = current.next #2           1 2 3 4
            current.next = previous  # 3 = None
            previous = current # previous = 1...234
            current = next_node  # 1 = 2
        self.head = previous
        return self.head




# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(1).value)
print(ll.get_position(2).value)
print(ll.get_position(3).value)


# Test insert
ll.insert(e4, 4)
# Should print 4 now
print(ll.get_position(3).value)

# print(f"yoyo: {ll.head.next.next.value}")
print("--------------")
# Test delete
# ll.delete(3)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
print(ll.get_position(4).value)
print("------------")
# print(ll.head.next.next.next.value)

print(ll.reverseLinkedList().value)

print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)
print(ll.get_position(4).value)
