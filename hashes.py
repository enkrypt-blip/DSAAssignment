import numpy as np
import csv

class Patient:
    def __init__(self, id, name, age, dept, urgency, treatment_status):
        self.id = id
        self.name = name
        self.age = age
        self.dept = dept
        self.urgency = int(urgency)
        self.treatment_status = treatment_status
    
    def __str__(self):
        return (f"ID: {self.id}, Name: {self.name}, Age: {self.age}, "
                f"Dept: {self.dept}, Urgency: {self.urgency}, "
                f"Status: {self.treatment_status}")

class DSAHashEntry:
    def __init__(self, key="", value=None):
        self.key = key
        self.value = value
        self.state = 0

class DSAHashTable:
    def __init__(self, tableSize):
        self.count = 0
        self.actualSize = self.nextPrime(tableSize)
        self.hashArray = np.empty(self.actualSize, dtype=object)
        for i in range(self.actualSize):
            self.hashArray[i] = DSAHashEntry()

    def put(self, key, value, inserting=True):
        if (self.count + 1)/ self.actualSize > 0.7:
            self.resize(self.actualSize * 2)

        index = self.findSlot(key)
        if self.hashArray[index].state != 1:
            self.count += 1
        self.hashArray[index].key = key
        self.hashArray[index].value = value
        self.hashArray[index].state = 1

    def get(self,key):
        index = self.findSlot(key)
        if self.hashArray[index].state != 1:
            raise Exception("Key not found")
        return self.hashArray[index].value

    def hasKey(self, key):
        index = self.findSlot(key)
        return self.hashArray[index].state == 1

    def remove(self, key):
        index = self.findSlot(key)
        if self.hashArray[index].state == 1:
            self.hashArray[index].state = -1
            self.hashArray[index].key = ""
            self.hashArray[index].value = None
            self.count -= 1
            if self.count / self.actualSize < 0.3:
                self.resize(max(7, self.actualSize // 2))

# Simple hashing function where the hash index is multiplied by 31 and added by the character unicode point.
    def hash(self,key): 
        table_size = self.actualSize
        hash_idx = 0
        for char in key:
            hash_idx = (33 * hash_idx + ord(char)) & 0xFFFFFFFF #simulates 32 bit overflow keeping the number under 32 bits for speed
        return hash_idx % table_size

# Linear probing
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

    def saveCSV(self, filename):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for entry in self.hashArray:
                    if entry.state == 1 and isinstance(entry.value, Patient):
                        p = entry.value
                        writer.writerow([p.id, p.name, p.age, p.dept, p.urgency, p.treatment_status])
        except Exception as e:
            print(f"Error saving: {e}")
   

    def loadCSV(self, filename):
        try:
            with open(filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for line in reader:
                    if len(line) == 2:
                        key, value = line
                        self.put(key, value)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Failed to load CSV: {e}")
        
    def loadFactor(self):
        return self.count / self.actualSize