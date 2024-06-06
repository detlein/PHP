import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

arr = [random.randint(0, 1000) for _ in range(10000)]
arr_copy1 = arr.copy()
arr_copy2 = arr.copy()
arr_copy3 = arr.copy()
arr_copy4 = arr.copy()
arr_copy5 = arr.copy()

start_time = time.time()
bubble_sort(arr)
end_time = time.time()

print(f"Отсортированный массив (пузырьковая сортировка): {arr}")
print(f"Время сортировки (пузырьковая сортировка): {end_time - start_time} секунд")

start_time = time.time()
selection_sort(arr_copy1)
end_time = time.time()

print(f"Отсортированный массив (сортировка выбором): {arr_copy1}")
print(f"Время сортировки (сортировка выбором): {end_time - start_time} секунд")

start_time = time.time()
insertion_sort(arr_copy2)
end_time = time.time()

print(f"Отсортированный массив (сортировка вставками): {arr_copy2}")
print(f"Время сортировки (сортировка вставками): {end_time - start_time} секунд")

start_time = time.time()
heap_sort(arr_copy3)
end_time = time.time()

print(f"Отсортированный массив (пирамидальная сортировка): {arr_copy3}")
print(f"Время сортировки (пирамидальная сортировка): {end_time - start_time} секунд")

start_time = time.time()
merge_sort(arr_copy4)
end_time = time.time()

print(f"Отсортированный массив (сортировка слиянием): {arr_copy4}")
print(f"Время сортировки (сортировка слиянием): {end_time - start_time} секунд")

start_time = time.time()
quick_sort(arr_copy5, 0, len(arr_copy5)-1)
end_time = time.time()

print(f"Отсортированный массив (быстрая сортировка): {arr_copy5}")
print(f"Время сортировки (быстрая сортировка): {end_time - start_time} секунд")
