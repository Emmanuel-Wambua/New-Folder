def intepolation_search(arr, n,x):
    low = 0
    high = (n - 1)

    while low <= high  and x >= arr[low] and x <= arr[high]:
        if low == high:
            if low == x:
                return low;
            return -1;

        pos = int(low + (((float(high - low)/(arr[high] - arr[low])) * (x - arr[low]))))

        if arr[pos] == x:
            return pos;

        if arr[pos] < x:
            low = pos + 1;

        else:
            high = pos - 1;

    return -1;


arr = [10, 11, 12, 13, 14, 15, 16, 17]

number = intepolation_search(arr, len(arr), 17)
print(number)