# Assignment main program which integrates all modules and performs operations based on user input
from graphs import *
from hashes import *
from heaps import *
from DSAsorts import *
import timeit
import random

# Constants
RANDOM_TIMES = 100
NEARLY_PERCENT = 0.10

# Function to generate and sort dataset
def doSort(n, arrayType, sortType):
        A = np.arange(1, n+1, 1)
        if arrayType =='d': 
            for i in range(0, int(n/2)):
                temp = A[i]
                A[i] = A[n-i-1]
                A[n-i-1] = temp
            print("Descending: ", A)
        elif arrayType == 'r':
            for i in range(RANDOM_TIMES*n):
                x = int(random.random()*n)
                y = int(random.random()*n)
                temp = A[x]
                A[x] = A[y]
                A[y] = temp
            print("Random: ", A)
        elif arrayType == 'n':
            for i in range(int(n*NEARLY_PERCENT/2+1)):
                x = int(random.random()*n)
                y = int(random.random()*n)
                temp = A[x]
                A[x] = A[y]
                A[y] = temp
            print("Nearly sorted: ", A)
        elif arrayType == 'a':
            print("Ascending: ", A)

        else:
            print("Unsupported array type")
        
        if sortType == "m":
            mergeSort(A)
        elif sortType == "q":
            quickSort(A)
        else:
            print("Unsupported sort algorithm")

        print(f"Sorted array: {A}")

# Main program
hospital = DSAGraph()
records = DSAHashTable(10000)
scheduler = Scheduler(10000)

# Main menu loop
while True:
    print("\nMain Menu: ")
    print("1: Hospital Map")
    print("2: Patient records")
    print("3: Hospital schedule")
    print("4: Patient Sort")
    print("5: Test Data")
    print("6: Exit")

    mm = input("Enter your module: ")

