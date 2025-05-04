from typing import Any
from Sort.sort import Sort  # Importing the Sort class from the sort module
# Define a QuickSort class to implement the QuickSort algorithm
class QuickSort(Sort):
    # Method to sort an array in-place using QuickSort
    def sort(self, array: list[Any]) -> None:
        # Base case: if the array has 1 or fewer elements, it's already sorted
        if len(array) <= 1:
            return

        # Choose the pivot element (middle element of the array)
        pivot: Any = array[len(array) // 2]

        # Declare variables for the partitions
        left_partion: list[Any]  # Elements less than the pivot
        middle_partion: list[Any]  # Elements equal to the pivot
        right_partition: list[Any]  # Elements greater than the pivot

        # Create the partitions by comparing elements with the pivot
        left_partion, middle_partion, right_partition = self.__create_partitions(array, pivot)

        # Recursively sort the left and right partitions
        self.sort(left_partion)
        self.sort(right_partition)

        # Combine the sorted partitions back into the original array
        array[:] = left_partion + middle_partion + right_partition

    # Private helper method to create partitions based on the pivot
    def __create_partitions(
        self, array: list[Any], pivot: Any
    ) -> tuple[list[Any], list[Any], list[Any]]:
        # Elements less than the pivot
        left = [x for x in array if x < pivot]

        # Elements equal to the pivot
        middle = [x for x in array if x == pivot]

        # Elements greater than the pivot
        right = [x for x in array if x > pivot]

        # Return the three partitions as a tuple
        return (left, middle, right)


# Main block to demonstrate the usage of the QuickSort class
if __name__ == "__main__":
    # Create an instance of the QuickSort class
    sorter = QuickSort()

    # Example array to be sorted
    arr = [True, False, True, False, True, False]

    # Print the original array and its length
    print("Original array:", arr, len(arr))

    # Sort the array using the QuickSort class
    sorter.sort(arr)

    # Print the sorted array and its length
    print("Sorted array:", arr, len(arr))
    # Example array to be sorted
    