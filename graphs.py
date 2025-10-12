from LinkedList import *
from stacksandqueues import *


class DSAGraph:
    def __init__(self):
        self.vertex = DSALinkedList()


    def getVertex(self, label):
        for v in self.vertex:
            if v.getLabel() == label:
                return v
        return None


    def addVertex(self, label, value=None):
        if self.getVertex(label) is not None:
            raise Exception('Department already exists')
        newVertex = DSAGraphVertex(label, value)
        self.vertex.insertLast(newVertex)


    def addEdge(self, fromLabel, toLabel, weight):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)

        if toVertex in fromVertex.getAdjacent():
            raise Exception('Corridor already exists')
        if fromVertex is None or toVertex is None:
            raise Exception('One or both departments not found')
        if fromVertex.getLabel() == toVertex.getLabel():
            raise Exception('Please choose two different departments')

        edge1 = DSAGraphEdge(fromVertex, toVertex, weight)
        edge2 = DSAGraphEdge(toVertex, fromVertex, weight)

        weight = float(weight)
        fromVertex.getAdjacent().insertLast(edge1)
        toVertex.getAdjacent().insertLast(edge2)


    def deleteVertex(self, label):
        vertex = self.getVertex(label)
        if vertex is None:
            raise Exception("Department not found")

        for v in self.vertex:
            if v.getLabel() != label:
                self.removeEdge(v.getAdjacent(), vertex)

        tempList = DSALinkedList()
        while not self.vertex.isEmpty():
            v = self.vertex.removeFirst()
            if v != vertex:
                tempList.insertLast(v)
        while not tempList.isEmpty():
            self.vertex.insertLast(tempList.removeFirst())


    def deleteEdge(self, fromLabel, toLabel):
        fromVertex = self.getVertex(fromLabel)
        toVertex = self.getVertex(toLabel)

        if fromVertex is None or toVertex is None:
            raise Exception("One or both departments not found")


        self.removeEdge(fromVertex.getAdjacent(), toVertex)
        self.removeEdge(toVertex.getAdjacent(), fromVertex)


    def removeEdge(self, adjList, targetVertex):    
        temp = DSALinkedList()
        while not adjList.isEmpty():
            edge = adjList.removeFirst()
            if edge.getToVertex() != targetVertex:
                temp.insertLast(edge)
        while not temp.isEmpty():
            adjList.insertLast(temp.removeFirst())



    def displayAsList(self):
        for vertex in self.vertex:
            print("Department: ",vertex.getLabel(), "|", end=" ")
            for edge in vertex.getAdjacent():
                toVertex = edge.getToVertex()
                weight = edge.getWeight()
                print(f"{toVertex.getLabel()} (lenght = {weight})", end=" ")
            print()


    def BFS(self,reference):
        T = DSAQueue()
        Q = DSAQueue()

        # Clear visited status for all vertices before starting
        for vertex in self.vertex:
            vertex.clearVisited()

        v = self.getVertex(reference)
        if v is None:
            raise Exception("Department not found")
            
        level = 0

        v.setVisited(True)
        Q.enqueue(v)
        Q.enqueue(None)

        while not Q.isEmpty():
            v = Q.dequeue()

            if v is None:
                level += 1
                if not Q.isEmpty():
                    Q.enqueue(None)
                continue

            for edge in sortAdjacentList(v.getAdjacent()):
                each = edge.getToVertex()
                if not each.getVisited():
                    T.enqueue((v, each, level+1))
                    each.setVisited(True)
                    Q.enqueue(each)
    
        print("BFS Traversal with levels:")
        while not T.isEmpty():
            fromVertex, toVertex, edgeLevel = T.dequeue()
            print(f"{fromVertex.getLabel()} -> {toVertex.getLabel()} (Level {edgeLevel})")
        print()

    def DFS(self, reference):
        T = DSAQueue()
        S = DSAStack()

        for vertex in self.vertex:
            vertex.clearVisited()

        v = self.getVertex(reference)
        if v is None:
            raise Exception("Department not found")
        v.setVisited(True)
        S.push(v)

        while not S.isEmpty():
            v = S.top()
            found_unvisited = False
            for edge in sortAdjacentList(v.getAdjacent()):
                each = edge.getToVertex()
                if not each.getVisited():
                    T.enqueue(v)
                    T.enqueue(each)
                    each.setVisited(True)
                    S.push(each)
                    found_unvisited = True
                    break
            if not found_unvisited:
                S.pop()

        print("DFS Traversal:")
        while not T.isEmpty():
            v = T.dequeue()
            print(v.getLabel(), end=" ")
        print()

