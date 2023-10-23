def quicksort(arr):
    if len(arr) <= 1:
        return arr
    n = arr[len(arr) // 2]
    l_arr = [i for i in arr if i < n]
    c_arr = [n] * arr.count(n)
    # c_arr = [i for i in arr if i == n]
    r_arr = [i for i in arr if i > n]
    return quicksort(l_arr) + c_arr + quicksort(r_arr)