# Menu for each module
    if mm == "1":
        one = True
        while one is True:
            print("\nMenu:")
            print("1: Add department")
            print("2: Remove department")
            print("3: Add corridor between departments")
            print("4: Remove corridor between departments")
            print("5: Display as list")
            print("6: Breadth first search with levels")
            print("7: Depth first search with cycle detection")
            print("8: Shortest path algorithm")
            print("9: Back")

            choice = input("Enter your choice (1-9): ")

            try:
                if choice == "1":
                    dept = input("Enter new department: ")
                    hospital.addVertex(dept)
                    print(f"{dept} added.")
                
                elif choice == "2":
                    dept = input("Enter the department to be deleted: ")
                    hospital.deleteVertex(dept)
                    print(f"{dept} removed.")

                elif choice == "3":
                    start = input("Enter the start department: ")
                    end = input("Enter the end department: ")
                    lenght = float(input("Enter the lenght of the corridor: "))
                    hospital.addEdge(start, end, lenght)
                    print(f"Corridor added between {start} and {end}.")

                elif choice == "4":
                    start = input("Enter the 'from' department: ")
                    end = input("Enter the 'to' department: ")
                    hospital.deleteEdge(start, end)

                elif choice == "5":
                    hospital.displayAsList()

                elif choice == "6":
                    start = input("Enter the start department: ")
                    hospital.BFS(start)
                    
                elif choice == "7":
                    start = input("Enter the start department: ")
                    hospital.DFS()
                    hospital.DFS_cycle_detect()
                
                elif choice == "8":
                    start = input("Enter the 'from' department: ")
                    end = input("Enter the 'to' department: ")
                    hospital.dijkstra(start, end)
                
                elif choice == "9":
                    one = False
                    break

            except Exception as err:
                print(f"Error: {err}")
        
    elif mm == "2":
        two = True
        while two is True:
            print("\nMenu: ")
            print("1: Add patient")
            print("2: Delete patient")
            print("3: Search patient")
            print("4: Back")

            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    id = input("Enter ID: ")
                    name = input("Enter Name: ")
                    age = int(input("Age: "))
                    dept = input("Department: ")
                    urg = int(input("Urgency level (1-5): "))
                    status = input("Status: ")
                    time = int(input("Estimated treatment time: "))  
                    p = Patient(id, name, age, dept, urg, status, time)
                    records.put(p.id, p)
                    print("Entry added/updated.")
                
                elif choice == "2":
                    delete = input("Enter ID to be deleted: ")
                    records.remove(delete)
                    print("Key successfuly removed")

                elif choice == "3":
                    search = input("Enter patient ID: ")
                    print(f"Patient {records.get(search)}")

                elif choice == "4":
                    two = False
                    break

            except Exception as err:
                print(f"An error occurred: {err}")
    elif mm == "3":
        three = True
        while three is True:
            print("\nMenu: ")
            print("1: Insert request")
            print("2: Remove request")
            print("3: Peek at next patient")
            print("4: Check patient priority")
            print("5: Update urgency level")
            print("6: Display schedule")
            print("7: Back")

            choice = input("Enter your choice (1-7): ")

            if choice == "1":
                id = input("Enter the patient ID: ")
                patient = records.get(id)
                scheduler.add_patient(id, patient.urgency, patient.treatment_time)

            elif choice == "2":
                try:
                    scheduler.heap.remove()
                except Exception as e:
                    print(f"Error removing patient: {e}")

            elif choice == "3":
                try:
                    next_patient = scheduler.heap.peek()
                    print(f"Next patient: {next_patient}")
                except Exception as e:
                    print(f"Error peeking at next patient: {e}")

            elif choice == "4":

                try:
                    priority = scheduler.getPriority(id)
                    print(f"Patient {id} has priority {round(priority, 2)}")
                except Exception as e:
                    print(f"Error retrieving priority: {e}")

            elif choice == "5":
                id = input("Enter the patient ID: ")
                new_urgency = int(input("Enter the new urgency level (1-5): "))
                scheduler.update_patient_priority(id, new_urgency)

            elif choice == "6":
                scheduler.heap.display()

            elif choice == "7":
                three = False
                break

    elif mm == "4":
        four = True
        while four is True:
            print("\nMenu: ")
            print("1: Quick Sort (Median of 3)")
            print("2: Merge Sort")
            print("3: Back")

            choice = input("Enter your choice (1-3): ")
            
            if choice == "1":
                times = records.getAllTimes()
                sorted_times = quickSortMedian3(times)
                print(f"Sorted times: {sorted_times}")

            elif choice == "2":
                times = records.getAllTimes()
                sorted_times = mergeSort(times)
                print(f"Sorted times: {sorted_times}")

            elif choice == "3":
                four = False
                break   

