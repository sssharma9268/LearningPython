class Node:

    def __init__(self):
        self.str = ""
        self.left = None
        self.right = None
        self.myList = []



def createTree(head, i, len,count):
        if i == len:
            return
        left = Node()
        right = Node()
        left.str = head.str + input[i]
        right.str = head.str
        left.myList=head.myList
        right.myList=head.myList
        head.left = left
        right.left = right

        print(head.str+" "+str(count))

        createTree(left,i+1,len,count+1)

        createTree(right,i+1,len,count+1)

def inorderTraverse(self,head):
    if head == None:
        return
    self.inorderTraverse(head.left)
    print(head.myList)
    self.inorderTraverse(head.right)



if __name__=='__main__':
    count=0
    input = str(input())

    l = len(input)

    head = Node()
    createTree(head,0,l,count)










