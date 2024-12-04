import random

#  pole s 10 hodnotami od 0-100
array = random.sample(range(101), 10)
print("Původní pole:", array)

# Bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Bogo sort
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def bogo_sort(arr):
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
    return arr, attempts

# Selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Řazení pomocí různých algoritmů
bubble_sorted = bubble_sort(array.copy())
bogo_sorted, bogo_attempts = bogo_sort(array.copy())
selection_sorted = selection_sort(array.copy())
insertion_sorted = insertion_sort(array.copy())

# Výstupy
print("Bubble sort:", bubble_sorted)
print("Bogo sort:", bogo_sorted, "(počet pokusů:", bogo_attempts, ")")
print("Selection sort:", selection_sorted)
print("Insertion sort:", insertion_sorted)
