from linked_list import MyList, ListNode

class Set:
    def __init__(self):
        self.linkedList = MyList()

    def length(self):
        return abs(self.linkedList.__len__)

    def contains(self):
        return self.linkedList.__contains__

    def add(self, item):
        newItem = ListNode(item)
        self.linkedList.add(newItem)

    def remove(self, target):
        self.linkedList.remove(target)

    def isSubsetOf(self, inputSet):
        for element in self.linkedList:
            if element not in inputSet.linkedList:
                return False
        return True

    def equals(self, inputSet):
        if len(self.linkedList) != len(inputSet.linkedList):
            return False
        else:
            return self.isSubsetOf(inputSet)

    def intersection( self, setB ):
        newSet = Set()
        for element in setB.linkedList:
            if self.linkedList.__contains__(element):
                newSet.add(element)
        return newSet

    def __repr__(self):
        output = "Set: "
        newList = list()
        for i in self.linkedList:
            newList.append(i)

        output += str(newList)
        
        return output