class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # the initial capacity of the array
        self.internalArray = [None for i in range(capacity)] # an initially empty array
        self.size = 0 # array is currently empty
        print(self.internalArray)

    def get(self, i: int) -> int:
        return self.internalArray[i]

    def set(self, i: int, n: int) -> None:
        # has the value for this element already been set? 
        if self.internalArray[i] == None: 
            self.size += 1
        self.internalArray[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity: 
            self.resize()

        # insert element into the current end of the array
        self.internalArray[self.size] = n
        # increment the pointer to the end of the array
        self.size += 1 

    def popback(self) -> int:
        if self.size == 0: 
            return None 
        lastElem = self.internalArray[self.size - 1]
        self.internalArray[self.size - 1] = None 
        self.size -= 1 
        return lastElem

    def resize(self) -> None:
        self.capacity = self.capacity*2
        temp = [None for i in range(self.capacity)]
        for i in range(len(self.internalArray)):
            temp[i] = self.internalArray[i]
        self.internalArray = temp 


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
