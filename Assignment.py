from graphs import *
from hashes import *
from heaps import *
from DSAsorts import *

hospital = DSAGraph()
records = DSAHashTable(20)
scheduler = Scheduler(100)

p1 = Patient("1200", "Ankur", 19, "eng", 5, "a", 10)
p2 = Patient("1300", "Jarod", 19, "sjnp", 2, "a", 20)
p3 = Patient("1400", "Josh", 20, "sjnp", 3, "i", 30)
p4 = Patient("1500", "Makayla", 19, "eng", 5, "a", 40)
p5 = Patient("1600", "Sophie", 16, "schl", 4, "i", 50)
p6 = Patient("6767", "Annas", 20, "rcr", 1, "a", 60)

records.put("1200", p1)
records.put("1300", p2)
records.put("1400", p3)
records.put("1500", p4)
records.put("1600", p5)
records.put("6767", p6)

while True:
    print("\nMain Menu: ")
    print("1: Hospital Map")
    print("2: Patient records")
    print("3: Hospital schedule")
    print("4: Patient Sort")
    print("5: Exit program")

    mm = input("Enter your module: ")

    if mm == "1":
        print("\nMenu:")
        print("1: Add department")
        print("2: Remove department")
        print("3: Add corridor between departments")
        print("4: Remove corridor between departments")
        print("5: Display as list")
        print("6: Breadth first search with levels")
        print("7: Depth first search with cycle detection")
        print("8: Shortest path algorithm")
        print("9: Exit program")

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
                print("Exitting program...")
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

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                id = input("Enter the patient ID: ")
                treatment_time = int(input("Enter estimated treatment time: "))
                patient = records.get(id)
                scheduler.add_patient(id, patient.urgency, treatment_time)

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
        while True:
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
                break   
             
    elif mm == "5":
        print("Exitting program...")
        break

