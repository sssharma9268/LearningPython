class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.flag = 0


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        if (self.head!=None):
            temp = Node(data)
            temp.next=None

            current=self.head
            while (current.next!=None):
                current = current.next
            current.next = temp

        else:
            new_node = Node(data)
            new_node.next = None
            self.head = new_node

    def displayList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " "+str(temp.flag))
            temp = temp.next

    def loops(self):
        # l = []
        # temp = self.head
        # while (temp):
        #     if (temp in l):
        #         return True
        #     l.append(temp)
        #     temp = temp.next
        # return False
        #flag = 0
        #temp=self.head

        # while (temp):
        #     temp.flag =1
        #     temp = temp.next
        #     if (temp.next!=None and temp.next.flag ==1):
        #         return True
        #     if temp.next == None:
        #         return False
        current = self.head
        temp = current.next.next
        while (temp.data!=current.data):
            if(temp==current):
                return True
            current = current.next
            temp = current.next.next

mylist = LinkedList()
mylist.add(20)
mylist.add(4)
mylist.add(15)
mylist.add(10)

mylist.displayList()


mylist.head.next.next.next = mylist.head.next;

if (mylist.loops()):
    print("Loop found")
else:
    print("No Loop ")