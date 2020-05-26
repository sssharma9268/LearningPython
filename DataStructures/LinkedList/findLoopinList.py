class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # self.flag = 0

    def __str__(self):
        return self.data

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
            print(str(temp.data) + " ")
            temp = temp.next

    def hasloop(self):
        current = self.head
        temp = self.head
        loop=False
        while (temp!=None and current!=None and temp.next!=None):
            current=current.next
            temp=temp.next.next
            if(temp==current):
                loop=True
                return loop

    def firstNodeInLoop(self):
        current =self.head
        temp=self.head
        loop=False
        while (temp!=None and current!=None and temp.next!=None):
            current=current.next
            temp=temp.next.next
            if(temp==current):
                loop=True
                break

        if(loop):
            current=self.head
            while(temp!=current):
                temp=temp.next
                current=current.next

            return temp

    def lengthOfLoop(self):
        firstNode = self.firstNodeInLoop()
        temp=firstNode.next
        length=0
        while (firstNode!=temp):
            temp=temp.next
            length+=1

        return length

    def endLoop(self):
        startNode =self.firstNodeInLoop()
        temp=startNode.next
        while(temp.next!=startNode):
            temp=temp.next

        temp.next=None


    def reverseIteratively(self):
        prev=None
        current=self.head
        while(current is not None):
            temp=current.next
            current.next=prev
            prev=current
            current=temp

        self.head=prev


if __name__ == '__main__':

    mylist = LinkedList()
    mylist.add(20)
    mylist.add(4)
    mylist.add(15)
    mylist.add(10)
    mylist.add(5)

    # mylist.head.next.next.next.next = mylist.head.next;
    mylist.displayList()
    mylist.reverseIteratively()
    mylist.displayList()
    # mylist.endLoop()
    # if (mylist.hasloop()):
    #     print("Loop found")
    #     print("Start of Loop", mylist.firstNodeInLoop().data)
    #     print("Length of a loop", mylist.lengthOfLoop())
    # else:
    #     print("No Loop ")
