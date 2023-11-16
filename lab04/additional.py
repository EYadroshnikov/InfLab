def delete_local_maxes(arr, is_max=True):
    if len(arr) < 3:
        return arr

    res = arr.copy()
    for i in range(1, len(arr) - 1):
        if (is_max and arr[i] > arr[i - 1] and arr[i] > arr[i + 1]) or (
                not is_max and arr[i] < arr[i - 1] and arr[i] < arr[i + 1]):
            res[i] = 0
    return res


arr1 = [432, 786, 230, 574, 954, 719, 381, 567, 853]
arr2 = [125, 789, 451, 893, 322, 667, 423, 540, 998, 234]
arr3 = [764, 312, 678, 287, 451, 832, 56, 231, 789]
print(f'original: {arr1}')
print(f'maxes: {delete_local_maxes(arr1)}')
print(f'minimums: {delete_local_maxes(arr1, is_max=False)}')
