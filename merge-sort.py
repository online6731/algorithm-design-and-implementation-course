import random


class Sort():
    """
    Implementation of sorting algorithms
    """

    @staticmethod
    def merge(arr1, arr2):
        arr = []
        arr1_index, arr2_index = 0, 0
        arr1 += [float('inf')]
        arr2 += [float('inf')]
        for i in range(len(arr1) + len(arr2) - 2):
            if arr1[arr1_index] < arr2[arr2_index]:
                arr.append(arr1[arr1_index])
                arr1_index += 1
            else:
                arr.append(arr2[arr2_index])
                arr2_index += 1
        return arr

    @staticmethod
    def merge_sort(arr):
        if len(arr) == 1:
            return arr
        else:
            arr1 = Sort.merge_sort(arr[:len(arr)//2])
            arr2 = Sort.merge_sort(arr[len(arr)//2:])
            return Sort.merge(arr1, arr2)

    @staticmethod
    def test(method, input_text):
        arr = list(map(int, input_text.split()))
        print('Initial Array:', arr)
        print('Sorted  Array:', method(arr))
        return method(arr) == sorted(arr)


if __name__ == '__main__':
    arr = ' '.join([str(random.randint(0, 100)) for i in range(10)])
    print(Sort.test(Sort.merge_sort, arr))
