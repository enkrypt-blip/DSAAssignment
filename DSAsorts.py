
# Python file to hold all sorting methods


import numpy as np
    # Merge sort algorithm
def mergeSort(A):
    mergeSortRecurse(A, 0, len(A) - 1)
    return A

# Recursive helper for merge sort
def mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        
        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx + 1, rightIdx)

        merge(A, leftIdx, midIdx, rightIdx)
    else:
        return A

# Merge two sorted halves
def merge(A, leftIdx, midIdx, rightIdx):
    tempArr = np.zeros(rightIdx - leftIdx + 1, dtype=object)
    i = leftIdx
    j = midIdx + 1
    k = 0

    while i <= midIdx and j <=  rightIdx: 
        if A[i] < A[j]:
            tempArr[k] = A[i]
            i += 1
        else:
            tempArr[k] = A[j]
            j += 1
        k += 1
    
    for i in range(i, midIdx + 1):
        tempArr[k] = A[i]
        k += 1
    
    for j in range(j, rightIdx + 1):
        tempArr[k] = A[j]
        k += 1

    for k in range(leftIdx, rightIdx + 1):
        A[k] = tempArr[k - leftIdx]
    
    return A

# Quick sort algorithm
def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRecurse(A, 0, len(A) - 1)
    return A

# Recursive helper for quick sort
def quickSortRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx: 
        pivotIdx = leftIdx  
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        quickSortRecurse(A, leftIdx, newPivotIdx - 1)
        quickSortRecurse(A, newPivotIdx + 1, rightIdx)
    
    else: 
        return A

# Partitioning logic for quick sort
def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    pivotVal = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotVal

    currIdx = leftIdx

    for i in range(leftIdx, rightIdx):
        if A[i] < pivotVal:
            temp = A[currIdx]
            A[currIdx] = A[i]
            A[i] = temp
            currIdx += 1
    newPivotIdx = currIdx
    A[rightIdx] = A[newPivotIdx]
    A[newPivotIdx] = pivotVal

    return newPivotIdx

# Quick sort with median-of-three pivot selection
def quickSortMedian3(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortMedian3Recurse(A, 0, len(A) - 1)
    return A

# Recursive helper for quick sort with median-of-three
def quickSortMedian3Recurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx: 
        midIdx = (leftIdx + rightIdx) // 2
        pivotIdx = medianOf3(A, leftIdx, midIdx, rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        quickSortMedian3Recurse(A, leftIdx, newPivotIdx - 1)
        quickSortMedian3Recurse(A, newPivotIdx + 1, rightIdx)
    else: 
        return A
    
# Find median of three for pivot selection  
def medianOf3(A, leftIdx, midIdx, rightIdx):
    a = A[leftIdx]
    b = A[midIdx]
    c = A[rightIdx]

    if a <= b <= c or c <= b <= a:
        return midIdx
    elif b <= a <= c or c <= a <= b:
        return leftIdx
    else:
        return rightIdx
    
# Quick sort with random pivot selection
def quickSortRandom(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRandomRecurse(A, 0, len(A) - 1)
    return A
# Recursive helper for quick sort with random pivot
def quickSortRandomRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx: 
        import random
        pivotIdx = random.randint(leftIdx, rightIdx)
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        quickSortRandomRecurse(A, leftIdx, newPivotIdx - 1)
        quickSortRandomRecurse(A, newPivotIdx + 1, rightIdx)
    
    else: 
        return A
    