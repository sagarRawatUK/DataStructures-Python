class Node:
    def __init__(self,data = None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head == None:
            print("Empty List")
            return
        itr = self.head
        lstr=''
        while itr:
            lstr += str(itr.data)+ "<--->"
            itr = itr.next
        print(lstr)
    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr

    def print_backward(self):
        if self.head == None:
            print("Empty List")
            return
        itr = self.get_last_node()
        lstr=''
        while itr:
            lstr += str(itr.data)+ "<--->"
            itr = itr.prev
        print(lstr)

    def insert_at_begining(self,data):
        node = Node(data,None,self.head)
        self.head.prev = node
        self.head = node

    def insert_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None,None)
            return
        itr = self.head
        while itr:
            if itr.next == None:
                itr.next = Node(data,itr,None)
                return
            itr = itr.next

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index<0 or index >= self.get_length():
            print("Invalid Index")
            return
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        count =0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                itr.next.next.prev = itr
                return
            itr = itr.next
        

    def insert_at(self,index,data):
        if index<0 or index >= self.get_length():
            print("Invalid Index")
            return
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data,itr,itr.next)
                if node.next:
                    node.next.prev = node
                itr.next = node
            itr = itr.next
            count +=1

if __name__ == "__main__":
    l = LinkedList()
    l.insert_values(["HEllo","My","Name","is","sagar"])
    l.insert_at(2,"Good")
    l.print_forward()
    l.print_backward()
        