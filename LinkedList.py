class Node:
  def __init__(self,value):
    self.value=value
    self.next=None

class LinkedList:
  #Let's define the constructor 
  def __init__(self,value):
    """
    This contructs an oblect of Node type with initial value passed to this contructor
    and both head and tail pointing to it and initial length of 1.
    -self: tells python this is a mothod inside a class and not a function
    -value: this will be used to create the first node when we initialize the class
    """
    new_node=Node(value)
    self.head=new_node
    self.tail=new_node
    self.length=1
  def printList(self):
    temp=self.head
    while temp is not None:
      print(temp.value)
      temp=temp.next
  def append(self,value):
    new_node=Node(value)
    if self.head is None:
      self.head=new_node
      self.tail=new_node
    else:
      self.tail.next=new_node
      self.tail=new_node
    self.length+=1
    return True
  def pop(self):
    """
    The pop method removes and returns the last node of the linked list
    """
    if self.head is None:
      return None
    else:
      temp=self.head
      pre=self.head
      while temp.next is not None:
        pre=temp #order is important to move preforward
        temp=temp.next
      self.tail=pre
      self.tail.next=None
      self.length-=1
      if self.length==0: #
        self.head=None
        self.tail=None
      return temp
  def prepend(self,value):
    """
    The passed value the method is added at the first location in the linkedList
    """
    new_node=Node(value)
    if self.head is None:
      self.head=new_node
      self.tail=new_node
    else:
      new_node.next=self.head
      self.head=new_node
    self.length+=1
    return True

      