# DFS cycle detect needs to be updated to list ALL cycles

    def DFS_cycle_detect(self):
        # Clear visited and parent for all vertices
        for vertex in self.vertex:
            vertex.clearVisited()
            vertex.setParent(None)

        cycle_nodes = []

        def dfs(v, parent, path):
            v.setVisited(True)
            v.setParent(parent)
            path.append(v)  # Track current path

            for edge in v.getAdjacent():
                adj = edge.getToVertex()
                if not adj.getVisited():
                    if dfs(adj, v, path):
                        return True
                elif adj != parent and adj in path:
                    # Cycle detected
                    # Extract the cycle nodes from path
                    cycle_start_index = path.index(adj)
                    cycle = path[cycle_start_index:]  # Nodes forming cycle
                    cycle_nodes.extend(cycle)
                    return True

            path.pop()  # Backtrack on path
            return False

        for vertex in self.vertex:
            if not vertex.getVisited():
                if dfs(vertex, None, []):
                    print("\nCycle Detected!")
                    print("\nCycle detected involving departments:")
                    print(" -> ".join([v.getLabel() for v in cycle_nodes]))
                    return cycle_nodes

        print("No cycle detected")
        return None

    def dijkstra(self, startLabel, endLabel):
        startVertex = self.getVertex(startLabel)
        endVertex = self.getVertex(endLabel)

        if startVertex is None or endVertex is None:
            raise Exception("One or both departments not found")

        # Initialize all vertices
        for vertex in self.vertex:
            vertex.setDistance(float('inf'))
            vertex.setPrevious(None)
            vertex.clearVisited()

        startVertex.setDistance(0)
        unvisited = list(self.vertex)

        while unvisited:
            # Sort by current distance
            unvisited.sort(key=lambda v: v.getDistance())
            current = unvisited.pop(0)

            current.setVisited(True)

            # Stop early if we reach the destination
            if current == endVertex:
                break

            for edge in current.getAdjacent():
                neighbor = edge.getToVertex()
                if not neighbor.getVisited():
                    try:
                        weight = float(edge.getWeight())
                    except ValueError:
                        raise Exception("Corridor lenght must be a number")

                    newDist = current.getDistance() + weight
                    if newDist < neighbor.getDistance():
                        neighbor.setDistance(newDist)
                        neighbor.setPrevious(current)

        # Reconstruct path
        path = []
        curr = endVertex
        while curr is not None:
            path.insert(0, curr.getLabel())
            curr = curr.getPrevious()

        distance = endVertex.getDistance()
        if distance == float('inf'):
            print(f"No path found from '{startLabel}' to '{endLabel}'.")
        else:
            print(f"Shortest path from '{startLabel}' to '{endLabel}':")
            print(" -> ".join(path))
            print(f"Total distance: {distance}")


def sortAdjacentList(adjList):
    sortedList = DSALinkedList()

    for current in adjList:
        inserted = False
        tempList = DSALinkedList()

        while not sortedList.isEmpty():
            v = sortedList.removeFirst()
            if not inserted and current.getToVertex().getLabel() < v.getToVertex().getLabel():
                tempList.insertLast(current)
                inserted = True
            tempList.insertLast(v)

        if not inserted:
            tempList.insertLast(current)

        while not tempList.isEmpty():
            sortedList.insertLast(tempList.removeFirst())

    return sortedList

class DSAGraphVertex:
    def __init__(self, label, value=None):
        self.label = label
        self.value = value
        self.edges = DSALinkedList()
        self.visited = False
        self.distance = float('inf')
        self.previous = None
    
    def getLabel(self):
        return self.label
    
    def getValue(self):
        return self.value
    
    def getAdjacent(self):
        return self.edges
    
    def getVisited(self):
        return self.visited
    
    def setVisited(self, visited):
        self.visited = True

    def clearVisited(self):
        self.visited = False

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance
    
    def setPrevious(self, prev):
        self.previous = prev

    def getPrevious(self):
        return self.previous
    
    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return getattr(self, 'parent', None)

    def toString(self):
        return f"Label: {self.label}, Value: {self.value}"

class DSAGraphEdge:
    def __init__(self, fromVertex, toVertex, weight):
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.weight = weight
        self.edges = DSALinkedList()

    def addEdge(self, vertex, weight):
        self.edges.insertLast(vertex)
        self.weight = weight

    def getFromVertex(self):
        return self.fromVertex

    def getToVertex(self):
        return self.toVertex

    def getEdges(self):
        return self.edges
    
    def getWeight(self):
        return self.weight
    
    def toString(self):
        return f"From: {self.fromVertex.getLabel()}, To: {self.toVertex.getLabel()}"