# Menu for test data
    elif mm == "5":
        # Pre-populated departments (vertices)
        d1 = hospital.addVertex("emergency")
        d2 = hospital.addVertex("cardiology")
        d3 = hospital.addVertex("neurology")
        d4 = hospital.addVertex("orthopedics")
        d5 = hospital.addVertex("pediatrics")
        d6 = hospital.addVertex("radiology")
        d7 = hospital.addVertex("oncology")
        d8 = hospital.addVertex("pharmacy")
        d9 = hospital.addVertex("surgery")
        d10 = hospital.addVertex("dermatology")
        d11 = hospital.addVertex("maternity")
        d12 = hospital.addVertex("urology") # <-- Isolated department
        print("\nDepartments added.")

        # Edges (Connections with weights)
        hospital.addEdge("emergency", "surgery", 5)
        hospital.addEdge("emergency", "radiology", 3)
        hospital.addEdge("emergency", "cardiology", 4)

        hospital.addEdge("cardiology", "neurology", 6)
        hospital.addEdge("cardiology", "oncology", 7)

        hospital.addEdge("neurology", "orthopedics", 8)
        hospital.addEdge("orthopedics", "surgery", 2)
        hospital.addEdge("orthopedics", "urology", 9)

        hospital.addEdge("pediatrics", "maternity", 4)
        hospital.addEdge("pediatrics", "dermatology", 6)

        hospital.addEdge("radiology", "oncology", 5)
        hospital.addEdge("radiology", "pharmacy", 3)

        hospital.addEdge("pharmacy", "dermatology", 2)
        hospital.addEdge("oncology", "surgery", 4)
        hospital.addEdge("urology", "maternity", 7)
        print("Corridors added.")


        p1 = Patient("1200", "Ankur", 19, "eng", 5, "a", 10)
        p2 = Patient("1300", "Jarod", 19, "sjnp", 2, "a", 20)
        p3 = Patient("1400", "Josh", 20, "sjnp", 3, "i", 30)
        p4 = Patient("1500", "Makayla", 19, "eng", 5, "a", 40)
        p5 = Patient("1600", "Sophie", 16, "schl", 4, "i", 50)
        p6 = Patient("6767", "Annas", 20, "rcr", 1, "a", 60)
        p7  = Patient("1700", "Liam", 25, "emergency", 3, "a", 25)
        p8  = Patient("1800", "Emma", 22, "cardiology", 4, "i", 35)
        p9  = Patient("1900", "Noah", 28, "neurology", 2, "a", 45)
        p10 = Patient("2000", "Olivia", 31, "orthopedics", 5, "a", 20)
        p11 = Patient("2100", "Ethan", 24, "pediatrics", 1, "i", 55)
        p12 = Patient("2200", "Ava", 27, "radiology", 3, "a", 15)
        p13 = Patient("2300", "Mason", 33, "oncology", 4, "a", 40)
        p14 = Patient("2400", "Isabella", 29, "pharmacy", 2, "i", 60)
        p15 = Patient("2500", "Lucas", 30, "surgery", 5, "a", 30)
        p16 = Patient("2600", "Mia", 23, "dermatology", 3, "i", 25)
        p17 = Patient("2700", "James", 35, "maternity", 2, "a", 50)
        p18 = Patient("2800", "Charlotte", 26, "urology", 1, "a", 40)
        p19 = Patient("2900", "Benjamin", 32, "psychiatry", 5, "i", 70)
        p20 = Patient("3000", "Harper", 21, "emergency", 4, "a", 20)
        print("Patients created.")

        records.put(p1.id, p1)
        records.put(p2.id, p2)
        records.put(p3.id, p3)
        records.put(p4.id, p4)
        records.put(p5.id, p5)
        records.put(p6.id, p6)
        records.put(p7.id, p7)
        records.put(p8.id, p8)
        records.put(p9.id, p9)
        records.put(p10.id, p10)
        records.put(p11.id, p11)
        records.put(p12.id, p12)
        records.put(p13.id, p13)
        records.put(p14.id, p14)
        records.put(p15.id, p15)
        records.put(p16.id, p16)
        records.put(p17.id, p17)
        records.put(p18.id, p18)
        records.put(p19.id, p19)
        records.put(p20.id, p20)
        print("Test data added.")

# Sort test data
        t = True
        while t is True:
            print("\nMenu: ")
            print("1: Generate and sort dataset")
            print("2: Back")

            choice = input("Enter your choice (1-2): ")

            if choice == "1":
                sortTpye = input("Enter sort type (m for Merge Sort, q for Quick Sort): ")
                size = int(input("Enter dataset size: "))
                arrayType = input("Enter array type (a, d, r, n): ")
                print(f"\nGenerating dataset of size {size} with type '{arrayType}' and sorting using '{sortTpye}'...")
                start_time = timeit.default_timer()
                doSort(size, arrayType, sortTpye)
                print
                end_time = timeit.default_timer()
                print(f"Sorting completed in {end_time - start_time} seconds.")

            elif choice == "2":
                t = False
                break

    elif mm == "6":
        print("Exiting program...")
        break

