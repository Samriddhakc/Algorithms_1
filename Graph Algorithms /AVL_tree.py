
import pdb

class Tree_Node:

    def __init__(self,val):
        self.curr_val=val
        self.left=None
        self.right=None
        self.height=1

class AVL_Tree:

    def _insert(self,iter,key):

        #step 1:Do normal insertions like in a Binary Tree. Samr as forming a while loop
        if not iter:
            return Tree_Node(key)
        elif iter.curr_val<=key:
            iter.right=self._insert(iter.right,key)
        else:
            iter.left=self._insert(iter.left,key)
        #update the height of the ancestor nodes
        print("the current key-iter val is",(key,iter.curr_val))
        iter.height=1+max(self.getHeight(iter.left),self.getHeight(iter.right))
        #get balance factor of the nodes
        balance=self.getBalance(iter)
        #step 4-If the node is unbalanced, then try out the four possible  cases for rotation
        #Case 1:Left-left
        if balance>1 and key<iter.left.curr_val:
            print("Loop1")
            return self.rightRotate(iter)

        #Case 2:Right-Right
        if balance<-1 and key>iter.right.curr_val:
            print("Loop2")
            return self.leftRotate(iter)

        #Case 3: Left-Right
        if balance>1 and key>iter.left.curr_val:
            print("Loop3")
            iter.left=self.leftRotate(iter.left)
            return self.rightRotate(iter)

        #Case 4: Right-Left
        if balance<-1 and key<iter.right.curr_val:
            print("Loop4")
            iter.right=self.rightRotate(iter.right)
            return self.leftRotate(iter)

        return iter

    def getBalance(self,var_node):
        if not var_node:
            return 0
        return self.getHeight(var_node.left)-self.getHeight(var_node.right)

    def getHeight(self,var_node):
        if not var_node:
            return 0
        else:
            return var_node.height


    def rightRotate(self,z):
        y=z.left
        T3=y.right

        #perform rotation
        z.left=T3
        y.right=z

        z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    def leftRotate(self,z):
         y=z.right
         T2=y.left

         #perform rotation
         y.left=z
         z.right=T2

         z.height=1+max(self.getHeight(z.left),self.getHeight(z.right))
         y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))

         return y

    def print_pre_order(self,iter):
        self._print_pre_order(iter)

    def pre_order_2(self,iter):

        if not iter:
            return

        print("{0} ".format(iter.curr_val), end="")
        self.pre_order_2(iter.left)
        self.pre_order_2(iter.right)

    def _print_pre_order(self,iter):
        print(iter.curr_val)
        if iter.left==None and iter.right==None:
            return
        else:
            if iter.left!=None:
                self._print_pre_order(iter.left)
            if iter.right!=None:
                self._print_pre_order(iter.right)


def main():

    AVL_t=AVL_Tree()
    iter=None
    iter=AVL_t._insert(iter,10)
    iter=AVL_t._insert(iter,20)
    iter=AVL_t._insert(iter,5)
    iter=AVL_t._insert(iter,30)
    iter=AVL_t._insert(iter,40)
    iter=AVL_t._insert(iter,25)
    #AVL_t.print_pre_order(iter)

main()
