from DataStructures.HashTable.HashTable import *

hashTable = HashTable()
hashTable.set(1, 10)
hashTable.set(2, 11)
hashTable.set(3, 13)

print(hashTable.delete(2).value)
print(hashTable.get(2))