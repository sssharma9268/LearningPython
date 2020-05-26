class Node:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root =Node(data)
        else:
             current =self.root
             prev=None

             while current is not None:
                 prev=current
                 if data<current.data:
                     current=current.left
                 else:
                     current=current.right

             if data<prev.data:
                 prev.left=Node(data)
             else:
                 prev.right=Node(data)


    def heightofNode(self,data): #height is distance of node from longest leaf node...height of leaf node is 0. Height of tree is maxDepth of tree
        node=self.searchNode(data)
        if node is None:  #height of empty node is -1
            return -1
        if node.right is None and node.left is None:#height of node with no left and right child is 0
            return 0

        height=-1
        myList = []
        myList.append(node)

        while True:
            nodeCount=len(myList)  #indicates the number of nodes at current level
            if nodeCount == 0:
                return height
            height += 1
            while nodeCount > 0:
                temp = myList.pop(0)
                if temp.left:
                    myList.append(temp.left)
                if temp.right:
                    myList.append(temp.right)
                nodeCount -= 1


    def depthofNode(self,data):  #distance of node from the root...root is at depth 0
        if self.root is None:
            return
        depth=0
        if data == self.root.data:
            print("\nDepth of Node:->"+ str(data )+ " is: "+ str(depth))
            return depth
        else:
            temp = self.root

            while True:
                if data < temp.data:
                    temp = temp.left
                else:
                    temp = temp.right
                depth+=1

                if temp is None:
                    print("Node not present")
                    return -1

                if temp.data == data:
                    print("\nDepth of Node:->"+ str(data )+ " is: "+ str(depth))
                    return depth

    def isBST(self):
        if self.root is None:
            return True

        myList = []
        temp=self.root
        myList.append(temp)
        while temp.left is not None:
            if temp.data < temp.left.data:
                return False
            temp = temp.left
            myList.append(temp)

        while len(myList)!=0:
            temp=myList.pop()

            if temp.right is not None:
                if temp.data > temp.right.data:
                    return False

                temp=temp.right
                myList.append(temp)
                while temp.left is not None:
                    if temp.data < temp.left.data:
                        return False
                    temp = temp.left
                    myList.append(temp)
        return True

    def getMin(self,node):
        if node is None:
            return
        if node.left is None:
            return node
        else:
            while (node.left):
                node = node.left

            return node

    def inOrderSuccessor(self,data):
        current = self.searchNode(data)
        if current is None:
            return
        if (current.right):
            return self.getMin(current.right)
        else:
            successor=None
            ancestor=self.root
            while ancestor!=current:
                if(current.data < ancestor.data):
                    successor=ancestor
                    ancestor=ancestor.left
                else:
                    ancestor=ancestor.right

            return successor

    def inOrder(self):
        if self.root is None:
            print("No data to traverse")
            return
        myList = []
        temp=self.root
        myList.append(temp)
        while temp.left is not None:
            temp = temp.left
            myList.append(temp)

        while len(myList)!=0:
            temp=myList.pop()
            print(temp.data,end="->")
            if temp.right is not None:
                temp=temp.right
                myList.append(temp)
                while temp.left is not None:
                    temp = temp.left
                    myList.append(temp)


    def preOrder(self):
        if self.root is None:
            print("No data to traverse")
            return
        myList = []
        myList.append(self.root)
        while len(myList)!=0:
            temp=myList.pop()
            print(temp.data,end="->")
            if temp.right is not None:
                myList.append(temp.right)
            if temp.left is not None:
                myList.append(temp.left)

    def postOrder(self):
        if self.root is None:
            print("No data to traverse")
            return
        myList = []
        myList2 = []
        temp=self.root
        while temp is not None:
            myList.append(temp)
            if temp.right is not None:
                myList.append(temp.right)
            temp=temp.left
        # for t in myList:
        #     print(t.data)

        while len(myList)!=0:
            temp=myList[-1]
            # myList.append(temp)
            if temp.right is not None and temp.right not in myList2:
                myList.append(temp.right)
            if temp.left is not None and temp.left not in myList2:
                myList.append(temp.left)
            temp=myList.pop()
            myList2.append(temp)
            print(temp.data,end="->")



    def levelOrder(self):
        if self.root is None:
            print("No data to traverse")
            return
        myList = []
        myList.append(self.root)
        while len(myList)!=0:
            temp=myList.pop(0)
            print(temp.data,end="->")
            if temp.left is not None:
                myList.append(temp.left)
            if temp.right is not None:
                myList.append(temp.right)

    def searchNode(self,data):
        print("\nSearching:",data)
        if self.root is None:
            return None
        else:
            if data==self.root.data:
                print("Found at Root Node:->",data)
                return self.root
            else:
                temp=self.root

                while True:
                    if data<temp.data:
                        temp=temp.left
                    else:
                        temp=temp.right

                    if temp is None:
                        print("Not Found")
                        return None

                    if temp.data == data:
                        print("found")
                        return temp


    def deleteNode(self,data):
        if self.root is None:
            return

        nodeTobeDeleted = self.searchNode(data)

        if nodeTobeDeleted is None:
            print("Node to be deleted not found")
            return
        else:
            print("Deleting Node:->",nodeTobeDeleted.data)
            parentOfnodeTobeDeleted = None
            temp = self.root
            while temp != nodeTobeDeleted:
                parentOfnodeTobeDeleted = temp
                if nodeTobeDeleted.data < temp.data:
                    temp = temp.left
                else:
                    temp = temp.right

            #Case:-1 node has no child
            if nodeTobeDeleted.left is None and nodeTobeDeleted.right is None:
                print("Node is leaf Node")
                temp=nodeTobeDeleted
                if nodeTobeDeleted.data < parentOfnodeTobeDeleted.data:
                    parentOfnodeTobeDeleted.left=None
                else:
                    parentOfnodeTobeDeleted.right=None

                return temp

            #Case:-2 node has one child
            if (nodeTobeDeleted.right) and not (nodeTobeDeleted.left):
                print("Node has only right Child")
                if nodeTobeDeleted.right.data < parentOfnodeTobeDeleted.data:
                    parentOfnodeTobeDeleted.left=nodeTobeDeleted.right
                else:
                    parentOfnodeTobeDeleted.right=nodeTobeDeleted.right
                return nodeTobeDeleted
            if (nodeTobeDeleted.left) and not nodeTobeDeleted.right:
                print("Node has only left child")
                # print("Parent Of node to be deleted-->",parentOfnodeTobeDeleted.data)
                if nodeTobeDeleted.left.data < parentOfnodeTobeDeleted.data:

                    parentOfnodeTobeDeleted.left=nodeTobeDeleted.left
                else:
                    parentOfnodeTobeDeleted.right=nodeTobeDeleted.left
                return nodeTobeDeleted

            #Case:-3 node has two child. In this case in-order successor will replace the node to be deleted
            if (nodeTobeDeleted.right) and (nodeTobeDeleted.left):
                print("Node has both childs")
                temp=nodeTobeDeleted
                successor=self.inOrderSuccessor(nodeTobeDeleted.data)
                print("Found Successor. Replacing node with successor and deleting successor",successor.data)
                node=self.deleteNode(successor.data)
                nodeTobeDeleted.data=successor.data
                return temp

    def getRoot(self):
        return self.root

