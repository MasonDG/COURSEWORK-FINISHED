class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 
 
def in_order(tree):
    #this creates an empty stack that will append tree nodes
    s = []
    #this variable will turn true after each tree node has been examined
    done = False
    while(done != True):
        #append the first node found to the stack then assign the lower value as the root
        if tree != None:     
            s.append(tree)
            tree = tree.left
        #Go back to the top node once the left side is done, check the right side
        elif len(s) >0 :
            #pop the most recent value from the stack which is the top node, print its value then look on the right side nodes.
                tree = s.pop()
                print (tree.value)
                tree = tree.right
        #repeat the same principles from left side to right, once the right side is empty, set the done variable to true to stop running the function.
        else:
                done = True
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
