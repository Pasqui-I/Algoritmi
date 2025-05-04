from typing import Any
import Sort.sort as sr
import Sort.Quick.quick_sort as qs
import Sort.Merge.merge_sort as ms

sorters: list[sr.Sort] = [qs.QuickSort(), ms.MergeSort()]
for sorter in sorters:
    # Example array to be sorted
    arr = [5, 3, 8, 1, 2, 7, 4, 6]

    # Print the original array and its length
    print("Original array:", arr, len(arr))

    # Sort the array using the sorter
    result: list[Any] | None = sorter.sort(arr)
    if result is not None:
        arr = result
    # Print the sorted array and its length
    print("Sorted array:", arr, len(arr))