if __name__ == '__main__':
    tree = Tree()
    tree.insert(15)
    tree.insert(10)
    tree.insert(20)
    tree.insert(8)
    tree.insert(14)
    tree.insert(17)
    tree.insert(25)
    tree.insert(6)
    tree.insert(11)
    tree.insert(12)
    tree.insert(13)
    tree.insert(16)
    tree.insert(27)
    # tree.insert(12)
    # tree.insert(14)

    root=tree.getRoot()
    print("Level Order Traversal: BFS")
    tree.levelOrder()
    print("\nDFS")
    print("In-Order Traversal")
    tree.inOrder()
    print("\nPre-Order Traversal")
    tree.preOrder()
    print("\nPost-Order Traversal")
    tree.postOrder()
    # foundNode=tree.searchNode(12)
    # # tree.deleteNode(4)
    # print("Inorder-Successor")
    # successor=tree.inOrderSuccessor(10)
    # print(successor.data)
    # print("Finding Minimum")
    # min=tree.getMin(tree.root)
    # print("\nMin Data",min.data)

    # node =tree.deleteNode(56)
    # print("Deleted Node",node.data)
    # tree.inOrder()
    tree.depthofNode(14)
    isBst = tree.isBST()
    if isBst:
        print("The given tree is Binary search Tree")
    else:
        print("The given tree is not Binary Search Tree")

    height=tree.heightofNode(25)
    print("Height of node:-",height)
