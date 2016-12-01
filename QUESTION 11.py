class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None

class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List: ",",".join(values))

      def remove(self, n):
            #if the previous node does not exist, assign the node position to the next available node.
          if n.prev!= None:
              n.prev.next = n.next
          else:
            #make the head of the heap the next available node
              self.head = n.next
      #   #if the next node does not exist then assign that nodes previous position to the current nodes previous position.
          if n.next!= None:
              n.next.prev = n.prev
          else:
            #assign the end of the queue to the nodes previous node.
              self.tail = n.prev
              
if __name__ == '__main__':
      l=List()
      l.insert(None, Node(4))
      l.insert(l.head,Node(6))
      l.insert(l.head,Node(8))
      l.insert(l.head,Node(12))
      l.remove(l.head)
      l.display()
