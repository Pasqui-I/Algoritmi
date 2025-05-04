from typing import Any  # Importing the `Any` type from the `typing` module for type annotations.
from Sort.sort import Sort  # Importing the `Sort` class from the `sort` module, which is presumably an abstract base class for sorting
# Defining a class `MergeSort` that implements the merge sort algorithm.
class MergeSort(Sort):
    # Method to sort an array using merge sort.
    def sort(self, array: list[Any]) -> list[Any]:
        # Base case: if the array has 1 or no elements, it is already sorted.
        if len(array) <= 1:
            return array

        # Finding the middle index of the array.
        middle: int = len(array) // 2

        # Recursively sorting the left and right halves of the array.
        left: list[Any] = self.sort(array[:middle])
        right: list[Any] = self.sort(array[middle:])

        # Merging the sorted halves and returning the result.
        return self.__merge(left, right)

    # Private method to merge two sorted arrays into one sorted array.
    def __merge(self, left: list[Any], right: list[Any]) -> list[Any]:
        result: list[Any] = list()  # Initializing an empty list to store the merged result.

        i: int = 0  # Pointer for the left array.
        j: int = 0  # Pointer for the right array.

        # Merging the two arrays by comparing their elements.
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:  # If the current element in the left array is smaller or equal.
                result.append(left[i])  # Add it to the result.
                i += 1  # Move the pointer in the left array.
            else:  # Otherwise, the current element in the right array is smaller.
                result.append(right[j])  # Add it to the result.
                j += 1  # Move the pointer in the right array.

        # Adding any remaining elements from the left array to the result.
        result.extend(left[i:])
        # Adding any remaining elements from the right array to the result.
        result.extend(right[j:])
        return result  # Returning the merged sorted array.

# Main block to demonstrate the usage of the `MergeSort` class.
if __name__ == "__main__":
    sorter = MergeSort()  # Creating an instance of the `MergeSort` class.
    arr = [3, 6, 8, 10, 1, 2, 1]  # Example array to be sorted.
    print("Original array:", arr, len(arr))  # Printing the original array and its length.
    arr = sorter.sort(arr)  # Sorting the array using the `sort` method.
    print("Sorted array:", arr, len(arr))  # Printing the sorted array and its length.