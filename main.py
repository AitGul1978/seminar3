from linked_list import MyList, ListNode
from setADT import Set as MySet
from myclass import Person as person
from child import Student as student

mySet = MySet()
secondSet = MySet()

print("Objects:")
john = person('John', 'Malcolm')
print(john)

josh_student = student('Josh', 'Pare', 123)
print(josh_student)

mySet.add(john)
mySet.add(john)
mySet.add(josh_student)
mySet.add(josh_student)
mySet.add(josh_student)
print("Items added:")
print(mySet)

print("Remove John:")
mySet.remove(john)

print(mySet)

secondSet.add(john)
secondSet.add(josh_student)
secondSet.add(josh_student)

print("second Set:")
print(secondSet)
print("isSubsetOf:")
print(mySet.isSubsetOf(secondSet))
print("equals:")
print(mySet.equals(secondSet))
print("intersection:")
print(mySet.intersection(secondSet))

