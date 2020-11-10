
class Node:
    def __init__(self,data =None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty Linked List")
            return
        itr = self.head
        lstr = ""
        while itr:
            lstr += str(itr.data)+ "--->"
            itr = itr.next
        print(lstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index<0 or index >=  self.get_length():
            print("Invalid Index")
            return
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == (index -1):
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
            
    def insert_at(self,index,data):
        if index<0 or index >=  self.get_length():
            print("Invalid Index")
            return
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr =self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node= Node(data_to_insert,itr.next)
                itr.next = node
                return
            itr = itr.next
        print("Data not Found")

    def remove_by_value(self,data):
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        print("Value not Found")


if __name__ == '__main__':
    l = LinkedList()
    l.insert_values(["Hello","my","name","is","Sagar"])
    l.print()
    l.insert_after_value("Sagar","Rawat")
    l.print()
    l.remove_by_value("Rawat")
    l.print()
