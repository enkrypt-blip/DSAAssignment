import numpy as np
import csv

class Scheduler:
    def __init__(self, max_size=100):
        self.heap = DSAHeap(max_size)

    def compute_priority(self, urgency, treatment_time):
        if treatment_time <= 0:
            raise ValueError("Please enter a valid treatment time.")
        if not (1 <= urgency <= 5):
            raise ValueError("Please enter a value between 1 and 5")
        return (6- urgency) + (1000/treatment_time)
    
    
    def add_patient(self, patient_id, urgency, treatment_time):
        try:
            priority = self.compute_priority(urgency, treatment_time)
            value = f"{patient_id}, Urgency: {urgency}, Time: {treatment_time}"
            self.heap.add(priority, value)
            print(f"\n[Added] {value} --> Priority: {round(priority, 2)}")
            self.heap.display()
        except ValueError as e:
            print(f"Error adding patient {patient_id}: {e}")

    def next_patient(self):
        removed = self.heap.remove()
        if removed:
            print(f"[Next Patient] {removed.value} (Priority: {removed.priority})")
        
    def display_heap(self):
        self.heap.display()

class DSAHeapEntry:
    def __init__(self, priority=None, value=None):
        self.priority = priority
        self.value = value
    
    def getPriority(self):
        return self.priority
    
    def setPriority(self, priority):
        self.priority = priority
    
    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def __gt__(self, other):
        if not isinstance(other, DSAHeapEntry):
            return NotImplemented
        return self.priority > other.priority

    def __lt__(self, other):
        if not isinstance(other, DSAHeapEntry):
            return NotImplemented
        return self.priority < other.priority

    def __eq__(self, other):
        if not isinstance(other, DSAHeapEntry):
            return NotImplemented
        return self.priority == other.priority


class DSAHeap():
    def __init__(self, max_size=10000):
        self.heap = DSAHeapEntry()
        self.heap_array = np.zeros(max_size, dtype=object)
        self.count = 0
        self.max_size = max_size
    
    def add(self, priority, value):
        try:
            if self.count == self.max_size:
                raise Exception("Scheduler is full")
            priority = int(priority)
            newEntry = DSAHeapEntry(priority, value)
            self.heap_array[self.count] = newEntry
            self.count += 1
            self.trickleUp(self.heap_array, self.count - 1)
        except ValueError:
            print("Error: Priority must be a number.")
        except Exception as err:
            print(f"Error adding to scheduler: {err}")

    def remove(self):
        try:
            if self.count == 0:
                raise Exception("Scheduler is empty")
            root = self.heap_array[0]
            self.count -= 1
            self.heap_array[0] = self.heap_array[self.count]
            self.trickleDown(self.heap_array, 0, self.count)
            return root
        except Exception as e:
            print(f"Error removing from scheduler: {e}")

    def display(self):
        try:
            if self.count == 0:
                print("Scheduler is empty.")
            else:
                for i in range(self.count):
                    print(f"Priority: {self.heap_array[i].priority}, Patient ID: {self.heap_array[i].value}")
        except Exception as e:
            print(f"Error displaying scheduler: {e}")
    
    def trickleUp(self, heap_array, currIdx):
        parentIdx = (currIdx - 1) // 2
        while currIdx > 0 and heap_array[currIdx] > heap_array[parentIdx]:
            self.swap(heap_array, currIdx, parentIdx)
            self.trickleUp(heap_array, parentIdx)
        return heap_array
    
    def trickleDown(self, heap_array, currIdx, count):
        lChildIdx = currIdx * 2 + 1
        rChildIdx = lChildIdx + 1

        if lChildIdx < count:
            largeIdx = lChildIdx
            if rChildIdx < count:
                if heap_array[lChildIdx].priority < heap_array[rChildIdx].priority:
                    largeIdx = rChildIdx
            if heap_array[largeIdx] > heap_array[currIdx]:
                self.swap(heap_array, largeIdx, currIdx)
                self.trickleDown(heap_array, largeIdx, count)

    def swap(self, heap_array, idx1, idx2):
        temp = heap_array[idx1]
        heap_array[idx1] = heap_array[idx2]
        heap_array[idx2] = temp
        return heap_array
    
    def heapify(self, heap_array, numItems):
        for i in range(numItems // 2 - 1, -1, -1):
            self.trickleDown(heap_array, i, numItems)
        return self.heap_array
    
    def heapsort(self, heap_array, numItems):
        self.heapify(heap_array, numItems)
        for i in range(numItems-1, 0, -1):
            self.swap(heap_array, 0, i)
            self.trickleDown(heap_array, 0, i)
        return heap_array
    

    def load_csv(self, filename):
        try:
            with open(filename, mode='r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) >= 2:
                        self.add(row[0],row[1])
                    else:
                        print(f"Skipping invalid row: {row}")
            self.heapify(self.heap_array, self.count)

        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except ValueError:
            print("Error: Invalid data format in CSV.")
        except Exception as err:
            print(f"Failed to load CSV: {err}")

    def saveCSV(self, filename):
        try:
            sortedHeap = self.heapsort(self.heap_array[:self.count], self.count)[::-1]
            with open(filename, 'w') as file:
                for i in range(self.count):
                    file.write(f"{sortedHeap[i].priority},{sortedHeap[i].value}\n")
            print("Heap saved to CSV successfully.")
        except Exception as e:
            print(f"Error saving to CSV: {e}") 
                
def main():
    print("Heaps user interface")
    try:
        size = int(input("What will be the size of the heap? "))
        if size <= 0:
            raise ValueError("Heap size must be a positive integer")
        scheduler = Scheduler(size)
    except ValueError as err:
        print(f"Error: {err} using default heap of 10000")
        scheduler = Scheduler(10000)

    while True:
        print("\nOptions:")
        print("1: Add to heap")
        print("2: Remove from heap")
        print("3: Display heap")  
        print("4: Load from CSV")
        print("5: Save to CSV")
        print("6: Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == '1':
                priority = input("Enter priority: ")
                value = input("Enter value: ")

            elif choice == '3':
                print("Heap contents: ")


            elif choice == '4':
                filename = input("Enter CSV file name to load: ")
                print("CSV successfully loaded")

            elif choice == '5':
                filename = input("Enter CSV to save to: ")
                print("Heap saved to CSV")      

            elif choice == '6':
                print("Exitting program")
                break

            else:
                print("Invalid option")

        except Exception as err:
            print(f"An error: {err} occured")

if __name__ == "__main__":
    main()