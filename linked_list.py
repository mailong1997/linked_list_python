class Node:
    def __init__(self, data = None, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def printLinked_List (self):
        # liên hệ cái node
        head = self.head

        #đi qua hết các giá trị
        while head != None:
            print(str(head.data) + " -> ", end = "")
            head = head.next
        
    def index(self, id):  # id > 0
        node_next = self.head
        # dataIndex = 1
        # B2: Đi tới next kế tiếp
        while node_next != None and id > 0: # node_next = node_2 and 1 > 0:
            id = id - 1 # 0
            # dataIndex = node_next.data
            node_next = node_next.next #node_2 -> node_ 3

        return node_next 
    
    def len(self):
        count = 0
        head = self.head
        while head != None:
            count += 1
            head = head.next
        return count


    def append(self, new_node):

        temp = Node(new_node)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = self.tail.next
    
    def insert(self, id, data):

        newNode = Node(data = data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if id == 0:
                temp = self.head
                self.head = newNode
                self.head.next = temp
            if id >= self.len()-1 or id < 0:
                self.tail.next = newNode
                self.tail = self.tail.next

            else:
                prevNode = self.index(id = id - 1)
                temp = prevNode.next
                prevNode.next = newNode
                newNode.next = temp
    
    def pop (self, id):
        if id == 0:
            temp = self.head.next
            del self.head
            self.head = temp

        elif id == self.len() - 1:
            del self.tail
            temp = self.index(id - 1)
            temp.next = None
            self.tail = temp
        
        elif id > 0 and id <= self.len() - 2:
            tmp3 = self.index(id-1)
            tmp4 = tmp3.next
            tmp3.next = tmp4.next
            del tmp4
        
        else:
            print("Index Error: out of range")


Ls = LinkedList()
