import sort


def delete_local_maxes(arr):
    if len(arr) < 3:
        return arr

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            arr[i] = 0
    return arr


def main():
    arr1 = [432, 786, 230, 574, 954, 719, 381, 567, 853]
    arr2 = [125, 789, 451, 893, 322, 667, 423, 540, 998, 234]
    arr3 = [764, 312, 678, 287, 451, 832, 56, 231, 789]
    print(
        f'test1:\n    original: {arr1}\n    sorted: {sort.quicksort(arr1)}\n    without local maxes: {delete_local_maxes(arr1)}\n')
    print(
        f'test2:\n    original: {arr2}\n    sorted: {sort.quicksort(arr2)}\n    without local maxes: {delete_local_maxes(arr2)}\n')
    print(
        f'test3:\n    original: {arr3}\n    sorted: {sort.quicksort(arr3)}\n    without local maxes: {delete_local_maxes(arr3)}\n')


if __name__ == '__main__':
    main()
