def zeros(arr):
    j = 0
    for num in arr:
        if num != 0:
            arr[j] = num
            j = j + 1

    for num in range(j, len(arr)):
        arr[num] = 0
    print(arr)


if __name__ == '__main__':
    A = [1, 4, 0, 6, 0, 7, 0]
    zeros(A)

