class LinkedListNode: 
    def __init__(self, value, next):
        self.next = next 
        self.value = value 

    
class LinkedList:
    
    def __init__(self):
        self.head = None 
        self.size = 0 
    
    def get(self, index: int) -> int:
        i = 0 
        temp = self.head 
        while temp: 
            if i == index: 
                return temp.value
            i += 1
            temp = temp.next 
        return -1

    def insertHead(self, val: int) -> None:
        # make the head pointer point to a new head 
        # and connect the new head to the old head, if one 
        # existed 
        self.head = LinkedListNode(val,self.head)
        self.size += 1

    def insertTail(self, val: int) -> None:
        temp = self.head 
        prev = None 
        while temp: 
            prev = temp
            temp = temp.next
        
        if not prev: 
            # list is empty
            self.head = LinkedListNode(val,None)
        else: 
            # at least one element in list
            prev.next = LinkedListNode(val,None)
        self.size += 1 

    def remove(self, index: int) -> bool:
        if self.size == 0 or index >= self.size or index < 0: 
            return False # nothing to remove 
        else:
            if index == 0: 
                self.head = self.head.next 
            else: 
                temp = self.head
                prev = None
                i = 0 
                while i != index: 
                    i += 1 
                    prev = temp 
                    temp = temp.next 
                prev.next = temp.next 

        self.size -= 1 
        return True


    def getValues(self) -> List[int]:
        temp = self.head 
        values = []
        while temp: 
            values.append(temp.value)
            temp = temp.next 

        return values 
