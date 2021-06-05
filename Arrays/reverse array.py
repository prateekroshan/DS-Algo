# Iterative python program to reverse an array

# Function to reverse A[] from start to end

# def reverse_arr(arr, start, end):
#     start = 0
#     end = len(arr) - 1
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#
#
# A = [1, 2, 3, 4, 5, 6]
#
# print(reverse_arr(A, 0, 5))
# print("Reversed list is")
# print(A)
#

# recursive way

# def reverse_arr2(arr, start, end):
#     if start >= end:
#         return
#     arr[start], arr[end] = arr[end], arr[start]
#     reverse_arr2(arr, start + 1, end - 1)
#
#
# A = [1, 2, 3, 4, 5, 6]
# print(A)
# reverse_arr2(A, 0, 5)
# print("Reversed list is")
# print(A)

# slicing

# def reverse_arr(arr):
#   print(arr[::-1])


# A = [1, 2, 3, 4, 5, 6]
# reverse_arr(A)

def reverse_arr(arr):
    start_index = 0
    end_index = len(arr) - 1

    while start_index < end_index:
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

    return arr


if __name__ == "__main__":
    A = [1, 5, 6, 4, 7, 8, 2]

    print(reverse_arr(A))
