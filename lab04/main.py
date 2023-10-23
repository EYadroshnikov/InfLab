import sort


def delete_local_maxes(arr):
    if len(arr) < 3:
        return arr

    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            arr[i] = 0
    return [i for i in arr if i != 0]


def main():
    arr1 = [432, 786, 230, 574, 954, 719, 381, 567, 853]
    arr2 = [125, 789, 451, 893, 322, 667, 423, 540, 998, 234]
    arr3 = [764, 312, 678, 287, 451, 832, 56, 231, 789]
    print(f'{arr1}: {delete_local_maxes(arr1)}')
    print(f'{arr2}: {delete_local_maxes(arr2)}')
    print(f'{arr3}: {delete_local_maxes(arr3)}')


if __name__ == '__main__':
    main()
