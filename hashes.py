import numpy as np
import csv

# Patient class to hold patient details
class Patient:
    def __init__(self, id, name, age, dept, urgency, treatment_status, treatment_time=1):
        self.id = id
        self.name = name
        self.age = age
        self.dept = dept
        self.urgency = int(urgency)
        self.treatment_status = treatment_status
        self.treatment_time = int(treatment_time)
    
    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Age: {self.age}, "
                f"Dept: {self.dept}, Urgency: {self.urgency}, "
                f"Status: {self.treatment_status}")  

# Hash entry class to hold key-value pairs and state
class DSAHashEntry:
    def __init__(self, key="", value=None):
        self.key = key
        self.value = value
        self.state = 0

# Hash table class with linear probing
class DSAHashTable:
    def __init__(self, tableSize):
        self.count = 0
        self.actualSize = self.nextPrime(tableSize)
        self.hashArray = np.empty(self.actualSize, dtype=object)
        for i in range(self.actualSize):
            self.hashArray[i] = DSAHashEntry()

# Put method to insert key-value pairs
    def put(self, key, value, inserting=True):
        if (self.count + 1)/ self.actualSize > 0.7:
            self.resize(self.actualSize * 2)

        index = self.findSlot(key)
        if self.hashArray[index].state != 1:
            self.count += 1
        self.hashArray[index].key = key
        self.hashArray[index].value = value
        self.hashArray[index].state = 1

# Get method to retrieve value by key
    def get(self,key):
        index = self.findSlot(key)
        if self.hashArray[index].state != 1:
            raise Exception("Key not found")
        return self.hashArray[index].value

# Method to check if key exists
    def hasKey(self, key):
        index = self.findSlot(key)
        return self.hashArray[index].state == 1

# Remove method to delete key-value pair
    def remove(self, key):
        index = self.findSlot(key)
        if self.hashArray[index].state == 1:
            self.hashArray[index].state = -1
            self.hashArray[index].key = ""
            self.hashArray[index].value = None
            self.count -= 1
            if self.count / self.actualSize < 0.3:
                self.resize(max(7, self.actualSize // 2))

# Simple hashing function where the hash index is multiplied by 33 and added by the character unicode point.
    def hash(self,key): 
        table_size = self.actualSize
        hash_idx = 0
        for char in key:
            hash_idx = (33 * hash_idx + ord(char)) & 0xFFFFFFFF #simulates 32 bit overflow keeping the number under 32 bits for speed
        return hash_idx % table_size

# Linear probing to find the appropriate slot for a key
    def findSlot(self, key, inserting=False):
        hashIdx = self.hash(key)
        origIdx = hashIdx
        giveUp = False

        while not giveUp:
            entry = self.hashArray[hashIdx]
            if entry.state == 0:
                if inserting:
                    return hashIdx
                else:
                    return hashIdx
            elif entry.state == 1 and entry.key == key:
                return hashIdx
            else:
                hashIdx = (origIdx + 1) % self.actualSize
                if hashIdx == origIdx:
                    giveUp = True

        if inserting:
            raise Exception("Hash table is full")
        return hashIdx

# Method to find the next prime number greater than or equal to n
    def nextPrime(self, n):
        def is_prime(x):
            if x < 2: return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n
    
    def resize(self, newSize):
        oldArray = self.hashArray
        oldSize = self.actualSize
        self.actualSize = self.nextPrime(newSize)
        self.hashArray = np.empty(self.actualSize, dtype=object)
        self.count = 0
        for i in range(self.actualSize):
            self.hashArray[i] = DSAHashEntry()

        for i in range(oldSize):
            if oldArray[i].state == 1:
                self.put(oldArray[i].key, oldArray[i].value)

# Method to calculate load factor        
    def loadFactor(self):
        return self.count / self.actualSize

# Method to get all treatment times of patients in the hash table
    def getAllTimes(self):
        durations = []
        for entry in self.hashArray:
            if entry.state == 1 and isinstance(entry.value, Patient):
                durations.append(int(entry.value.treatment_time))
        return durations